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
    form_fields = ['c1_coplayer', 'c2_probabilities', 'c3_decision_importance', 'c_attempts1']

    def vars_for_template(self):
        return {
            'c1_solution': Constants.comprehension_solutions['c1_coplayer'],
            'c2_solution': Constants.comprehension_solutions['c2_probabilities'],
            'c3_solution': Constants.comprehension_solutions['c3_decision_importance'],
        }


class Comprehension2(Page):
    template_name = 'noa_intro/Comprehension2.html'
    form_model = 'player'
    form_fields = ['c4_payoff_ab_red', 'c5_payoff_ab_green', 'c6_payoff_bb_green', 'c7_payoff_ba_green', 'c_attempts2']

    def vars_for_template(self):
        return {
            'c4_solution': Constants.comprehension_solutions['c4_payoff_ab_red'],
            'c5_solution': Constants.comprehension_solutions['c5_payoff_ab_green'],
            'c6_solution': Constants.comprehension_solutions['c6_payoff_bb_green'],
            'c7_solution': Constants.comprehension_solutions['c7_payoff_ba_green'],
        }

    def before_next_page(self):
        self.player.set_data()


class ComprehensionDropout(Page):
    def is_displayed(self):
        return self.player.c_attempts1 + self.player.c_attempts2 > Constants.max_quiz_attempts + 2

    def vars_for_template(self):
        return {
            'attempts': self.player.c_attempts1 + self.player.c_attempts2 - 2,
            'experimenter_name': self.session.config.get('experimenter_name', 'Christian Koenig'),
            'experimenter_email': self.session.config.get('experimenter_email', 'christian.koenig@uibk.ac.at'),
        }


page_sequence = [
    Introduction,
    Instructions,
    Comprehension1,
    Comprehension2,
    ComprehensionDropout
]
