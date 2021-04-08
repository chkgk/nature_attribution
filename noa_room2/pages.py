from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['action2_b']

    def before_next_page(self):
        self.player.participant.vars["action2_b"] = self.player.action2_b


class BeliefColor(Page):
    form_model = 'player'
    form_fields = ['green_red_r2']


class BeliefOther(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r2']


page_sequence = [
    Decision,
   # BeliefColor,
   # BeliefOther
]
