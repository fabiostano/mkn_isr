import random
from random import choice
import statistics
from otree.api import *
c = cu
doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'mathJitsi'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 6
    TASK_TIME_LIMIT = 5 * 60 # Task Time
    TRIAL_TIME = 28
    BREAK_TIME = 4
    MIN_DIFFICULTY = 1  # Start difficulty level
    MAX_DIFFICULTY = 50  # Highest difficulty level; As in brownie autonomy selection screen;

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']
    LATIN_SQUARE_ORDERS = [
        ["B", "F", "O", "A"],
        ["F", "A", "B", "O"],
        ["O", "B", "A", "F"],
        ["A", "O", "F", "B"]
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    color = models.StringField(initial="none")
    action_log = models.LongStringField(initial="")
    answer_history = models.StringField(initial="")
    level_history = models.StringField(initial="", blank=True)
    level_storage = models.IntegerField()  # This is for the self-selected difficulty

    # ----- Timestamps ----- #
    task_load_time = models.StringField(blank=True)
    rest_actions_eo = models.StringField(label="")

    # ----- Communication Logs ----- #
    speech_time = models.StringField(blank=True)

    def make_7p_likert_field(label, blank=False):
        return models.IntegerField(
            label=label,
            choices=[1, 2, 3, 4, 5, 6, 7],
            widget=widgets.RadioSelectHorizontal,
            blank=blank
        )

    ### Task Round Survey

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test",
                                   choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'],
                                            [8, '8'], [9, '9']], widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'],
                                           [8, '8'], [9, '9']], widget=widgets.RadioSelectHorizontal)

    # ----- Flow ----- #
    fss01 = make_7p_likert_field('I felt just the right amount of challenge.')
    fss02 = make_7p_likert_field('My thoughts/activities ran fluidly and smoothly.')
    fss03 = make_7p_likert_field('I didn’t notice time passing.')
    fss04 = make_7p_likert_field('I had no difficulty concentrating.')
    fss05 = make_7p_likert_field('My mind was completely clear.')
    fss06 = make_7p_likert_field('I was totally absorbed in what I was doing.')
    fss07 = make_7p_likert_field('The right thoughts/movements occurred of their own accord.')
    fss08 = make_7p_likert_field('I knew what I had to do each step of the way.')
    fss09 = make_7p_likert_field('I felt that I had everything under control.')
    fss10 = make_7p_likert_field('I was completely involved in the task.')

    sfss1 = make_7p_likert_field('I felt I was competent enough to meet the demands of the situation.')
    sfss2 = make_7p_likert_field('I had a strong sense of what I wanted to do.')
    sfss3 = make_7p_likert_field('I had a good idea about how well I was doing while I was involved in the task/activity.')

    # ----- Challenge Skill Balance ----- #
    csb1 = make_7p_likert_field('Compared to all other activities which I partake in, the difficulty of this one is ...')
    csb2 = make_7p_likert_field('For me personally, the task demands were ...')

    # ----- Individual Stress ----- #
    is1 = make_7p_likert_field('... I felt strain due to the task demands.')
    is2 = make_7p_likert_field('... I felt emotionally drained.')
    is3 = make_7p_likert_field('... I felt used up due to the task demands.')
    is4 = make_7p_likert_field('... I felt fatigued due to the task demands.')
    is5 = make_7p_likert_field('... I felt burned out from working on the task.')

    # ----- Perceived Task Performance ----- #
    ptp1 = make_7p_likert_field('How successful do you think you were in accomplishing the goals of the task set by the experimenter (or yourself)?')
    ptp2 = make_7p_likert_field('How satisfied were you with your performance in accomplishing these goals?')
    ptp3 = make_7p_likert_field('How hard did you work to accomplish your level of performance?')

    # ----- Satisfaction of Autonomy Need ----- #
    san1 = make_7p_likert_field('I was free to do things my own way.')
    san2 = make_7p_likert_field('My choices expressed my "true self".')
    san3 = make_7p_likert_field('I was really doing what interests me.')

    # ----- Task Motivation ----- #
    tm1 = make_7p_likert_field('I was motivated to perform well on this task.')
    tm2 = make_7p_likert_field('Performing the task was interesting to me.')
    tm3 = make_7p_likert_field('I put a lot of effort into coming up with the correct solutions.')

    # ----- Collective Challenge Skill Balance ----- #
    ccsb1 = make_7p_likert_field('The difficulty of this activity for our team is ...')
    ccsb2 = make_7p_likert_field('For us as a team, the task demands were ...')

    # ----- Emotional Contagion ----- #
    ec1 = make_7p_likert_field('How much were you on the same wavelength with your team?')

    # ----- Emotional Synchrony ----- #
    es1 = make_7p_likert_field('We felt a strong shared emotion.')

    # ----- Perceived Group Performance ----- #
    pgp1 = make_7p_likert_field('How successful do you think your team was in accomplishing the goals of the task set by the experimenter (or yourself)?')
    pgp2 = make_7p_likert_field('How satisfied were you with your team’s performance in accomplishing these goals?')
    pgp3 = make_7p_likert_field('How hard did your team work to accomplish your level of performance?')

    # ----- Information Sharing ----- #
    info1 = make_7p_likert_field('We shared useful information with each of the team members.')
    info2 = make_7p_likert_field('We made sure we correctly understood our co-workers’ contributions.')

    ### Task Phase Survey

    # ----- Task Importance ----- #
    ti1 = make_7p_likert_field('... something important to me was at stake.')
    ti2 = make_7p_likert_field('... I was careful to not make mistakes.')
    ti3 = make_7p_likert_field('... I was worried about failing.')

    # ----- Perceived Task Complexity ----- #
    ptc1 = make_7p_likert_field('This task was a complex task.')
    ptc2 = make_7p_likert_field('This task was mentally demanding.')
    ptc3 = make_7p_likert_field('This task required a lot of thought and problem-solving.')
    ptc4 = make_7p_likert_field('This task was challenging.')

    # ----- Quality of Team Interaction ----- #
    qti1 = make_7p_likert_field('There was a lot of unpleasantness amoung members of this team.')
    qti2 = make_7p_likert_field('The longer we worked together as a team, the less well we did.')
    qti3 = make_7p_likert_field('Working together energised and uplifted members of our team.')
    qti4 = make_7p_likert_field('Every time someone attempted to correct a solution, things seemed to get worse rather than better.')

    # ----- Teamwork Enjoyment ----- #
    twe1 = make_7p_likert_field('My relations with other team members were strained.')
    twe2 = make_7p_likert_field('I very much enjoyed talking and working with my teammates.')
    twe3 = make_7p_likert_field('The chance to interact was one of the best parts of working on this team.')

    # ----- Team Effort ----- #
    te1 = make_7p_likert_field('Team members demonstrated their commitment by putting in a lot of effort to help us succeed.')
    te2 = make_7p_likert_field('Everyone on this team was motivated to have the team succeed.')
    te3 = make_7p_likert_field('Some members of our team did not carry their fair share of the overall workload.')

    # ----- Interdependence ----- #
    int1 = make_7p_likert_field('Members of this group had their own individual jobs to do, with little need for them to work together.')
    int2 = make_7p_likert_field('Generating the outcome or product of this group required a great deal of communication and coordination among members.')
    int3 = make_7p_likert_field('Members of this group had to depend heavily on one another to get the group’s work done.')

    # ----- Common Goal ----- #
    cg1 = make_7p_likert_field('There was great uncertainty and ambiguity about what this group is supposed to accomplish.')
    cg2 = make_7p_likert_field('This group’s purposes were specified so clearly that all members knew exactly what the group had to accomplish.')
    cg3 = make_7p_likert_field('This group’s purposes were so challenging that members had to stretch to accomplish them.')
    cg4 = make_7p_likert_field('This group’s purposes were not especially challenging—achieving them was well within reach.')
    cg5 = make_7p_likert_field('The actions of this group don’t make much of a difference to anybody else.')
    cg6 = make_7p_likert_field('This group’s actions were of great importance for those giving us the tasks.')

    # ----- Teamwork Behaviors ----- #
    twb1 = make_7p_likert_field('Our team often comes up with innovative ways of proceeding with the work that turn out to be just what is needed.')
    twb2 = make_7p_likert_field('Our team often falls into mindless routines, without noticing any changes that may have occurred in our situation.')
    twb3 = make_7p_likert_field('Our team has a great deal of difficulty actually carrying out the plans we make for how we will proceed with the task.')
    twb4 = make_7p_likert_field('How seriously a member’s ideas are taken by others on our team often depends more on who the person is than on how much he or she actually knows.')
    twb5 = make_7p_likert_field('Members of our team actively share their special knowledge and expertise with one another.')
    twb6 = make_7p_likert_field('Our team is quite skilled at capturing the lessons that can be learned from our work experiences.')

    # ----- Team Size ----- #
    tsz1 = make_7p_likert_field('This group was larger than it needed to be.')
    tsz2 = make_7p_likert_field('This group had too few members for what it had to accomplish.')
    tsz3 = make_7p_likert_field('This group was just the right size to accomplish its purposes.')

    # ----- Team Diversity ----- #
    td1 = make_7p_likert_field('Members of this group were too dissimilar to work together well.')
    td2 = make_7p_likert_field('This group did not have a broad enough range of experiences and perspectives to accomplish its purposes.')
    td3 = make_7p_likert_field('This group had a nearly ideal “mix” of members’  abilities and experiences.')

    # ----- Team Skills Complementarity ----- #
    tsc1 = make_7p_likert_field('Members of this group had more than enough talent and experience for the kind of task that we did.')
    tsc2 = make_7p_likert_field('Everyone in this group had the skills that are needed for the group’s work.')
    tsc3 = make_7p_likert_field('Some members of this group lacked the knowledge and skills that they needed to do their parts of the group’s work.')

    # ----- Means for Coordination ----- #
    mc1 = make_7p_likert_field('The format of the task made it difficult to coordinate our interaction.')
    mc2 = make_7p_likert_field('During the tasks, it was sufficiently possible to coordinate our work.')

    # ----- Work Motivation ----- #
    wm1 = make_7p_likert_field('I felt a real sense of personal satisfaction when our team did well.')
    wm2 = make_7p_likert_field('I felt bad and unhappy when our team had performed poorly.')
    wm3 = make_7p_likert_field('My own feelings were not affected one way or the other by how well our team performed.')
    wm4 = make_7p_likert_field('When our team has done well, I have done well.')

    # ----- Work Satisfaction ----- #
    ws1 = make_7p_likert_field('I enjoy the kind of work we did in this team.')
    ws2 = make_7p_likert_field('Working on this team is an exercise in frustration.')
    ws3 = make_7p_likert_field('Generally speaking, I am very satisfied with this team.')

    # ----- Personal Growth ----- #
    perg1 = make_7p_likert_field('I learn a great deal from my work on this team.')
    perg2 = make_7p_likert_field('My own creativity and initiative are suppressed by this team.')
    perg3 = make_7p_likert_field('Working on this team stretches my personal knowledge and skills.')

    # ----- Collective Efficacy ----- #
    ce1 = make_7p_likert_field('Our team shows more abilities than other groups.')
    ce2 = make_7p_likert_field('Our team is more efficiently prepared to complete such tasks.')
    ce3 = make_7p_likert_field('Our team has the ability to overcome problems.')

    # ----- Skill Level ----- #
    sl1 = make_7p_likert_field('I think that my competence in this area is ...')
    sl2 = make_7p_likert_field('I think that our team’s competence in this area is ...')

    # ----- Perceived Social Presence ----- #
    psp1 = make_7p_likert_field('There was a sense of human contact during the group work.')
    psp2 = make_7p_likert_field('There was a sense of personalness during the group work.')
    psp3 = make_7p_likert_field('There was a sense of sociability during the group work.')
    psp4 = make_7p_likert_field('There was a sense of human warmth during the group work.')
    psp5 = make_7p_likert_field('There was a sense of human sensitivity during the group work.')

    # ----- Identity Fusion ----- #
    fusion = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                 widget=widgets.RadioSelectHorizontal)

    # ----- Familiarity ----- #
    fam1_lightcoral = make_7p_likert_field('After this task, how well do you know the player labeled lightcoral?', blank=True)
    fam2_lightcoral = make_7p_likert_field('During the task, how closely did you work together with the player labeled lightcoral?', blank=True)
    fam1_lightgreen = make_7p_likert_field('After this task, how well do you know the player labeled lightgreen?', blank=True)
    fam2_lightgreen = make_7p_likert_field('During the task, how closely did you work together with the player labeled lightgreen?', blank=True)
    fam1_lightblue = make_7p_likert_field('After this task, how well do you know the player labeled lightblue?', blank=True)
    fam2_lightblue = make_7p_likert_field('During the task, how closely did you work together with the player labeled lightblue?', blank=True)

