
from otree.api import *
import random
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    selected_playlist = models.StringField()

    # ----- DEMOGRAPHICS ----- #
    english = models.StringField(
        label='Please indicate the level of your English language proficiency.',
        choices=["A1 Beginner – I can understand and use familiar everyday expressions and very basic phrases.",
                 "A2 Elementary English – I can understand sentences and frequently used expressions related to areas of most immediate relevance.",
                 "B1 Intermediate English – I understand the main points of clear input on familiar matters regularly encountered in work, school, etc.",
                 "B2 Upper-Intermediate English – I understand the main ideas of complex text on concrete and abstract topics, incl. technical discussions, etc.",
                 "C1 Advanced English – I can understand a wide range of demanding, longer texts, and recognise implicit meaning.",
                 "C2 Proficient English – I can understand with ease virtually everything I hear or read."]
    )

    age = models.IntegerField(
        label='What is your age?'
    )

    gender = models.StringField(
        label='What is your gender?',
        choices=["Male", "Female", "Diverse", "Prefer not to say"]
    )

    occupation = models.StringField(
        label='What is your current occupation?',
        choices=["Apprentice", "Student", "Employee", "Self-Employed", "Unemployed", "Other"]
    )

    field_of_study = models.StringField(
        label='What is/was your field of study?',
        choices=['Natural Sciences (e.g. Mathematics, Computer Science)','Engineering and Technology (e.g. Civil Engineering, Mechanical Engineering)', 'Medial and Health Sciences (e.g. Medicine, Pharmacology)', 'Agricultural Science (e.g. Forestry, Veterinary Science)', 'Social Sciences (e.g. Economics, Educational Sciences)', 'Humanities (e.g. History, Languages)', 'Not Specified']
    )

    dominant_hand = models.StringField(
        label='What is your dominant hand?',
        choices=["Left", "Right", "Both"]
    )

    ### --- STATE Q --- ###
    # ----- Mental Readiness ----- #
    mr2 = models.IntegerField(label="How sleepy are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mr3 = models.IntegerField(label="How motivated are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Mental Fatigue ----- #
    mf1 = models.IntegerField(label="If I were to do something right now, I could keep my thoughts focused on it.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf2 = models.IntegerField(label="Right now, I could concentrate well.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf3 = models.IntegerField(label="Currently, it would take a lot of effort to concentrate on something.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf4 = models.IntegerField(label="My thoughts would easily wander off at the moment.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)


class Welcome(Page):
    form_model = 'player'

class IntroQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'english', 'occupation', 'field_of_study', 'dominant_hand', 'mr2', 'mr3']

class StateQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['pleasure', 'arousal', 'mf1', 'mf2', 'mf3', 'mf4']

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        sequence = player.participant.vars.get('selected_sequence', [])
        return sequence[0] if sequence else upcoming_apps[0]

def creating_session(subsession: Subsession):
    sequences = [
        ['HiddenProfile_Chat', 'mathChat', 'Outro'],
        ['mathChat', 'HiddenProfile_Chat', 'Outro'],
        ['HiddenProfile_Jitsi', 'mathJitsi', 'Outro'],
        ['mathJitsi', 'HiddenProfile_Jitsi', 'Outro'],
    ]

    for group in subsession.get_groups():
        selected_sequence = random.choice(sequences)
        for p in group.get_players():
            p.participant.vars['selected_sequence'] = selected_sequence

page_sequence = [Welcome, IntroQuestionnaire, StateQuestionnaire]