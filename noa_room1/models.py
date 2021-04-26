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
Room 1 App for Nature of Attribution
'''


class Constants(BaseConstants):
    name_in_url = 'noa_room1'
    players_per_group = None
    num_rounds = 1


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

        for player in self.get_players():
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
    # treatment 
    treatment = models.StringField()
    wtp_treatment = models.BooleanField(initial=False)
    wtp_round_1 = models.BooleanField(initial=True)

    # round payment indicator
    payment_room_1 = models.BooleanField()

    prefers_b = models.BooleanField(
        choices=[(False, 'Action A'), (True, 'Action B')],
        label='A final question, for which there is no right or wrong answer: Which action would you choose?',
        widget=widgets.RadioSelect)

    action1_b = models.BooleanField(
        choices=[(False, 'A'), (True, 'B')],
        widget=widgets.RadioSelect(),
        label='Which action do you choose?')

    # beliefs
    green_red_r1 = models.IntegerField(min=0, max=100)
    a_or_b_r1 = models.IntegerField(min=0, max=100)
