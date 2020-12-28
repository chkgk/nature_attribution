from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class TreatmentSelection(Page):
    form_model = 'group'
    form_fields = ['debug_treatment']

    def is_displayed(self):
        return self.is_debug and self.player.id_in_subsession == 1 and not self.player.participant.vars.get('vars_set', False)

    def before_next_page(self):
        self.subsession.set_treatment_vars(self.group.debug_treatment)


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
    TreatmentSelection,
    Decision,
    BeliefColor,
    BeliefOther
]