def creating_session(subsession):
    def creating_session(subsession):
        for group in subsession.get_groups():
            if group.round_number == 1:
                # Draw once and store at the session level
                condition_order = choice(C.LATIN_SQUARE_ORDERS)
                print("Chosen Latin square:", condition_order)

                for p in group.get_players():
                    p.participant.condition_order = condition_order

            for p in group.get_players():
                p.color = C.COLORMAP[p.id_in_group - 1]

class Explanation(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "round_nr": player.round_number - 1
        }

    def is_displayed(player: Player):
        return player.round_number > 1

class PracticeAfter(Page):
    form_model = 'player'

    def is_displayed(player: Player):
        return player.round_number == 1

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

    def is_displayed(player: Player):
        return player.round_number > 1

class BeforeTask(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "round_number": player.round_number
        }

    def is_displayed(player: Player):
        return player.round_number < 2

    def before_next_page(player, timeout_happened):
        player.color = C.COLORMAP[player.id_in_group-1]

class Wait_Page(WaitPage):
    form_model = 'player'
    title_text = "Please wait until all other team members are ready."
    body_text = "You will be redirected automatically."

class TaskSurvey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random
        all_fields = []
        state_fields = ['pleasure', 'arousal']
        all_fields += state_fields
        fss_fields = ['fss01', 'fss02', 'fss03', 'fss04', 'fss05', 'fss06', 'fss07', 'fss08', 'fss09', 'fss10']
        random.shuffle(fss_fields)
        all_fields += fss_fields
        sfss_fields = ['sfss1', 'sfss2', 'sfss3']
        random.shuffle(sfss_fields)
        all_fields += sfss_fields
        csb_fields = ['csb1', 'csb2']
        random.shuffle(csb_fields)
        all_fields += csb_fields
        is_fields = ['is1', 'is2', 'is3', 'is4', 'is5']
        random.shuffle(is_fields)
        all_fields += is_fields
        ptp_fields = ['ptp1', 'ptp2', 'ptp3']
        random.shuffle(ptp_fields)
        all_fields += ptp_fields
        san_fields = ['san1', 'san2', 'san3']
        random.shuffle(san_fields)
        all_fields += san_fields
        tm_fields = ['tm1', 'tm2', 'tm3']
        random.shuffle(tm_fields)
        all_fields += tm_fields
        ccsb_fields = ['ccsb1', 'ccsb2']
        random.shuffle(ccsb_fields)
        all_fields += ccsb_fields
        ec_fields = ['ec1']
        all_fields += ec_fields
        es_fields = ['es1']
        random.shuffle(es_fields)
        all_fields += es_fields
        pgp_fields = ['pgp1', 'pgp2', 'pgp3']
        random.shuffle(pgp_fields)
        all_fields += pgp_fields
        info_fields = ['info1', 'info2']
        random.shuffle(info_fields)
        all_fields += info_fields
        return all_fields

