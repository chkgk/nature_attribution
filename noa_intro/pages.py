from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Instructions(Page):
    pass


class Comprehension1(Page):
    template_name = 'noa_intro/Comprehension1.html'
    form_model = 'player'
    form_fields = ['c1_coplayer', 'c2_probabilities', 'c3_decision_importance']

    def vars_for_template(self):
        return {
            'page': 1,
            'c1_ok': False,
            'c2_ok': False,
            'c3_ok': False,
        }

class ComprehensionCheck1(Page):
    template_name = 'noa_intro/Comprehension1.html'
    form_model = 'player'
    form_fields = ['c1_coplayer', 'c2_probabilities', 'c3_decision_importance']

    def vars_for_template(self):
        return {
            'page': 2,
            'c1_ok': self.player.c1_coplayer == Constants.comprehension_solutions['c1_coplayer'],
            'c2_ok': self.player.c2_probabilities == Constants.comprehension_solutions['c2_probabilities'],
            'c3_ok': self.player.c3_decision_importance == Constants.comprehension_solutions['c3_decision_importance'],
        }

    def error_message(self, values):
        if values['c1_coplayer'] != Constants.comprehension_solutions['c1_coplayer'] or \
           values['c2_probabilities'] != Constants.comprehension_solutions['c2_probabilities'] or \
           values['c3_decision_importance'] != Constants.comprehension_solutions['c3_decision_importance']:
            return 'Please check your answers again!'

class Comprehension2(Page):
    template_name = 'noa_intro/Comprehension2.html'
    form_model = 'player'
    form_fields = ['c4_payoff_ab_red', 'c5_payoff_ab_green', 'c6_payoff_bb_green', 'c7_payoff_ba_green']

    def vars_for_template(self):
        return {
            'page': 1,
            'c4_ok': False,
            'c5_ok': False,
            'c6_ok': False,
            'c7_ok': False,
        }


class ComprehensionCheck2(Page):
    template_name = 'noa_intro/Comprehension2.html'
    form_model = 'player'
    form_fields = ['c4_payoff_ab_red', 'c5_payoff_ab_green', 'c6_payoff_bb_green', 'c7_payoff_ba_green']

    def vars_for_template(self):
        return {
            'page': 2,
            'c4_ok': self.player.c4_payoff_ab_red == Constants.comprehension_solutions["c4_payoff_ab_red"],
            'c5_ok': self.player.c5_payoff_ab_green == Constants.comprehension_solutions["c5_payoff_ab_green"],
            'c6_ok': self.player.c6_payoff_bb_green == Constants.comprehension_solutions["c6_payoff_bb_green"],
            'c7_ok': self.player.c7_payoff_ba_green == Constants.comprehension_solutions["c7_payoff_ba_green"],
        }

    def error_message(self, values):
        if values["c4_payoff_ab_red"] != Constants.comprehension_solutions["c4_payoff_ab_red"] or \
           values["c5_payoff_ab_green"] != Constants.comprehension_solutions["c5_payoff_ab_green"] or \
           values["c6_payoff_bb_green"] != Constants.comprehension_solutions["c6_payoff_bb_green"] or \
           values["c7_payoff_ba_green"] != Constants.comprehension_solutions["c7_payoff_ba_green"]:
            return "Please check your answers again!"


page_sequence = [
    Introduction,
    Instructions,
    Comprehension1,
    ComprehensionCheck1,
    Comprehension2,
    ComprehensionCheck2
]
