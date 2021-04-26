from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Decision, {
            'action2_b': random.choice([True, False])
        }
        yield pages.BeliefColor, {
            'green_red_r2': random.randint(0, 100)
        }
        yield pages.BeliefOther, {
            'a_or_b_r2': random.randint(0, 100)
        }
