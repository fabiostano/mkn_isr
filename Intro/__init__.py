
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

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9']], widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9']], widget=widgets.RadioSelectHorizontal)

    # ----- REST ACTIONS ----- #
    rest_actions_eo = models.StringField(label="")
    rest_actions_ec = models.StringField(label="")

class Vorbereitung(Page):
    form_model = 'player'

class Welcome(Page):
    form_model = 'player'

class IntroQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'english', 'occupation', 'field_of_study', 'dominant_hand']

class StateQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['pleasure', 'arousal']

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

class RestEyesClosed(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']

page_sequence = [Vorbereitung, Welcome, IntroQuestionnaire, StateQuestionnaire, RestEyesOpen, RestEyesClosed]