from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Survey, {
            'age': random.randint(18, 100),
            'gender': random.choice(['Male', 'Female', 'Other', 'I prefer not to tell']),
            'education': random.randint(0,5),
            'major': 'bla',
            'risk': random.randint(0, 10),
            'comments': 'None'
        }
        yield pages.LastPage