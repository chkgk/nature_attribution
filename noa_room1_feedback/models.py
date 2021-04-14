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
Room 1 App for Nature of Attribution
'''


class Constants(BaseConstants):
    name_in_url = 'noa_room1_feedback'
    players_per_group = None
    num_rounds = 1

    max_group_match_waiting = 180  # seconds

    max_price = 0.5
    min_price = 0.0


class Subsession(BaseSubsession):
    max_pay = models.CurrencyField()
    ball_green_probability = models.FloatField()

    def creating_session(self):
        self.max_pay = self.session.config.get('max_pay', False)
        red_balls = self.session.config.get('red_balls', False)
        green_balls = self.session.config.get('green_balls', False)

        if not all([self.max_pay, red_balls, green_balls]):
            raise Exception('Session not configured properly')
        self.ball_green_probability = green_balls / (green_balls + red_balls)

        for player in self.get_players():
            # set all variables on the player so that they are included in exports
            player.nc_treatment = self.session.vars['nc_treatment']
            player.wtp_treatment = self.session.vars['wtp_treatment']
            if self.session.vars['wtp_treatment']:
                player.wtp_round_1 = self.session.vars['wtp_round_1']
            player.payment_room_1 = player.participant.vars['payment_room_1']

    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) >= 2:
            group = waiting_players[:2]

            return group

        # we only get here, if not enough players are waiting
        # every 30 seconds (approx.) the wait page reloads. These reloads trigger this method.
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
    nc_treatment = models.BooleanField(initial=False)
    wtp_treatment = models.BooleanField(initial=False)
    wtp_round_1 = models.BooleanField()

    wants_to_know = models.BooleanField()

    # round payment indicator
    payment_room_1 = models.BooleanField()

    action = models.BooleanField()
    other_b_r1 = models.BooleanField()
    partner_id_in_subsession = models.IntegerField()
    game_payoff = models.CurrencyField()
    info_price = models.CurrencyField()
    info_bought = models.BooleanField()
    wtp_payment = models.CurrencyField()
    wtp_result = models.CurrencyField()
    dropped_out = models.BooleanField(initial=False)

    def matching_takes_too_long(self):
        now = time.time()
        return now - self.participant.vars.get('r1_start_wait', now) > Constants.max_group_match_waiting

    def set_partner_action(self):
        if self.dropped_out:
            return
        self.action = self.participant.vars.get('action1_b')
        partner = self.get_others_in_group()[0]
        self.partner_id_in_subsession = partner.id_in_subsession
        self.participant.vars["partner_1"] = self.partner_id_in_subsession
        self.other_b_r1 = partner.participant.vars.get('action1_b')

    def calculate_game_round_payoff(self):
        if not self.dropped_out:
            if self.group.ball_green:
                if self.action and self.other_b_r1:
                    self.game_payoff = c(0)
                elif self.action and not self.other_b_r1:
                    self.game_payoff = self.subsession.max_pay
                elif not self.action and self.other_b_r1:
                    self.game_payoff = c(1)
                else:
                    self.game_payoff = c(1)
            else:
                self.game_payoff = c(0)
        else:
            self.game_payoff = c(0)

        self.participant.vars["game_payoff_1"] = self.game_payoff
        self.participant.vars["ball_green_1"] = self.group.ball_green

    def bdm_mechanism(self):
        self.info_price = c(Constants.min_price + (random.random() * (Constants.max_price - Constants.min_price)))
        if self.wtp_payment >= self.info_price:
            self.info_bought = True
            self.wtp_result = Constants.max_price - self.info_price
        else:
            self.info_bought = False
            self.wtp_result = Constants.max_price

    def set_room_payoff(self):
        if self.wtp_treatment and self.wtp_round_1 and self.wants_to_know:
            self.participant.vars['room_payoff_1'] = self.game_payoff + self.wtp_result
        else:
            self.participant.vars['room_payoff_1'] = self.game_payoff