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

author = 'Christian König gen. Kersting'

doc = """
Room 1 App for Nature of Attribution
"""


class Constants(BaseConstants):
    name_in_url = 'noa_room1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.aa_treatment = player.participant.vars.get('aa_treatment', False)
            player.ra_treatment = player.participant.vars.get('ra_treatment', False)
            player.cc_treatment = player.participant.vars.get('cc_treatment', False)
            player.nc_treatment = player.participant.vars.get('nc_treatment', False)
            player.wtp_treatment = player.participant.vars.get('wtp_treatment', False)
            player.payment_room_1 = player.participant.vars.get('payment_room_1', False)


    def set_treatment_vars(self, treatment):
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

    prefers_b = models.BooleanField(
        choices=[(False, 'Action A'), (True, 'Action B')],
        label="A final question, for which there is no right or wrong answer: Which action would you choose?",
        widget=widgets.RadioSelect)

    action1_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelect(),
        label="Which action do you choose?")

    # beliefs
    green_red_r1 = models.IntegerField(min=0, max=100)
    a_or_b_r1 = models.IntegerField(min=0, max=100)