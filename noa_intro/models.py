from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

from otree.api import Currency as c

import random

author = 'Christian König gen. Kersting'

doc = '''
Intro App for Nature of Attribution Project
'''


class Constants(BaseConstants):
    name_in_url = 'noa_intro'
    players_per_group = None
    num_rounds = 1

    max_quiz_attempts = 3

    comprehension_solutions = {
        'c1_coplayer': 2,
        'c2_probabilities': 1,
        'c3_decision_importance': 2,
        'c4_payoff_ab_red': 1,
        'c5_payoff_ab_green': 2,
        'c6_payoff_bb_green': 1,
        'c7_payoff_ba_green': 3
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        max_pay = self.session.config.get('max_pay', False)
        red_balls = self.session.config.get('red_balls', False)
        green_balls = self.session.config.get('green_balls', False)
        announce_q = self.session.config.get('announce_q', False)

        if not all([max_pay, red_balls, green_balls]):
            raise Exception('Session not configured properly')

        for g in self.get_groups():
            g.max_pay = c(max_pay)
            g.red_balls = red_balls
            g.green_balls = green_balls
            g.announce_q = announce_q

        treatment = self.session.config.get('treatment', None)
        if not treatment:
            raise Exception('Treatment not set')

        self.session.vars['treatment'] = treatment
        if treatment in ['IM', 'FI']:
            self.session.vars['wtp_treatment'] = True
            self.session.vars['wtp_round_1'] = treatment == 'IM'
        else:
            self.session.vars['wtp_treatment'] = False

        for player in self.get_players():
            player.participant.vars['payment_room_1'] = random.randint(1, 2) == 1

            # set all variables on the player so that they are included in exports
            player.treatment = self.session.vars['treatment']
            player.wtp_treatment = self.session.vars['wtp_treatment']
            if self.session.vars['wtp_treatment']:
                player.wtp_round_1 = self.session.vars['wtp_round_1']
            player.payment_room_1 = player.participant.vars['payment_room_1']


class Group(BaseGroup):
    max_pay = models.CurrencyField()
    red_balls = models.IntegerField()
    green_balls = models.IntegerField()
    announce_q = models.BooleanField()


class Player(BasePlayer):
    # treatments
    treatment = models.StringField()
    wtp_treatment = models.BooleanField(initial=False)
    wtp_round_1 = models.BooleanField()

    # round payment indicator
    payment_room_1 = models.BooleanField()

    # comprehension check fields
    c_attempts1 = models.IntegerField(initial=0)
    c_attempts2 = models.IntegerField(initial=0)

    c1_coplayer = models.IntegerField(choices=[
            [1, 'the same participant in both rounds.'],
            [2, 'a different participant in each round.']
        ],
        label='1. Which of the following is correct? In the first round and in the second round, my co-player is',
        widget=widgets.RadioSelect)  # questions are on the template to work for CC and non-CC

    c2_probabilities = models.IntegerField(
        choices=[[1, 'choose A more often than B.'],
                 [2, 'choose B more often than A.'],
                 [3, 'choose A and B equally often.']],
        label='2. Which of the following is correct? On average, co-players',
        widget=widgets.RadioSelect)

    c3_decision_importance = models.IntegerField(
        choices=[[1, 'The outcome of round 1 is less important than the outcome of round 2.'],
                 [2, 'The outcomes of both rounds are equally important.'],
                 [3, 'The outcome of round 2 is less important than the outcome of round 1.']],
        label='3. Remember that only one of the two rounds counts for your payment, with equal chance. What does this mean?',
        widget=widgets.RadioSelect)

    c4_payoff_ab_red = models.IntegerField(
        choices=[(1, '0'), (2, '1'), (3, '')],
        label='1. What is your payout if your action is A, your co-player’s action is B, and the ball is red?',
        widget=widgets.RadioSelect)

    c5_payoff_ab_green = models.IntegerField(
        choices=[(1, '0'), (2, '1'), (3, '')],
        label='2. What is your payout if your action is A, your co-player’s action is B, and the ball is green?',
        widget=widgets.RadioSelect)

    c6_payoff_bb_green = models.IntegerField(
        choices=[(1, '0'), (2, '1'), (3, '')],
        label='3. What is your payout if your action is B, your co-player’s action is B, and the ball is green?',
        widget=widgets.RadioSelect)

    c7_payoff_ba_green = models.IntegerField(
        choices=[(1, '0'), (2, '1'), (3, '')],
        label='4. What is your payout if your action is B, your co-player’s action is A, and the ball is green?',
        widget=widgets.RadioSelect)

    action_b = models.BooleanField(
        choices=[(False, 'A'), (True, 'B')],
        widget=widgets.RadioSelect(),
        label='Which action do you choose?')
