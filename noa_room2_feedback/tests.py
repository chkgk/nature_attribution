from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):
    def play_round(self):
        if self.player.wtp_treatment and not self.player.wtp_round_1:
            yield pages.Results, {
                'wtp_payment': random.randint(0, 50) / 100,
                'wants_to_know': random.choice([True, False])
            }

            if self.player.wants_to_know:
                if self.player.wtp_payment >= self.player.info_price:
                    expect(self.player.info_bought, True)
                    expect(self.player.wtp_result, Constants.max_price - self.player.info_price)
                else:
                    expect(self.player.info_bought, False)
                    expect(self.player.wtp_result, Constants.max_price)
            else:
                expect(self.player.info_bought, False)
                expect(self.player.wtp_result, Constants.max_price)

            if self.player.wants_to_know:
                yield pages.WTPResults
        else:
            yield pages.Results

        if self.player.payment_room_1:
            expected_payoff = self.player.participant.vars['room_payoff_1']
        else:
            expected_payoff = self.player.participant.vars['room_payoff_2']

        expect(self.player.payoff, expected_payoff)