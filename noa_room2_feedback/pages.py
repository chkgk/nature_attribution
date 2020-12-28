from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class GroupMatching(WaitPage):
    template_name = 'noa_room2_feedback/GroupingWaitPage.html'
    group_by_arrival_time = True

    def vars_for_template(self):
        # we abuse this function to set the time the participant first arrives on the waitpage.
        if not self.participant.vars.get('r2_start_wait', None):
            self.participant.vars['r2_start_wait'] = time.time()

        return dict()

    def after_all_players_arrive(self):
        if len(self.group.get_players()) == 1:
            return

        self.group.draw_ball()
        for player in self.group.get_players():
            player.set_partner_action()
            player.calculate_game_round_payoff()


class Results(Page):
    def is_displayed(self):
        return not self.player.dropped_out

    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action else 'A',
            'others_action': 'B' if self.player.other_b_r2 else 'A',
            'ball_color': 'green' if self.group.ball_green else 'red'
        }

    def before_next_page(self):
        self.player.set_room_payoff()


page_sequence = [
    GroupMatching,
    Results,
]
