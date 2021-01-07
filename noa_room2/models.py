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

author = 'Christian König gen. Kersting'

doc = '''
Room 2 App for Nature of Attribution
'''


class Constants(BaseConstants):
    name_in_url = 'noa_room2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # set all variables on the player so that they are included in exports
            player.aa_treatment = self.session.vars['aa_treatment']
            player.ra_treatment = self.session.vars['ra_treatment']
            player.cc_treatment = self.session.vars['cc_treatment']
            player.nc_treatment = self.session.vars['nc_treatment']
            player.wtp_treatment = self.session.vars['wtp_treatment']
            player.payment_room_1 = self.session.vars['payment_room_1']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # treatment indicators
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)
    cc_treatment = models.BooleanField(initial=False)
    nc_treatment = models.BooleanField(initial=False)
    wtp_treatment = models.BooleanField(initial=False)

    # round payment indicator
    payment_room_1 = models.BooleanField()

    action1_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
    )

    action2_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelect(),
        label="Which action do you choose?",
    )

    switcher = models.BooleanField()

    # beliefs
    green_red_r2 = models.IntegerField(min=0, max=100)
    a_or_b_r2 = models.IntegerField(min=0, max=100)