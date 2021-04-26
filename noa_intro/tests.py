from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):
    def play_round(self):
        c_attempts1 = random.randint(1, 3)
        c_attempts2 = random.randint(1, 3)

        yield pages.Introduction
        yield pages.Instructions
        yield Submission(pages.Comprehension1, {
            'c1_coplayer': Constants.comprehension_solutions['c1_coplayer'],
            'c2_probabilities': Constants.comprehension_solutions['c2_probabilities'],
            'c3_decision_importance': Constants.comprehension_solutions['c3_decision_importance'],
            'c_attempts1': c_attempts1
        }, check_html=False)
        yield Submission(pages.Comprehension2, {
            'c4_payoff_ab_red': Constants.comprehension_solutions['c4_payoff_ab_red'],
            'c5_payoff_ab_green': Constants.comprehension_solutions['c5_payoff_ab_green'],
            'c6_payoff_bb_green': Constants.comprehension_solutions['c6_payoff_bb_green'],
            'c7_payoff_ba_green': Constants.comprehension_solutions['c7_payoff_ba_green'],
            'c_attempts2': c_attempts2
        }, check_html=False)

        if c_attempts1 + c_attempts2 > 5:
            yield Submission(pages.ComprehensionDropout, check_html=False)
