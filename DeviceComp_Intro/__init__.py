from otree.api import *
import random
import string
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'DeviceCompIntro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    custom_group_id = models.StringField(blank=True)

def random_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def creating_session(subsession):
    for group in subsession.get_groups():
        group.custom_group_id = random_code()

class Player(BasePlayer):
    token = models.StringField(
        label='Please enter your study token here:'
    )

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

    # ------ Extended User Characteristics ------

    glasses = models.StringField(
        label='Are you wearing glasses right now?',
        choices=["Yes", "No"]
    )

    headsize = models.StringField(
        label="What is your head's size?",
        choices=["Small", "Medium", "Large"]
    )

    # Actually top & ears should be described separately: That is what I need most!
    # https://www.hair.com/hair-length-chart.html
    # https://therighthairstyles.com/hair-length-chart/
    hair_style_top = models.StringField(
        label="",  # 'How long is your hair on the top of your head?',
        choices=["(Almost) No Hair (0-1cm)",
                 "Very Short (1-10cm)",
                 "Short (Ear or Chin Length)",
                 "Medium (Shoulder or Armpit Length)",
                 "Long (Mid-back or Tailbone Length)"]
    )

    hair_style_ears = models.StringField(
        label="",  # 'How long is your hair close to your ears?',
        choices=["Short (0-5mm)", "Medium (5-10mm)", "Long (>10mm)"]
    )

    # Following the articles describing hair types
    # https://www.healthline.com/health/beauty-skin-care/types-of-hair#style-and-care
    # https://www.healthline.com/health/beauty-skin-care/types-of-hair#hair-types
    # http://projects.i-ctm.eu/it/progetto/figaro-1k
    # TODO: Could add pictograms here
    hair_type = models.StringField(
        label="",  # 'Which of these categories describes your hair type best?',
        choices=["Straight", "Wavy", "Curly", "Coily", "Braided", "Dreadlocks"]
    )

    # https://www.livingproof.com/hair-101/hair-density.html
    # TODO: Could add pictograms here
    hair_density = models.StringField(
        label="What is your hair's density?",
        choices=["Low (Fine Hair)", "Medium", "High (Dense/Thick Hair)"]
    )

    # TODO: Could add pictograms here
    beard_style = models.StringField(
        label='How long is your beard next to your ears?',
        choices=["No Beard (0mm)", "Light Stubble (0-5mm)", "Medium Stubble (5-10mm)", "Full Beard (>10mm)"]
    )

    # Main question - http://dx.doi.org/10.4236/jcdsa.2014.42012
    skin_oily_dry_1 = models.StringField(
        label='You would characterize your facial skin as:',
        choices=["Dry", "Normal", "Oily"]
    )

    # Added as a more common question - http://dx.doi.org/10.4236/jcdsa.2014.42012
    skin_oily_dry_2 = models.StringField(
        label='How often does your face appear shiny in photos?',
        choices=["Never, or you’ve never noticed shine", "Sometimes", "Frequently", "Always"]
    )

    # https://drive.google.com/file/d/16aKIh4P8atG0iOzCd3yMa0mXMW3nvg8o/view
    skin_resistant_sensitive_1 = models.StringField(
        label='Skin care products (including cleansers, moisturizers, toners, sunscreens, perfume, makeup...) cause your face to break out, get a rash, itch, or sting.',
        choices=["Never", "Rarely", "Often", "Always", "I don’t wear products on my face"]
    )

    # https://drive.google.com/file/d/16aKIh4P8atG0iOzCd3yMa0mXMW3nvg8o/view
    skin_resistant_sensitive_2 = models.StringField(
        label='How often does your face appear red in photos?',
        choices=["Never, or I never noticed it", "Sometimes", "Frequently", "Always"]
    )

class DevicesOverview(Page):
    form_model = 'player'

class UserCharacteristics(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        dem_fields = ['age', 'gender', 'dominant_hand', 'glasses', 'english', 'occupation',
                      'headsize', 'hair_style_top', 'hair_style_ears', 'hair_type', 'hair_density', 'beard_style',
                      'skin_oily_dry_1', 'skin_oily_dry_2', 'skin_resistant_sensitive_1', 'skin_resistant_sensitive_2']

        form_fields = dem_fields
        return form_fields

class ID(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        setup_fields = ['token'] # , 'booth'
        return setup_fields

class JitsiInit(Page):
    form_model = 'player'

    def vars_for_template(player):
        return dict(
            id = player.id_in_group,
            color=player.id_in_group,
            room_id=player.group.id
        )

page_sequence = [# ID,
                 JitsiInit,
                 UserCharacteristics,
                 DevicesOverview
                 ]