from rest_math_shared import *
from otree.api import *
import random
import string
c = cu

doc = ''
class C(BaseConstants, MathConstants):
    NAME_IN_URL = 'DeviceExG'
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

    ux_speed = models.IntegerField(
        label='The setup of the headset was quick.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    ux_ease = models.IntegerField(
        label='The setup of the headset was easy.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    ux_look = models.IntegerField(
        label='The headset looks good.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    wx_public = models.IntegerField(
        label='I would feel comfortable wearing this headset in public.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    wx_private = models.IntegerField(
        label='I would feel comfortable wearing this headset in private.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    wx_conversation = models.IntegerField(
        label='I would feel comfortable having a conversation while wearing this headset.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    wx_others = models.IntegerField(
        label='This headset would make other people uncomfortable.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

class UXWX_Survey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['ux_comfort', 'ux_speed', 'ux_ease', 'ux_look',
                       'wx_public', 'wx_private', 'wx_conversation', 'wx_others']
        random.shuffle(form_fields)
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 3

class Device(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

page_sequence = [Device,
                 RestEyesOpen, RestEyesClosed, TLX_Fat_Survey_Rest,
                 MathInstructions, MathTask, TLX_Fat_Survey_Math, BeforeTask,
                 UXWX_Survey]