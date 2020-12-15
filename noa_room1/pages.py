from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class TreatmentSelection(Page):
    form_model = 'group'
    form_fields = ['debug_treatment']

    def is_displayed(self):
        return self.is_debug and self.player.id_in_subsession == 1 and not self.player.participant.vars.get('vars_set', True)

    def before_next_page(self):
        self.subsession.set_treatment_vars(self.group.debug_treatment)


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
    TreatmentSelection,
    ActionPreference,
    Decision,
    DecisionAssignment,
    BeliefColor,
    BeliefOther
]
