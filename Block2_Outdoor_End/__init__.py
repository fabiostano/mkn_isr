from rest_math_shared import *
from otree.api import *
import random
import string
c = cu

doc = ''
class C(BaseConstants, MathConstants):
    NAME_IN_URL = 'Block2OutdoorEnd'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2+2

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def creating_session(subsession):
    pass

class Player(BasePlayer):
    locals().update(rest_fields())
    locals().update(math_fields())
    locals().update(tlx_fat_fields())

    # ----- UX/WX Questions -----
    ux_comfort = models.IntegerField(
        label='The headset is comfortable.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

class RecordingInstructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class HeadphonesSetup(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class AudioSetup(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class RecordingSetup(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {"token": player.participant.code}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class RecordingStop(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

class UXSurvey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['ux_comfort']
        random.shuffle(form_fields)
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

class Block2End(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

page_sequence = [RecordingInstructions,
                 # HeadphonesSetup,
                 AudioSetup, RecordingSetup,
                 RestEyesOpen, RestEyesClosed, TLX_Fat_Survey_Rest,
                 MathInstructions, MathTask, TLX_Fat_Survey_Math, BeforeTask,
                 UXSurvey, RecordingStop, Block2End]