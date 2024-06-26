from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import time

author = 'Christian König gen. Kersting'

doc = '''
Room 2 App for Nature of Attribution
'''


class Constants(BaseConstants):
    name_in_url = 'noa_room2_feedback'
    players_per_group = None
    num_rounds = 1

    max_group_match_waiting = 180  # seconds

    max_price = 0.5
    min_price = 0.0


class Subsession(BaseSubsession):
    ball_green_probability = models.FloatField()
    max_pay = models.CurrencyField()

    def creating_session(self):
        self.max_pay = self.session.config.get('max_pay', False)
        red_balls = self.session.config.get('red_balls', False)
        green_balls = self.session.config.get('green_balls', False)

        if not all([self.max_pay, red_balls, green_balls]):
            raise Exception('Session not configured properly')
        self.ball_green_probability = green_balls / (green_balls + red_balls)

        for player in self.get_players():
            # set all variables on the player so that they are included in exports
            player.treatment = self.session.vars['treatment']
            player.wtp_treatment = self.session.vars['wtp_treatment']
            if self.session.vars['wtp_treatment']:
                player.wtp_round_1 = self.session.vars['wtp_round_1']
            player.payment_room_1 = player.participant.vars['payment_room_1']

    def group_by_arrival_time_method(self, waiting_players):
        # make sure to advance dropped out players immediately
        for wp in waiting_players:
            if wp.participant.vars.get('dropout', False):
                wp.dropped_out = True
                return [wp]

        # now we match players, making sure that they continue with a stranger
        if len(waiting_players) >= 2:
            for p in waiting_players:
                for q in waiting_players:
                    if p == q:
                        continue
                    if p.id_in_subsession != q.participant.vars.get('partner_1', None):
                        return [p, q]

        # we only get here, if not enough active players are waiting
        # now we have time to check if somebody has been waiting for too long. if so, we advance them
        for p in waiting_players:
            if p.matching_takes_too_long():
                p.dropped_out = True
                p.participant.vars['dropout'] = True
                return [p]  # make sure your app can handle a group with size 1


class Group(BaseGroup):
    ball_green = models.BooleanField(doc="True (1) if color of ball drawn is green in round 1, else False (0).")

    def draw_ball(self):
        self.ball_green = random.random() < self.subsession.ball_green_probability


class Player(BasePlayer):
    # treatment indicators
    treatment = models.StringField()
    wtp_treatment = models.BooleanField(initial=False)
    wtp_round_1 = models.BooleanField(initial=True)

    wants_to_know = models.BooleanField(initial=False)

    # round payment indicator
    payment_room_1 = models.BooleanField()

    action = models.BooleanField()
    other_b_r2 = models.BooleanField()
    partner_id_in_subsession = models.IntegerField()
    game_payoff = models.CurrencyField()

    info_price = models.CurrencyField()
    info_bought = models.BooleanField(initial=False)
    wtp_payment = models.CurrencyField()
    wtp_result = models.CurrencyField()

    dropped_out = models.BooleanField(initial=False)

    def matching_takes_too_long(self):
        now = time.time()
        return now - self.participant.vars.get('r2_start_wait', now) > Constants.max_group_match_waiting

    def set_partner_action(self):
        if self.dropped_out:
            return
        self.action = self.participant.vars.get('action_b_r2')
        partner = self.get_others_in_group()[0]
        self.partner_id_in_subsession = partner.id_in_subsession
        self.participant.vars["partner_2"] = self.partner_id_in_subsession
        self.other_b_r2 = partner.participant.vars.get('action_b_r2')
        self.participant.vars['other_b_r2'] = self.other_b_r2

    def calculate_game_round_payoff(self):
        if not self.dropped_out:
            if self.group.ball_green:
                if self.action and self.other_b_r2:
                    self.game_payoff = c(0)
                elif self.action and not self.other_b_r2:
                    self.game_payoff = self.subsession.max_pay
                elif not self.action and self.other_b_r2:
                    self.game_payoff = c(1)
                else:
                    self.game_payoff = c(1)
            else:
                self.game_payoff = c(0)
        else:
            self.game_payoff = c(0)

        self.participant.vars["game_payoff_2"] = self.game_payoff
        self.participant.vars["ball_green_2"] = self.group.ball_green

    def bdm_mechanism(self):
        self.info_price = c(Constants.min_price + (random.random() * (Constants.max_price - Constants.min_price)))
        self.info_bought = self.wtp_payment >= self.info_price

    def set_room_payoff(self):
        if self.info_bought:
            self.wtp_result = Constants.max_price - self.info_price
        else:
            self.wtp_result = Constants.max_price

        if self.wtp_treatment and not self.wtp_round_1:
            self.participant.vars['room_payoff_2'] = self.game_payoff + self.wtp_result
        else:
            self.participant.vars['room_payoff_2'] = self.game_payoff

        if self.payment_room_1:
            self.payoff = self.participant.vars.get('room_payoff_1', 0)
        else:
            self.payoff = self.participant.vars.get('room_payoff_2', 0)

        self.participant.vars['payment'] = self.payoff
