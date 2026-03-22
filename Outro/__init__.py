
from otree.api import *
from otree.api import models, widgets
import random

c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    color = models.StringField()
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
                                     widget=widgets.RadioSelectHorizontal, blank=True)
    rec_lightgreen = models.IntegerField(label='Before the study, how well did you know the player labeled lightgreen?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
                                     widget=widgets.RadioSelectHorizontal, blank=True)
    rec_lightblue = models.IntegerField(label='Before the study, how well did you know the player labeled lightblue?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
                                     widget=widgets.RadioSelectHorizontal, blank=True)

    # ----- Qual. Fields ----- #
    # Individual Flow
    qual_indiv_q1_general = models.LongStringField(blank=True, label="When working on the tasks, did you experience flow more strongly in the chat or video meeting setting, if at all?<br>If so, please describe what made either setting more or less conducive to flow for you.")
    qual_indiv_q2_moment = models.LongStringField(blank=True, label="Can you describe a moment or aspect of the task where you particularly noticed being more (or less) “in flow” in either the chat or video meeting setting?")
    qual_indiv_q3_task = models.LongStringField(blank=True, label="Did characteristics of the task (e.g., task type, structure, or difficulty) influence your flow experience in chat versus video meetings?<br>If yes, how? Please explain.")
    # qual_indiv_q4_medium = models.LongStringField(blank=True, label="Did the communication setting (chat vs. video meeting) influence your flow experience? If yes, how? Please explain.")
    qual_indiv_q4_functional = models.LongStringField(blank=True, label="Do you think the chat and video meeting shaped communication (e.g., how easy or effective it was) differently in a way that impacted your flow? If yes, how? Please explain.")
    qual_indiv_q4_motivational = models.LongStringField(blank=True,label="Do you think the chat and video meeting shaped your mood, stress, or motivation differently in a way that impacted your flow?<br>If yes, how? Please explain.")
    qual_indiv_q5_mst_velocity = models.LongStringField(blank=True, label="... how quickly you received responses from your team members?")
    qual_indiv_q5_mst_parallel = models.LongStringField(blank=True, label="... whether multiple messages or exchanges could occur at the same time?")
    qual_indiv_q5_mst_symbols = models.LongStringField(blank=True, label="... how easily tone, emphasis, or subtle meaning could be expressed in communication?")
    qual_indiv_q5_mst_rehearse = models.LongStringField(blank=True, label="... how you could think about and change what you wanted to say before sending it?")
    qual_indiv_q5_mst_reprocess = models.LongStringField(blank=True, label="... whether you could go back and review earlier messages or information from your team members?")

    # Reciprocal Flow
    qual_recip_q1_general = models.LongStringField(blank=True, label="When working on the tasks, did your team members influence your flow? If yes, please describe how and why.")
    qual_recip_q2_moment = models.LongStringField(blank=True, label="Was there a difference in how team members influenced your flow in the chat or video meeting setting? If yes, how? Please explain.")
    # qual_recip_q2_moment = models.LongStringField(blank=True, label="Can you describe a moment during the task when the interaction with your team members especially helped or disrupted your experience of being “in flow” in the chat or video meeting settings?")
    qual_recip_q3_task = models.LongStringField(blank=True, label="Did characteristics of the task (e.g., task type, structure, or difficulty) influence how your team members affected your flow experience in chat versus video meetings? If yes, how? Please explain.")
    qual_recip_q4_medium = models.LongStringField(blank=True, label="Did characteristics of the communication setting (chat vs. video meeting) influence how your team members affected your flow experience? If yes, how? Please explain.")
    qual_recip_q5_mst_velocity = models.LongStringField(blank=True, label="... how quickly you received responses from your team members?")
    qual_recip_q5_mst_parallel = models.LongStringField(blank=True, label="... whether multiple messages or exchanges could occur at the same time?")
    qual_recip_q5_mst_symbols = models.LongStringField(blank=True, label="... how easily tone, emphasis, or subtle meaning could be expressed in communication?")
    qual_recip_q5_mst_rehearse = models.LongStringField(blank=True, label="... how you could think about and change what you wanted to say before sending it?")
    qual_recip_q5_mst_reprocess = models.LongStringField(blank=True, label="... whether you could go back and review earlier messages or information from your team members?")

def creating_session(subsession: Subsession):
    for group in subsession.get_groups():
        for p in group.get_players():
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

class Qual_Intro(Page):
    form_model = 'player'

class Qual_Individual_General(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_indiv_q1_general', 'qual_indiv_q2_moment']
        return all_fields

class Qual_Individual_Specific(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_indiv_q3_task', 'qual_indiv_q4_functional', 'qual_indiv_q4_motivational',
                      'qual_indiv_q5_mst_velocity', 'qual_indiv_q5_mst_parallel', 'qual_indiv_q5_mst_symbols', 'qual_indiv_q5_mst_rehearse', 'qual_indiv_q5_mst_reprocess']
        return all_fields

class Qual_Reciproc_General(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_recip_q1_general', 'qual_recip_q2_moment']
        return all_fields

class Qual_Reciproc_Specific(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        all_fields = ['qual_recip_q3_task', 'qual_recip_q4_medium',
                      'qual_recip_q5_mst_velocity', 'qual_recip_q5_mst_parallel', 'qual_recip_q5_mst_symbols', 'qual_recip_q5_mst_rehearse', 'qual_recip_q5_mst_reprocess']
        return all_fields

page_sequence = [TraitQuestionnaire, # Qual_Intro,
                 Qual_Individual_General, Qual_Individual_Specific,
                 Qual_Reciproc_General, # Qual_Reciproc_Specific,
                 ThankYou, Goodbye]