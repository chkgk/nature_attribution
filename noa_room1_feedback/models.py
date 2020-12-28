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

    max_group_match_waiting = 15  # seconds

    ball_green_probability = 0.8
    action_b_probability = 0.4

    max_price = 0.5
    min_price = 0.0

    # note: False = red, True = green
    payoff_matrix = {
        False:
            {
                False: 1,
                True: 1
            },
        True:
            {
                False: 3,
                True: 0
            }
    }


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        # immediately advance players in the CC treatment
        if waiting_players:
            if waiting_players[0].cc_treatment:
                return [waiting_players[0]]

        if len(waiting_players) >= 2:
            group = waiting_players[:2]

            for p in group:
                p.set_treatment_vars()

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
        self.ball_green = random.random() < Constants.ball_green_probability


class Player(BasePlayer):
    # treatment indicators
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)
    cc_treatment = models.BooleanField(initial=False)
    nc_treatment = models.BooleanField(initial=False)
    wtp_treatment = models.BooleanField(initial=False)

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
        self.action = self.participant.vars.get('action1_b')
        if self.cc_treatment:
            self.partner_id_in_subsession = None
            self.participant.vars['partner_1'] = None
            self.other_b_r1 = random.random() < Constants.action_b_probability
        else:
            partner = self.get_others_in_group()[0]
            self.partner_id_in_subsession = partner.id_in_subsession
            self.participant.vars["partner_1"] = self.partner_id_in_subsession
            self.other_b_r1 = partner.participant.vars.get('action1_b')

    def calculate_game_round_payoff(self):
        if self.other_b_r1 is not None:
            if self.group.ball_green:
                self.game_payoff = c(Constants.payoff_matrix[self.action][self.other_b_r1])
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
        if self.wtp_treatment:
            self.participant.vars['room_payoff_1'] = self.game_payoff + self.wtp_result
        else:
            self.participant.vars['room_payoff_1'] = self.game_payoff

    def set_treatment_vars(self):
        self.aa_treatment = self.participant.vars.get('aa_treatment', False)
        self.ra_treatment = self.participant.vars.get('ra_treatment', False)
        self.cc_treatment = self.participant.vars.get('cc_treatment', False)
        self.nc_treatment = self.participant.vars.get('nc_treatment', False)
        self.wtp_treatment = self.participant.vars.get('wtp_treatment', False)
        self.payment_room_1 = self.participant.vars.get('payment_room_1', False)