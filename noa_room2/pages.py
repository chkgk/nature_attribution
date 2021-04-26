from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['action2_b']

    def is_displayed(self):
        return not self.player.participant.vars.get('dropout', False)

    def before_next_page(self):
        self.player.participant.vars["action_b_r2"] = self.player.action2_b
        self.player.determine_switch()


class BeliefColor(Page):
    form_model = 'player'
    form_fields = ['green_red_r2']

    def before_next_page(self):
        self.player.participant.vars["green_red_r2"] = self.player.green_red_r2

    def is_displayed(self):
        return not self.player.participant.vars.get('dropout', False)


class BeliefOther(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r2']

    def before_next_page(self):
        self.player.participant.vars["a_or_b_r2"] = self.player.a_or_b_r2

    def is_displayed(self):
        return not self.player.participant.vars.get('dropout', False)


page_sequence = [
    Decision,
    BeliefColor,
    BeliefOther
]
