from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ActionPreference(Page):
    form_model = 'player'
    form_fields = ["prefers_b"]

    def is_displayed(self):
        return self.player.aa_treatment


class Decision(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['action1_b'] if self.player.ra_treatment else []

    def before_next_page(self):
        if self.player.aa_treatment:
            self.player.action1_b = True
        self.player.participant.vars["action1_b"] = self.player.action1_b


class DecisionAssignment(Page):
    def is_displayed(self):
        return self.player.aa_treatment


class BeliefColor(Page):
    form_model = 'player'
    form_fields = ['green_red_r1']


class BeliefOther(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r1']


page_sequence = [
    ActionPreference,
    Decision,
    DecisionAssignment,
    BeliefColor,
    BeliefOther
]
