from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class GroupMatching(WaitPage):
    template_name = 'noa_room1_feedback/GroupingWaitPage.html'
    group_by_arrival_time = True

    def vars_for_template(self):
        # we abuse this function to set the time the participant first arrives on the waitpage.
        if not self.participant.vars.get('r1_start_wait', None):
            self.participant.vars['r1_start_wait'] = time.time()

        return dict()

    def after_all_players_arrive(self):
        if len(self.group.get_players()) == 1:
            return

        self.group.draw_ball()
        for player in self.group.get_players():
            player.set_partner_action()
            player.calculate_game_round_payoff()


class Results(Page):
    form_model = 'player'

    def is_displayed(self):
        return not self.player.dropped_out

    def get_form_fields(self):
        return ['wtp_payment'] if self.player.wtp_treatment else []

    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action else 'A',
            'others_action': 'B' if self.player.other_b_r1 else 'A',
            'ball_color': 'green' if self.group.ball_green else 'red'
        }

    def before_next_page(self):
        if self.player.wtp_treatment:
            self.player.bdm_mechanism()

        self.player.set_room_payoff()


class WTPResults(Page):
    def is_displayed(self):
        return self.player.wtp_treatment and not self.player.dropped_out

    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action else 'A',
            'others_action': 'B' if self.player.other_b_r1 else 'A',
            'ball_color': 'green' if self.group.ball_green else 'red',
            'room_payoff': self.player.participant.vars['room_payoff_1']
        }


page_sequence = [
    GroupMatching,
    Results,
    WTPResults
]