class TaskPhaseSurvey(Page):
    form_model = 'player'

    def vars_for_template(player):
        return dict(my_color=player.color)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        all_fields = []
        ptc_fields = ['ptc1', 'ptc2', 'ptc3', 'ptc4']
        random.shuffle(ptc_fields)
        all_fields += ptc_fields
        qti_fields = ['qti1', 'qti2', 'qti3', 'qti4']
        random.shuffle(qti_fields)
        all_fields += qti_fields
        twe_fields = ['twe1', 'twe2', 'twe3']
        random.shuffle(twe_fields)
        all_fields += twe_fields
        te_fields = ['te1', 'te2', 'te3']
        random.shuffle(te_fields)
        all_fields += te_fields
        int_fields = ['int1', 'int2', 'int3']
        random.shuffle(int_fields)
        all_fields += int_fields
        cg_fields = ['cg1', 'cg2', 'cg3', 'cg4', 'cg5', 'cg6']
        random.shuffle(cg_fields)
        all_fields += cg_fields
        twb_fields = ['twb1', 'twb2', 'twb3', 'twb4', 'twb5', 'twb6']
        random.shuffle(twb_fields)
        all_fields += twb_fields
        tsz_fields = ['tsz1', 'tsz2', 'tsz3']
        random.shuffle(tsz_fields)
        all_fields += tsz_fields
        td_fields = ['td1', 'td2', 'td3']
        random.shuffle(td_fields)
        all_fields += td_fields
        tsc_fields = ['tsc1', 'tsc2', 'tsc3']
        random.shuffle(tsc_fields)
        all_fields += tsc_fields
        mc_fields = ['mc1', 'mc2']
        random.shuffle(mc_fields)
        all_fields += mc_fields
        wm_fields = ['wm1', 'wm2', 'wm3', 'wm4']
        random.shuffle(wm_fields)
        all_fields += wm_fields
        ws_fields = ['ws1', 'ws2', 'ws3']
        random.shuffle(ws_fields)
        all_fields += ws_fields
        perg_fields = ['perg1', 'perg2', 'perg3']
        random.shuffle(perg_fields)
        all_fields += perg_fields
        ce_fields = ['ce1', 'ce2', 'ce3']
        random.shuffle(ce_fields)
        all_fields += ce_fields
        sl_fields = ['sl1', 'sl2']
        random.shuffle(sl_fields)
        all_fields += sl_fields
        psp_fields = ['psp1', 'psp2', 'psp3', 'psp4', 'psp5']
        random.shuffle(psp_fields)
        all_fields += psp_fields
        fam_fields = ['fam1_lightcoral', 'fam2_lightcoral', 'fam1_lightgreen', 'fam2_lightgreen', 'fam1_lightblue', 'fam2_lightblue']
        all_fields += fam_fields
        fusion_fields = ['fusion']
        all_fields += fusion_fields
        return all_fields

    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

