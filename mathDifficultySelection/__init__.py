import random
from otree.api import *
c = cu
doc = ''

class Constants(BaseConstants):
    name_in_url = 'MathDifficultySelection'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # ----- FLOW SHORT SCALE ----- #
    fss01 = models.IntegerField(
        label='I felt just the right amount of challenge.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss02 = models.IntegerField(
        label='My thoughts/activities ran fluidly and smoothly.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss03 = models.IntegerField(
        label="I didn't notice time passing.",
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss04 = models.IntegerField(
        label='I had no difficulty concentrating.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss05 = models.IntegerField(
        label='My mind was completely clear.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss06 = models.IntegerField(
        label='I was totally absorbed in what I was doing.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss07 = models.IntegerField(
        label='The right thoughts/movements occurred of their own accord.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss08 = models.IntegerField(
        label='I knew what I had to do each step of the way.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss09 = models.IntegerField(
        label='I felt that I had everything under control.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    fss10 = models.IntegerField(
        label='I was completely lost in thought.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- AUTONOMY ----- #
    aut01 = models.IntegerField(
        label='I was free to do things my own way.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    aut02 = models.IntegerField(
        label='My choices expressed my ‘‘true self’’.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    aut03 = models.IntegerField(
        label='I was really doing what interests me.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- RATING SCALE MENTAL EFFORT ----- #
    rsme = models.IntegerField(
        min = 0,
        max = 150
    )

    # ----- FATIGUE ----- #
    fatigue_state = models.StringField(
        label='How tired/awake are you right now?',
        choices=['Fully alert, wide awake ',
                 'Very lively, responsive, but not at peak',
                 'Okay, somewhat fresh',
                 'A little tired, less than fresh',
                 'Moderately tired, let down',
                 'Extremely tired, very difficult to concentrate',
                 'Completely exhausted, unable to function effectively']
    )

    # ----- PLEASURE & AROUSAL ----- #
    pleasure = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, '']]
    )

    arousal = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, '']]
    )

    # ----- PERCEIVED DIFFICULTY & SKILL ----- #
    difficulty = models.IntegerField(
        label='Compared to all other activities which I participate in, this one was...',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    competence = models.IntegerField(
        label = 'I think that my competence in this area is...',
        choices = [[1, ''], [2, ''], [3, ''], [4, ''],
                   [5, ''], [6, ''], [7, '']],
        widget = widgets.RadioSelectHorizontal
    )

    demands = models.IntegerField(
        label='For me personally, the task\'s demands were generally...',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- TASK IMPORTANCE ----- #
    importance01 = models.IntegerField(
        label='During this task, something important to me was at stake.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    importance02 = models.IntegerField(
        label='During this task, I was careful not to make any mistakes.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    importance03 = models.IntegerField(
        label='During this task, I was worried about failing.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- INTRINSIC MOTIVATION / INTEREST ----- #
    interest01 = models.IntegerField(
        label='I enjoyed doing this task very much.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest02 = models.IntegerField(
        label='This task was fun to do.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest03 = models.IntegerField(
        label='I thought this was a boring task.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest04 = models.IntegerField(
        label='This task did not hold my attention at all.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest05 = models.IntegerField(
        label='I would describe this task as very interesting.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest06 = models.IntegerField(
        label='I thought this task was quite enjoyable.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )
    interest07 = models.IntegerField(
        label='While I was doing this task, I was thinking about how much I enjoyed it.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''],
                 [5, ''], [6, ''], [7, '']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- MATH TASK ACTIONS ----- #
    math_actions = models.StringField(
        label=''
    )

    math_actions_tutorial = models.StringField(
        label=''
    )

    math_difficulty_selection = models.IntegerField(
        label='Select your difficulty:',
        initial=6,
        min=1,
        max=12
    )

class BetweenRounds_fss(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        fss_fields = ['fss01', 'fss02', 'fss03', 'fss04', 'fss05', 'fss06', 'fss07', 'fss08', 'fss09', 'fss10']
        aut_fields = ['aut01', 'aut02', 'aut03']
        rsme_fields = ['rsme']
        fatigue_fields = ['fatigue_state']

        random.shuffle(fss_fields)
        random.shuffle(aut_fields)

        form_fields = fss_fields + aut_fields + rsme_fields + fatigue_fields
        return form_fields

class BetweenRounds_rsme(Page):
    form_model = 'player'

    form_fields = ['rsme']

class BetweenRounds_pna(Page):
    form_model = 'player'

    form_fields = ['pleasure', 'arousal']

class MathInstructions(Page):
    form_model = 'player'

class MathTutorial(Page):
    form_model = 'player'
    form_fields = ['math_actions_tutorial']

    def vars_for_template(player: Player):
        return {
            "taskDuration": player.participant.vars['taskDurationMsTut'],
            "trialDuration": player.participant.vars['trialDurationMsTut'],
            "breakDuration": player.participant.vars['breakDurationMsTut']
        }

class AfterTutorial(Page):
    form_model = 'player'

class AfterSelection(Page):
    form_model = 'player'

class MathEasy(Page):
    form_model = 'player'
    form_fields = ['math_actions']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "taskDuration": 60 * 1000,
            "trialDuration": 18 * 1000,
            "breakDuration": 4 * 1000
        }


class MathDifficultySelection(Page):
    form_model = 'player'
    form_fields = ['math_difficulty_selection']

    def before_next_page(player: Player, timeout_happened):
        player.participant.math_difficulty_selection = player.math_difficulty_selection

page_sequence = [MathInstructions, MathTutorial, AfterTutorial,
                 MathEasy, MathDifficultySelection, AfterSelection, MathCalibration]