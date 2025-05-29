
from otree.api import *
from otree.api import models, widgets

c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(blank=True)
    IBAN = models.StringField(blank=True)
    BIC = models.StringField(blank=True)

    ### --- TRAIT Q --- ###

    # ----- Task Attitudes ----- #
    ta1 = models.IntegerField(label="How much do you like performing mental arithmetic?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    ta2 = models.IntegerField(label="How much do you like writing?",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                widget=widgets.RadioSelectHorizontal)
    ta3 = models.IntegerField(label="To what extent do you prefer writing over mental arithmetic?",
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

    # ----- Familiarity ----- #

    familiarity = models.IntegerField(label='Before the study, how familiar were you with the people in your group?',
                                     choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                     widget=widgets.RadioSelectHorizontal)

    familiar_members = models.IntegerField(label='How many of your group members did you know before the study?',
                                           choices=[[0, '0'], [1, '1'], [2, '2']])

    # ----- SDFS-2 ----- #
    sdfs1 = models.IntegerField(label="I feel I am competent enough to meet the demands of the situation",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs2 = models.IntegerField(label="I do things spontaneously and automatically without having to think.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs3 = models.IntegerField(label="I have a strong sense of what I want to do.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs4 = models.IntegerField(
        label="I have a good idea about how well I am doing while I am involved in the task/activity.",
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs5 = models.IntegerField(label="I am completely focused on the task at hand.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs6 = models.IntegerField(label="I have a feeling of total control over what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs7 = models.IntegerField(label="I am not worried about what others may be thinking of me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs8 = models.IntegerField(label="The way time passes seems to be different from normal.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs9 = models.IntegerField(label="I find the experience extremely rewarding.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    ac_sdfs = models.IntegerField(
        label='This is an attention check. Please select the answer on the far right.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], widget=widgets.RadioSelectHorizontal)

    # ----- Extraversion ----- #
    e1 = models.IntegerField(
        label='... is reserved.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e2 = models.IntegerField(
        label='... is talkative.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e3 = models.IntegerField(
        label='... generates a lot of enthusiasm.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e4 = models.IntegerField(
        label='... is outgoing/sociable.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e5 = models.IntegerField(
        label='... is sometimes shy/inhibited.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ------ Domain Expertise ------ #
    domain_exp_transcription = models.IntegerField(
        label="I am experienced in transcribing snippets of text.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_typing = models.IntegerField(
        label="I am a fast typer.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_research = models.IntegerField(
        label="I am experienced in reading and working with scientific papers.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_reading = models.IntegerField(
        label="I generally like reading papers or articles.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Mind Wandering Trait ----- #
    mwt01 = models.IntegerField(label="I find my thoughts wandering spontaneously.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt02 = models.IntegerField(label="My thoughts tend to be pulled from topic to topic.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt03 = models.IntegerField(label="I mind wander even when I’m supposed to be doing something else.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt04 = models.IntegerField(label="I have difficulty controlling my thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt05 = models.IntegerField(label="I find it hard to switch my thoughts off.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt06 = models.IntegerField(label="My thoughts are disorganized and `all over the place'.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt07 = models.IntegerField(label="I find it difficult to think about one thing without another thought entering my mind.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt08 = models.IntegerField(label="I find my thoughts are distracting and prevent me from focusing on what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt09 = models.IntegerField(label="I have difficulty slowing my thoughts down and focusing on one thing at a time.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt10 = models.IntegerField(label="I find myself flitting back and forth between different thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    ### --- MUSIC AT WORK TYPE --- ###

    from otree.api import models, widgets

    def make_likert_field(label, widget=widgets.RadioSelectHorizontal):
        return models.IntegerField(
            label=label,
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
            widget=widget,
        )

    # ----- General ----- #
    mt_g_01 = make_likert_field("I sometimes listen to music while working.")
    mt_g_02 = make_likert_field("I think music can help me to achieve more in certain tasks.")
    mt_g_03 = make_likert_field("Listening to music at work improves my overall long-term productivity.")
    mt_g_04 = make_likert_field("Listening to music at work improves my overall long-term emotional well-being.")

    # ----- Reason ----- #
    mt_r_01 = make_likert_field("... because it helps me to get into the flow state.")
    mt_r_02 = make_likert_field("... because it helps me to stay in the flow state.")
    mt_r_03 = make_likert_field("... because it helps me to experience more intense flow states.")
    mt_r_04 = make_likert_field("... because it helps me to block off potential distractions from the outside.")
    mt_r_05 = make_likert_field("... because it keeps unwanted inner thoughts away.")
    mt_r_06 = make_likert_field("... because it motivates me to get started with my work.")
    mt_r_07 = make_likert_field("... because it motivates me to keep going with my work.")
    mt_r_08 = make_likert_field("... because it makes work more enjoyable.")
    mt_r_09 = make_likert_field("... to boost my creativity.")
    mt_r_10 = make_likert_field("... because it boosts my energy.")
    mt_r_11 = make_likert_field("... to improve my mood.")
    mt_r_12 = make_likert_field("... because it calms me down.")
    mt_r_13 = make_likert_field("... because it inspires me.")
    mt_r_14 = make_likert_field("... to make boring tasks less boring.")
    mt_r_15 = make_likert_field("... because it creates a personal bubble in shared spaces.")
    mt_r_16 = make_likert_field("... because it helps me to complete tasks faster.")
    mt_r_17 = make_likert_field("... because it helps me maintain a high level of accuracy in my work.")
    mt_r_18 = make_likert_field("... because it helps me manage my workload better.")
    mt_r_19 = make_likert_field("... because it helps me to stay on track and avoid procrastination.")
    mt_r_20 = make_likert_field("... because it helps me feel more connected to my work.")

    # ----- Source ----- #
    mt_s_01 = make_likert_field("I use curated playlists or algorithms to listen to music at work.")
    mt_s_02 = make_likert_field("I create my own playlists which I listen to at work.")
    mt_s_03 = make_likert_field("I listen to the radio or similar live curated formats at work.")

    # ----- Work Tasks ----- #
    mt_w_01 = make_likert_field("... tasks that are rather easy for me.")
    mt_w_02 = make_likert_field("... tasks that are rather hard for me.")
    mt_w_03 = make_likert_field("... routine tasks.")
    mt_w_04 = make_likert_field("... tasks that are new to me.")
    mt_w_05 = make_likert_field("... repetitive tasks that require minimal focus.")
    mt_w_06 = make_likert_field("... tasks that require deep focus or high accuracy.")
    mt_w_07 = make_likert_field("... creative tasks (e.g. drafting new ideas).")
    mt_w_08 = make_likert_field("... graphical tasks (e.g. coming up with visualizations).")
    mt_w_09 = make_likert_field("... tasks that require lots of analytical thinking (e.g. programming).")
    mt_w_10 = make_likert_field("... tasks that require demanding writing and reading (e.g. academic work).")
    mt_w_11 = make_likert_field("... tasks that require easy writing and reading (e.g. handling e-mails).")
    mt_wd = make_likert_field("I listen to different types of music for different tasks.")

    # ----- Temporal ----- #
    mt_t_01 = make_likert_field("I need a constant level of background music while working.")
    mt_t_02 = make_likert_field(
        "I only use background music for certain selected periods and then turn it off again.")
    mt_t_03 = make_likert_field("I find myself listening to music at work more often during the morning.")
    mt_t_04 = make_likert_field("I find myself listening to music at work more often during the afternoon.")
    mt_t_05 = make_likert_field("I find myself listening to music at work more often during the evening.")
    mt_t_06 = make_likert_field("I find myself listening to music at work more often during the night.")
    mt_td = make_likert_field("I listen to different types of music for different times of day.")

    # ----- Environment ----- #
    mt_e_01 = make_likert_field("I like to use background music when working at home.")
    mt_e_02 = make_likert_field("I like to use background music when working in the office.")
    mt_e_03 = make_likert_field(
        "I like to use background music when working in co-working spaces or public libraries.")
    mt_e_04 = make_likert_field(
        "I like to use background music when working in means of public transportation (e.g. train).")
    mt_e_05 = make_likert_field("I like to use background music when working in public places (e.g. cafes, parks).")
    mt_e_06 = make_likert_field("I find it easier to focus with music when I am working alone.")
    mt_e_07 = make_likert_field("I listen to music while working in shared spaces to create a sense of privacy.")
    mt_e_08 = make_likert_field("I listen to music while working in noisy environments.")
    mt_e_09 = make_likert_field("I listen to music while working in quiet environments.")
    mt_ed = make_likert_field("I listen to different types of music for different locations.")

    # ----- Characteristics of Music ----- #
    mt_c_01 = make_likert_field("... classical music.")
    mt_c_02 = make_likert_field("... lofi music.")
    mt_c_03 = make_likert_field("... hip-hop music.")
    mt_c_04 = make_likert_field("... rock music.")
    mt_c_05 = make_likert_field("... pop music.")
    mt_c_06 = make_likert_field("... electronic music.")
    mt_c_07 = make_likert_field("... jazz music.")
    mt_c_08 = make_likert_field("... ambient music.")
    mt_c_09 = make_likert_field("... music with lyrics.")
    mt_c_10 = make_likert_field("... instrumental music without lyrics.")
    mt_c_11 = make_likert_field("... fast music.")
    mt_c_12 = make_likert_field("... slow music.")
    mt_cd = make_likert_field("I like to listen to the same type of music at work as in my free time.")


class ThankYou(Page):
    form_model = 'player'
    form_fields = ['name', 'IBAN', 'BIC']

class Goodbye(Page):
    form_model = 'player'

class TraitQuestionnaire(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        import random
        task_fields = ['ta1', 'ta2', 'ta3']
        random.shuffle(task_fields)
        all_fields=task_fields

        proneness_work_fields = ['fpw1', 'fpw2', 'fpw3', 'fpw4', 'fpw5', 'fpw6', 'fpw7']
        all_fields += proneness_work_fields

        proneness_household_fields = ['fph1', 'fph2', 'fph3', 'fph4', 'fph5', 'fph6', 'fph7']
        all_fields += proneness_household_fields

        proneness_leisure_fields = ['fpl1', 'fpl2', 'fpl3', 'fpl4', 'fpl5', 'fpl6', 'fpl7']
        all_fields += proneness_leisure_fields

        familiarity_fields = ['familiarity', 'familiar_members']
        all_fields += familiarity_fields

        flow_fields = ['sdfs1', 'sdfs2', 'sdfs3', 'sdfs4', 'sdfs5', 'sdfs6', 'sdfs7', 'sdfs8', 'sdfs9']
        random.shuffle(flow_fields)
        all_fields += flow_fields

        ext_fields = ['e1', 'e2', 'e3', 'e4', 'e5']
        random.shuffle(ext_fields)
        all_fields += ext_fields

        domain_fields = ['domain_exp_transcription', 'domain_exp_typing', 'domain_exp_research', 'domain_exp_reading']
        random.shuffle(domain_fields)
        all_fields += domain_fields

        mwt_fields = ['mwt01', 'mwt02', 'mwt03', 'mwt04', 'mwt05', 'mwt06', 'mwt07', 'mwt08', 'mwt09', 'mwt10']
        random.shuffle(mwt_fields)
        all_fields += mwt_fields

        mt_g_fields = ['mt_g_01', 'mt_g_02', 'mt_g_03', 'mt_g_04']
        random.shuffle(mt_g_fields)
        all_fields += mt_g_fields

        return all_fields

class MusicType(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random
        mt_r_fields = ['mt_r_01', 'mt_r_02', 'mt_r_03', 'mt_r_04', 'mt_r_05',
                       'mt_r_06', 'mt_r_07', 'mt_r_08', 'mt_r_09', 'mt_r_10',
                       'mt_r_11', 'mt_r_12', 'mt_r_13', 'mt_r_14', 'mt_r_15',
                       'mt_r_16', 'mt_r_17', 'mt_r_18', 'mt_r_19', 'mt_r_20']
        random.shuffle(mt_r_fields)
        all_fields = mt_r_fields

        mt_s_fields = ['mt_s_01', 'mt_s_02', 'mt_s_03']
        random.shuffle(mt_s_fields)
        all_fields += mt_s_fields

        mt_w_fields = ['mt_w_01', 'mt_w_02', 'mt_w_03', 'mt_w_04', 'mt_w_05',
                       'mt_w_06', 'mt_w_07', 'mt_w_08', 'mt_w_09', 'mt_w_10',
                       'mt_w_11', 'mt_wd']
        random.shuffle(mt_w_fields)
        all_fields += mt_w_fields

        mt_t_fields = ['mt_t_01', 'mt_t_02', 'mt_t_03', 'mt_t_04', 'mt_t_05', 'mt_t_06', 'mt_td']
        random.shuffle(mt_t_fields)
        all_fields += mt_t_fields

        mt_c_fields = ['mt_c_01', 'mt_c_02', 'mt_c_03', 'mt_c_04', 'mt_c_05', 'mt_c_06', 'mt_c_07', 'mt_cd']
        random.shuffle(mt_c_fields)
        all_fields += mt_c_fields

        mt_e_fields = ['mt_e_01', 'mt_e_02', 'mt_e_03', 'mt_e_04', 'mt_e_05',
                       'mt_e_06', 'mt_e_07', 'mt_e_08', 'mt_e_09', 'mt_ed']
        random.shuffle(mt_e_fields)
        all_fields += mt_e_fields

        return all_fields



page_sequence = [TraitQuestionnaire, ThankYou, Goodbye]