# A function to calculate the optimal difficulty from the calibration stage
def calculate_baseline_level(level_history_str):
    # Convert the comma-separated string into a list of integers
    levels = list(map(int, level_history_str.strip().split(',')))
    n = len(levels)

    # If there are no levels, return the default baseline level of 1
    if n == 0:
        return 1

    # Compute the number of values to consider: last 25% of the list
    # Add 1 if there's a remainder to match the Java behavior
    quartile_len = n // 4 + (1 if n % 4 > 0 else 0)

    # Slice the last 'quartile_len' values from the list
    recent_levels = levels[-quartile_len:]

    # Compute and return the integer average (rounded down)
    return sum(recent_levels) // quartile_len

class Task(Page):
    form_model = 'player'
    form_fields = ['action_log', 'task_load_time', 'level_history', 'speech_time']

    def vars_for_template(player):
        # Configure parameters for different task round (difficulty treatments)
        if player.round_number == 1:  # This is the practice round!
            level = 1
            difficulty = "Easy"
            min_level = C.MIN_DIFFICULTY
        elif player.round_number == 2:  # This is the calibration round!
            level = 1
            difficulty = "Optimal"
            min_level = C.MIN_DIFFICULTY

        # Now start the "real" task rounds (after practice and calibration)
        else:  # Rounds 3–6: Experimental rounds
            # Get current condition letter from the Latin square
            index = player.round_number - 3  # 0 for round 3, up to 3 for round 6
            condition = player.participant.condition_order[index]

            if condition == "B":
                level = 1
                difficulty = "Easy"
                min_level = C.MIN_DIFFICULTY

            elif condition == "F":
                level = player.participant.calibrated_difficulty
                difficulty = "Optimal"
                min_level = C.MIN_DIFFICULTY

            elif condition == "A":
                # Check all difficulty selections and calculate the median
                selected_difficulties = []
                for p in player.group.get_players():
                    selected_difficulties.append(p.participant.selected_difficulty)
                median_difficulty = statistics.median(selected_difficulties)
                # Set the parameters
                level = median_difficulty
                difficulty = "Optimal"
                min_level = C.MIN_DIFFICULTY

            elif condition == "O":
                # "In the Hard condition, the difficulty level could not fall more than
                # three levels below the calibrated starting level. This starting level
                # was set to be twelve levels higher than the level calibrated as optimal
                # for the participant(s) in a calibration stage before the main task."
                level = player.participant.calibrated_difficulty + 12
                # print("Level: " + str(level))
                difficulty = "Hard"
                min_level = level - 3

            else:
                raise ValueError(f"Unknown condition: {condition}")

        return dict(
            level=level,
            min_level=min_level,
            max_level=C.MAX_DIFFICULTY,
            difficulty=difficulty,
            id=player.id_in_group,
            taskDuration=C.TASK_TIME_LIMIT,
            trialDuration=C.TRIAL_TIME,
            breakDuration=C.BREAK_TIME,
            color=C.COLORMAP[player.id_in_group - 1],
            room_id=player.group.id
        )

    def before_next_page(player, timeout_happened):
        if player.round_number == 2:  # This is the calibration round!
            # Check if the level_history object is not empty
            if player.level_history and player.level_history.strip():
                calibrated_difficulty = calculate_baseline_level(player.level_history)
                print("Calibrated difficulty: " + str(calibrated_difficulty))

                # Set this level for all participants
                for p in player.subsession.get_players():
                    p.participant.calibrated_difficulty = calibrated_difficulty

            # else: # This would be the case if I auto-advance (even just one player...)
            #    player.participant.calibrated_difficulty = -1


    @staticmethod
    def live_method(player, data):
        group = player.group
        info_type = data.get("info_type")

        # Get the group-level shared dict to track selections
        if not group.session.vars.get("active_selections"):
            group.session.vars["active_selections"] = {}  # { "sol_1": "lightblue", "sol_2": "lightgreen", ... }

        active_selections = group.session.vars["active_selections"]

        if info_type == "selected":
            selected_id = data.get("selected")
            player_color = data.get("player")

            active_selections = group.session.vars["active_selections"]

            # Remove previous selection by the same player
            previous_selection = [key for key, value in active_selections.items() if value == player_color]
            for key in previous_selection:
                del active_selections[key]  # Remove old selection

            # Check if the new field is already taken
            if selected_id.startswith("final"):
                # Allow overlapping selections on final input fields
                pass
            elif selected_id in active_selections:
                return {}  # Prevent overriding someone else's selection

            # Assign the new selection to this player
            active_selections[selected_id] = player_color
            group.session.vars["active_selections"] = active_selections

            print(active_selections)

            # Broadcast updates
            return {p.id_in_group: {"info_type": "selected", "player": player_color, "selected": selected_id,
                                    "previous": previous_selection} for p in group.get_players()}

        # Handle deselection
        elif info_type == "deselect":
            player_color = data.get("player")
            active_selections = group.session.vars["active_selections"]
            element = data.get("deselected")

            # Find the player's current selection and remove it
            fields_to_remove = [key for key, value in active_selections.items() if value == player_color]

            for key in fields_to_remove:
                del active_selections[key]  # Remove only the player's selection

            group.session.vars["active_selections"] = active_selections

            # Broadcast deselection update to all players
            return {p.id_in_group: {"info_type": "deselected", "player": player_color, "field": element} for p
                    in group.get_players()}

        # Handle input changes
        elif info_type == "input_changed":
            selected_id = data.get("selected")
            content = data.get("content")
            return {p.id_in_group: {"info_type": "input_changed", "player": player.color,
                                    "selected": selected_id, "content": content} for p in group.get_players()}

        # Handle input changes
        elif info_type == "final_input_changed":
            content = data.get("content")
            return {p.id_in_group: {"info_type": "final_input_changed", "player": data.get("player"),
                                    "content": content} for p in group.get_players()}

        elif info_type == "Equations":
            return {p.id_in_group: data for p in group.get_players()}

        elif info_type == "openFinalInput":
            return {p.id_in_group: data for p in group.get_players()}

        elif info_type == "timeUp":
            return {p.id_in_group: data for p in group.get_players()}

        elif info_type == "final_answer_submitted":
            player_color = data.get("player")
            answer = data.get("answer")

            # Sammelbecken für abgegebene Antworten
            submissions = group.session.vars.setdefault("final_submissions", {})
            submissions[player_color] = answer

            # Noch nicht alle fertig → nur diese Abgabe broadcasten
            if len(submissions) < len(group.get_players()):
                return {p.id_in_group: {
                    "info_type": "player_submitted",
                    "player": player_color,
                    "answer": answer
                } for p in group.get_players()}

            # Alle drei haben abgegeben → Broadcast & Speicher leeren
            group.session.vars["final_submissions"] = {}
            return {p.id_in_group: {
                "info_type": "all_submitted",
                "submissions": submissions
            } for p in group.get_players()}

        return {}

class DifficultySelection(Page):
    form_model = 'player'
    form_fields = ['level_storage']

    def vars_for_template(player):
        return dict(
            level = 1,
            min_level = 1,
            max_level = C.MAX_DIFFICULTY,
            id = player.id_in_group,
            color = C.COLORMAP[player.id_in_group-1]
        )

    def before_next_page(player, timeout_happened):
        # Set this level for this participant
        player.participant.selected_difficulty = player.level_storage

    def is_displayed(player: Player):
        # Only applicable for rounds 3–6
        if player.round_number < 3:
            return False

        index = player.round_number - 3  # Index 0–3 for condition_order
        return player.participant.condition_order[index] == "A"

page_sequence = [BeforeTask, # Only shown once
                 DifficultySelection, # Only shown once
                 Explanation, Wait_Page, Task, # All repeated (incl. practice and calibration)
                 PracticeAfter,
                 TaskSurvey, RestEyesOpen, # All repeated (only after calibration)
                 TaskPhaseSurvey # Only shown once
                 ]