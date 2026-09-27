from rest_math_shared import *
from otree.api import *
import random
import string
c = cu

doc = ''
class C(BaseConstants, MathConstants):
    NAME_IN_URL = 'Block1HomeStart'
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
    qual_work_activity = models.LongStringField(blank=True, label="What was the task, and what did doing it actually involve (e.g. writing, reading, meetings, coding, admin work)?")
    qual_work_env = models.LongStringField(blank=True, label="Where were you, what did the space look like, and what was it like to work there? For example, you might mention the room and lighting, noise level, temperature, how comfortable your seating was, whether anyone else was around, and anything that distracted you or helped you focus.")

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

class RecordingSetup(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {"token": player.participant.code}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class AudioSetup(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class WorkTask(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

class WorkSurvey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_work_activity', 'qual_work_env']
        return all_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

page_sequence = [RecordingInstructions,
                 AudioSetup, HeadphonesSetup, RecordingSetup,
                 RestEyesOpen, RestEyesClosed, TLX_Fat_Survey_Rest,
                 MathInstructions, MathTask, TLX_Fat_Survey_Math, BeforeTask,
                 WorkTask, WorkSurvey
                 ]