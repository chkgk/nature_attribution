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
Outro / Survey app for the Nature of Attribution project
'''


class Constants(BaseConstants):
    name_in_url = 'noa_outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # set all variables on the player so that they are included in exports
            player.treatment = self.session.vars['treatment']
            player.wtp_treatment = self.session.vars['wtp_treatment']
            if self.session.vars['wtp_treatment']:
                player.wtp_round_1 = self.session.vars['wtp_round_1']
            player.payment_room_1 = player.participant.vars['payment_room_1']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # treatment indicators
    treatment = models.StringField()
    wtp_treatment = models.BooleanField(initial=False)
    wtp_round_1 = models.BooleanField(initial=True)

    # round payment indicator
    payment_room_1 = models.BooleanField()

    # survey
    age = models.IntegerField(
        label='What is your age?',
        min=18,
        max=120
    )

    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'I prefer not to tell'],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    education = models.IntegerField(
        choices=[
            (0, 'Less than high school degree'),
            (1, 'High school degree or equivalent (e.g. GED)'),
            (2, 'Some college, but no degree'),
            (3, 'Associate degree'),
            (4, 'Bachelor degree'),
            (5, 'Graduate degree')
        ],
        label='What is the highest level of school you have completed or the highest degree you have received?',
        widget=widgets.RadioSelect)

    major = models.StringField(
        label='If you had at least some college education, please tell us your major: ',
        blank=True
    )

    risk = models.FloatField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='How do you see yourself: Are you in general a person who takes risk (10) or do you try to avoid \
                    risks (0)? Please self-grade your choice (0-10).',
        widget=widgets.RadioSelectHorizontal()
    )

    comments = models.LongStringField(label="Do you have any comments about this study?", blank=True)

    c_attempts1 = models.IntegerField()
    c_attempts2 = models.IntegerField()

    action_b_r1 = models.BooleanField()
    other_b_r1 = models.BooleanField()
    ball_green_r1 = models.BooleanField()
    green_red_r1 = models.IntegerField(min=0, max=100)
    a_or_b_r1 = models.IntegerField(min=0, max=100)

    action_b_r2 = models.BooleanField()
    other_b_r2 = models.BooleanField()
    ball_green_r2 = models.BooleanField()
    green_red_r2 = models.IntegerField(min=0, max=100)
    a_or_b_r2 = models.IntegerField(min=0, max=100)

    switcher = models.BooleanField()

    def collect_data(self):
        self.c_attempts1 = self.participant.vars.get('c_attempts1', 0)
        self.c_attempts2 = self.participant.vars.get('c_attempts2', 0)

        self.action_b_r1 = self.participant.vars.get('action_b_r1', False)
        self.action_b_r2 = self.participant.vars.get('action_b_r2', False)

        self.other_b_r1 = self.participant.vars.get('other_b_r1', False)
        self.other_b_r2 = self.participant.vars.get('other_b_r2', False)

        self.ball_green_r1 = self.participant.vars.get('ball_green_1', False)
        self.ball_green_r2 = self.participant.vars.get('ball_green_2', False)

        self.a_or_b_r1 = self.participant.vars.get('a_or_b_r1', 0)
        self.a_or_b_r2 = self.participant.vars.get('a_or_b_r2', 0)

        self.green_red_r1 = self.participant.vars.get('green_red_r1', 0)
        self.green_red_r2 = self.participant.vars.get('green_red_r2', 0)

        self.switcher = self.participant.vars.get('switcher', False)