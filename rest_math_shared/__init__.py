from _shared.rest_math_fields import *
from otree.api import *
c = cu
doc = ''

class C(BaseConstants, MathConstants):
    name_in_url = 'Rest_Math_Shared'

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    locals().update(rest_fields())
    locals().update(math_fields())
    locals().update(tlx_fat_fields())

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class RestEyesClosed(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class TLX_Fat_Survey_Rest(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['tlx_single', 'mr_mood', 'mr_sleepy', 'mr_motivy', 'mf_single']
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class MathInstructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class MathTask(Page):
    form_model = 'player'
    form_fields = ['math_actions']

    @staticmethod
    def vars_for_template(player: Player):
        difficulty_level = MathConstants.math_levels[player.round_number-1]

        return {"round_duration_ms": MathConstants.task_duration_ms,
                "trial_duration_ms": MathConstants.trial_duration_ms,
                "difficulty_level": difficulty_level}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= 2

class BeforeTask(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {"round_number": player.round_number-1}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number < 2

class TLX_Fat_Survey_Math(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['tlx_single',
                       'mr_mood', 'mr_sleepy', 'mr_motivy', 'mf_single']
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        if player.round_number <= 2: return True

page_sequence = [RestEyesOpen, RestEyesClosed, TLX_Fat_Survey_Rest,
                 MathInstructions,
                 MathTask,
                 TLX_Fat_Survey_Math, BeforeTask]