from rest_math_shared import *
from otree.api import *
import random
import string
c = cu

doc = ''
class C(BaseConstants, MathConstants):
    NAME_IN_URL = 'Block2OutdoorStart'
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

    # ----- Qual. Fields ----- #
    qual_outdoor_activity = models.LongStringField(blank=True,
                                                label="How did you move during the 10-minute walk? For example, you might mention your walking pace, whether it was steady or varied, whether you stopped or paused at any point, and how physically demanding the walk felt.")
    qual_outdoor_env = models.LongStringField(blank=True,
                                           label="What was your environment like during this block — both while doing the recordings and while walking? For example, you might mention the setting, noise level, weather, how busy or quiet it was, whether anyone else was around.")

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

class OutdoorTask(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

class OutdoorSurvey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_outdoor_activity', 'qual_outdoor_env']
        return all_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3


page_sequence = [RecordingInstructions,
                 AudioSetup, HeadphonesSetup, RecordingSetup,
                 RestEyesOpen, RestEyesClosed, TLX_Fat_Survey_Rest,
                 MathInstructions, MathTask, TLX_Fat_Survey_Math, BeforeTask,
                 OutdoorTask, OutdoorSurvey
                 ]