from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['action1_b']

    def before_next_page(self):
        self.player.participant.vars["action_b_r1"] = self.player.action1_b


class BeliefColor(Page):
    form_model = 'player'
    form_fields = ['green_red_r1']

    def before_next_page(self):
        self.player.participant.vars["green_red_r1"] = self.player.green_red_r1


class BeliefOther(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r1']

    def before_next_page(self):
        self.player.participant.vars["a_or_b_r1"] = self.player.a_or_b_r1


page_sequence = [
    Decision,
    BeliefColor,
    BeliefOther
]
