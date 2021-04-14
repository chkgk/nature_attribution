from ._builtin import Page
from otree.api import Currency as c


class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'major', 'risk']

    def is_displayed(self):
        return not self.participant.vars.get('dropout', False)

    def error_message(self, values):
        if values['education'] >= 2 and not values['major'].strip():
            return 'Please indicate your major.'


class LastPage(Page):
    def vars_for_template(self):
        return {
            'payment_room': '1' if self.player.participant.vars.get('payment_room_1', None) else '2',
            'payment': self.player.participant.vars.get('payment', c(0)),
            'info_bought': self.player.participant.vars.get('info_bought', False),
            'info_price': self.player.participant.vars.get('info_price', c(0)),
            'wtp_bonus': self.player.participant.vars.get('wtp_bonus', c(0.5)),
            'experimenter_name': self.session.config.get('experimenter_name', 'Christian Koenig'),
            'experimenter_email': self.session.config.get('experimenter_email', 'christian.koenig@uibk.ac.at'),
            'dropout': self.participant.vars.get('dropout', False)
        }


page_sequence = [
    Survey,
    LastPage
]
