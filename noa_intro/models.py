from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

import random

author = 'Christian König gen. Kersting'

doc = """
Intro App for Nature of Attribution Project
"""


class Constants(BaseConstants):
    name_in_url = 'noa_intro'
    players_per_group = None
    num_rounds = 1

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
        treatment = self.session.config.get('treatment')
        self.set_treatment_vars(treatment)

    def set_treatment_vars(self, treatment):
        # determine the treatment indicators for the session
        cc_treatment = 'CC' in treatment
        aa_treatment = 'AA' in treatment
        ra_treatment = 'RA' in treatment
        nc_treatment = 'NC' in treatment
        wtp_treatment = 'WTP' in treatment

        for player in self.get_players():
            # set all variables on the player so that they are included in exports
            player.aa_treatment = aa_treatment
            player.ra_treatment = ra_treatment
            player.cc_treatment = cc_treatment
            player.nc_treatment = nc_treatment
            player.wtp_treatment = wtp_treatment
            player.payment_room_1 = random.choice([True, False])

            # also set them on the participant, so we can use them in other apps
            player.participant.vars["aa_treatment"] = aa_treatment
            player.participant.vars["ra_treatment"] = ra_treatment
            player.participant.vars["cc_treatment"] = cc_treatment
            player.participant.vars["nc_treatment"] = nc_treatment
            player.participant.vars["wtp_treatment"] = wtp_treatment
            player.participant.vars["payment_room_1"] = player.payment_room_1


class Group(BaseGroup):
    debug_treatment = models.StringField(choices=[
        'RA',
        'AA',
        'CC_RA',
        'CC_AA',
        'RA_NC',
        'AA_NC',
        'RA_NC_WTP',
        'AA_NC_WTP',
        'CC_RA_NC_WTP',
        'CC_AA_NC_WTP'
    ],
    initial='RA')


class Player(BasePlayer):
    # treatment indicators
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)
    cc_treatment = models.BooleanField(initial=False)
    nc_treatment = models.BooleanField(initial=False)
    wtp_treatment = models.BooleanField(initial=False)

    # round payment indicator
    payment_room_1 = models.BooleanField()

    # comprehension check fields
    c1_coplayer = models.IntegerField(widget=widgets.RadioSelect)  # questions are on the template to work for CC and non-CC

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
        choices=[[1, 'US$ 0'],
                 [2, 'US$ 1'],
                 [3, 'US$ 3']],
        label="4. What is your payout if your action is A, your co-player’s action is B, and the ball is red?",
        widget=widgets.RadioSelect)

    c5_payoff_ab_green = models.IntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        label="5. What is your payout if your action is A, your co-player’s action is B, and the ball is green?",
        widget=widgets.RadioSelect)

    c6_payoff_bb_green = models.IntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        label="6. What is your payout if your action is B, your co-player’s action is B, and the ball is green?",
        widget=widgets.RadioSelect)

    c7_payoff_ba_green = models.IntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        label="7. What is your payout if your action is B, your co-player’s action is A, and the ball is green?",
        widget=widgets.RadioSelect)
