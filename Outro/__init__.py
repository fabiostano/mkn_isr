
from otree.api import *
from otree.api import models, widgets

c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ### --- TRAIT Q --- ###

    # ----- Task Attitudes ----- #
    ta1 = models.IntegerField(label="How much do you like performing mental arithmetic?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    ta2 = models.IntegerField(label="How much do you like decision making tasks?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)

    # ----- Flow Disposition Work ----- #
    fpw1 = models.IntegerField(label="... you feel bored?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw2 = models.IntegerField(label="... it feels as if your ability to perform what you do completely matches how difficult it is?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw3 = models.IntegerField(label="... you have a clear picture of what you want to achieve, and what you need to do to get there?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw4 = models.IntegerField(label="... you are conscious of how well or poorly you perform what you are doing?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw5 = models.IntegerField(label="... you feel completely concentrated?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw6 = models.IntegerField(label="... you have a sense of complete control?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpw7 = models.IntegerField(label="... what you do feels extremely enjoyable to do?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)

    # ----- Flow Disposition Household ----- #
    fph1 = models.IntegerField(label="... you feel bored?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph2 = models.IntegerField(label="... it feels as if your ability to perform what you do completely matches how difficult it is?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph3 = models.IntegerField(label="... you have a clear picture of what you want to achieve, and what you need to do to get there?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph4 = models.IntegerField(label="... you are conscious of how well or poorly you perform what you are doing?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph5 = models.IntegerField(label="... you feel completely concentrated?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph6 = models.IntegerField(label="... you have a sense of complete control?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fph7 = models.IntegerField(label="... what you do feels extremely enjoyable to do?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)

    # ----- Flow Disposition Leisure ----- #
    fpl1 = models.IntegerField(label="... you feel bored?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl2 = models.IntegerField(label="... it feels as if your ability to perform what you do completely matches how difficult it is?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl3 = models.IntegerField(label="... you have a clear picture of what you want to achieve, and what you need to do to get there?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl4 = models.IntegerField(label="... you are conscious of how well or poorly you perform what you are doing?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl5 = models.IntegerField(label="... you feel completely concentrated?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl6 = models.IntegerField(label="... you have a sense of complete control?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    fpl7 = models.IntegerField(label="... what you do feels extremely enjoyable to do?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)

    # ----- Recognition ----- #
    rec_lightcoral = models.IntegerField(label='Before the study, how well did you know the player labeled lightcoral?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
                                     widget=widgets.RadioSelectHorizontal)
    rec_lightgreen = models.IntegerField(label='Before the study, how well did you know the player labeled lightgreen?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
                                     widget=widgets.RadioSelectHorizontal)
    rec_lightblue = models.IntegerField(label='Before the study, how well did you know the player labeled lightblue?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
                                     widget=widgets.RadioSelectHorizontal)

def creating_session(subsession: Subsession):
    for p in subsession.get_players():
         p.color = C.COLORMAP[p.id_in_group - 1]

class ThankYou(Page):
    form_model = 'player'

class Goodbye(Page):
    form_model = 'player'

class TraitQuestionnaire(Page):
    form_model = 'player'

    def vars_for_template(player):
        return dict(my_color=player.color)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        task_fields = ['ta1', 'ta2']
        random.shuffle(task_fields)
        all_fields=task_fields

        proneness_work_fields = ['fpw1', 'fpw2', 'fpw3', 'fpw4', 'fpw5', 'fpw6', 'fpw7']
        all_fields += proneness_work_fields

        proneness_household_fields = ['fph1', 'fph2', 'fph3', 'fph4', 'fph5', 'fph6', 'fph7']
        all_fields += proneness_household_fields

        proneness_leisure_fields = ['fpl1', 'fpl2', 'fpl3', 'fpl4', 'fpl5', 'fpl6', 'fpl7']
        all_fields += proneness_leisure_fields

        recognition_fields = ['rec_lightcoral', 'rec_lightgreen', 'rec_lightblue']
        all_fields += recognition_fields

        return all_fields

page_sequence = [TraitQuestionnaire, ThankYou, Goodbye]