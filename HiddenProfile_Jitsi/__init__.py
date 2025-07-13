from otree.api import *
import random
from random import choice

class C(BaseConstants):
    NAME_IN_URL = 'HiddenProfile_Jitsi'
    PLAYERS_PER_GROUP = 3  # CHRO, CMO, CFO
    NUM_ROUNDS = 3
    BASE_PAYOUT = 200
    TEAM_BONUS = 30
    DEPT_BONUS = 50
    MAX_INFO_SHARING_BONUS = 70
    TASK_PREP_TIME_LIMIT = 3*60
    TASK_TIME_LIMIT = 5*60  # 3 * 60  # Task Time

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']

    PROJECTS = [
        {'name': 'Project A: EcoTrack', 'profit': 4, 'env_impact': 60, 'market_demand': 70000, 'salary_cost': 50000,
         'criteria': 'environmental'},
        {'name': 'Project B: TalentSphere', 'profit': 3, 'env_impact': 95, 'market_demand': 80000, 'salary_cost': 60000,
         'criteria': 'salary'},
        {'name': 'Project C: MarketPulse', 'profit': 2, 'env_impact': 40, 'market_demand': 60000, 'salary_cost': 55000,
         'criteria': 'market'}
    ]

    FACTORIES = [
        {'name': 'Factory A: United States', 'construction_cost': 280, 'energy_cost': 55, 'criteria': 'skills'},
        {'name': 'Factory B: China', 'construction_cost': 190, 'energy_cost': 50, 'criteria': 'costs'},
    ]

    CANDIDATES = [
        {'name': 'Candidate A: SBU Europe', 'headcount': 6.200, 'revenue_growth': 5, 'profit_margin': 16, 'customer_satisfaction': 83,
         'criteria': 'operational efficiency'},
        {'name': 'Candidate B: SBU Asia', 'headcount': 8.400, 'revenue_growth': 10, 'profit_margin': 14, 'customer_satisfaction': 79,
         'criteria': 'scalability'},
        {'name': 'Candidate 3: SBU Americas', 'headcount': 5.600, 'revenue_growth': 7, 'profit_margin': 18, 'customer_satisfaction': 88,
         'criteria': 'customer engagement'},
        {'name': 'Candidate 4: SBU Africa', 'headcount': 3.800, 'revenue_growth': 7, 'profit_margin': 10, 'customer_satisfaction': 72,
        'criteria': 'workforce investments'},
        {'name': 'Candidate 5: SBU Middle East', 'headcount': 5.200, 'revenue_growth': 4, 'profit_margin': 19, 'customer_satisfaction': 78,
         'criteria': 'digital innovation'},
        {'name': 'Candidate 6: SBU Australia', 'headcount': 2.1000, 'revenue_growth': 9, 'profit_margin': 17, 'customer_satisfaction': 86,
         'criteria': 'agile product management'},
    ]

    ROLES = ['Chief Human Resources Officer', 'Chief Marketing Officer',
             'Chief Financial Officer']

    TIMEOUT_SECONDS = 5 * 60  # 5 minutes in seconds
    SENTIMENT_UPDATE_INTERVAL = 15  # seconds

    LATIN_SQUARE_ORDERS = [
        ["EASY", "MED", "HARD"],
        ["MED", "HARD", "EASY"],
        ["HARD", "EASY", "MED"]
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    chosen_project = models.StringField(initial=None)
    project_profit = models.CurrencyField(initial=0)

    chosen_factory = models.StringField(initial=None)
    factory_points = models.CurrencyField(initial=0)

    chosen_candidate = models.StringField(initial=None)
    candidate_points = models.CurrencyField(initial=0)

class Player(BasePlayer):
    color = models.StringField(initial="none")
    player_role = models.StringField()
    personal_interest = models.StringField()
    shared_info = models.StringField()
    project_choice = models.StringField()
    factory_choice = models.StringField()
    candidate_choice = models.StringField(blank=True)
    player_payoff = models.CurrencyField(initial=C.BASE_PAYOUT)
    next_ready = models.BooleanField(initial=False)

    # ----- Timestamps ----- #
    task_load_time_project = models.StringField(blank=True)
    task_finish_click_time_project = models.StringField(blank=True)
    task_end_time_project = models.StringField(blank=True)
    task_load_time_discussion = models.StringField(blank=True)
    task_finish_click_time_discussion = models.StringField(blank=True)
    task_end_time_discussion = models.StringField(blank=True)
    rest_actions_eo = models.StringField(label="")

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

    # ----- Perceived Task Complexity ----- #
    ptc1 = make_7p_likert_field('This task was a complex task.')
    ptc2 = make_7p_likert_field('This task was mentally demanding.')
    ptc3 = make_7p_likert_field('This task required a lot of thought and problem-solving.')
    ptc4 = make_7p_likert_field('This task was challenging.')

    # ----- Quality of Team Interaction ----- #
    qti1 = make_7p_likert_field('There was a lot of unpleasantness among members of this team.')
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

def creating_session(subsession: Subsession):
    for group in subsession.get_groups():
        import random
        roles = C.ROLES[:]
        random.shuffle(roles)

        # Draw once and store at the session level
        if group.round_number == 1:
            # Draw once and store at the session level
            hp_condition_order = choice(C.LATIN_SQUARE_ORDERS)
            print("Chosen Latin square for HP:", hp_condition_order)

            for p in group.get_players():
                p.participant.hp_condition_order = hp_condition_order

        for p in group.get_players():
            p.color = C.COLORMAP[p.id_in_group - 1]
            p.player_role = roles.pop()

            if p.player_role == 'Chief Human Resources Officer':
                p.personal_interest = 'salary_cost'
            elif p.player_role == 'Chief Marketing Officer':
                p.personal_interest = 'market_demand'
            elif p.player_role == 'Chief Financial Officer':
                p.personal_interest = 'profit'

class RoleAssignment(Page):
    def vars_for_template(player: Player):
         return {
            'role': player.player_role,
            'personal_interest': player.personal_interest,
             "round_nr": player.round_number
        }

    def is_displayed(player: Player):
        return player.round_number == 1

class WaitForRoleAssignment(WaitPage):
    def is_displayed(self):
        # This ensures that all players must pass through this wait page
        return True

    def before_next_page(self):
        for p in self.group.get_players():
            p.next_ready = False

class DiscussionPreface(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Discussion(Page):
    form_model = 'player'
    form_fields = ['task_load_time_discussion', 'task_finish_click_time_discussion', 'task_end_time_discussion', 'speech_time']

    def vars_for_template(player):
        return dict(
            id = player.id_in_group,
            color=C.COLORMAP[player.id_in_group - 1],
            taskDuration=C.TASK_TIME_LIMIT,
            room_id=player.group.id
        )

    @staticmethod
    def live_method(player, data):
        if data.get("type") == "next_clicked":
            player.next_ready = True

            all_ready = all(p.next_ready for p in player.group.get_players())
            if all_ready:
                return {p.id_in_group: {"type": "go_to_next"} for p in player.group.get_players()}
            else:
                return {player.id_in_group: {"type": "waiting"}}

class ProjectDecision(Page):
    form_model = 'player'
    form_fields = ['project_choice']

    @staticmethod
    def is_displayed(player: Player):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        projects = C.PROJECTS
        return {
            'projects': projects,
            'session_code': player.session.code,
            'group_id': player.group.id_in_subsession,
        }

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'MED' is the current condition
        return order[player.round_number - 1] == 'MED'

class FactoryDecision(Page):
    form_model = 'player'
    form_fields = ['factory_choice']

    @staticmethod
    def is_displayed(player: Player):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        factories = C.FACTORIES
        return {
            'factories': factories,
            'session_code': player.session.code,
            'group_id': player.group.id_in_subsession,
        }

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'EASY' is the current condition
        return order[player.round_number - 1] == 'EASY'

class CandidateDecision(Page):
    form_model = 'player'
    form_fields = ['candidate_choice']

    @staticmethod
    def is_displayed(player: Player):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        candidates = C.CANDIDATES
        return {
            'candidates': candidates,
            'session_code': player.session.code,
            'group_id': player.group.id_in_subsession,
        }

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'HARD' is the current condition
        return order[player.round_number - 1] == 'HARD'

class WaitForProjectInfo(WaitPage):
    form_model = 'player'
    title_text = "Please wait until all other team members are ready."
    body_text = "You will be redirected automatically."

class WaitForDecision(WaitPage):
    def after_all_players_arrive(group: Group):
        player = group.get_players()[0]  # alle Spieler haben dieselbe Reihenfolge
        condition = player.participant.hp_condition_order[player.round_number - 1]

        if condition == 'MED':
            set_winning_project(group)
        elif condition == 'LOW':
            set_winning_factory(group)
        elif condition == 'HIGH':
            set_winning_candidate(group)
        else:
            print(f"[Warnung] Unbekannte Bedingung: {condition}")

class Results(Page):
    def vars_for_template(player: Player):
        return {
            'payoff': player.player_payoff,
            'chosen_project': player.group.chosen_project,
        }

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

    def is_displayed(player: Player):
        return player.round_number == 1

class GameOverview(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Overview_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

    def is_displayed(player: Player):
        return player.round_number == 1

class Overview_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

    def is_displayed(player: Player):
        return player.round_number == 1

class Overview_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

    def is_displayed(player: Player):
        return player.round_number == 1

class GameGoal(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class ProjectInformation(Page):
    form_model = 'player'
    form_fields = ['task_load_time_project', 'task_finish_click_time_project','task_end_time_project']

    @staticmethod
    def is_displayed(player: Player):
        return True

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'MED' is the current condition
        return order[player.round_number - 1] == 'MED'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'role': player.player_role,
            'taskDuration': C.TASK_PREP_TIME_LIMIT,
        }

    @staticmethod
    def live_method(player: Player, data):
        if data.get("type") == "next_clicked":
            player.next_ready = True
            all_ready = all(p.next_ready for p in player.group.get_players())
            if all_ready:
                return {p.id_in_group: {"type": "go_to_next"} for p in player.group.get_players()}
            else:
                return {player.id_in_group: {"type": "waiting"}}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.next_ready = False

class FactoryInformation(Page):
    form_model = 'player'
    form_fields = ['task_load_time_project', 'task_finish_click_time_project','task_end_time_project']

    @staticmethod
    def is_displayed(player: Player):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'role': player.player_role,
            'taskDuration': C.TASK_PREP_TIME_LIMIT,
        }

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'EASY' is the current condition
        return order[player.round_number - 1] == 'EASY'

    @staticmethod
    def live_method(player: Player, data):
        if data.get("type") == "next_clicked":
            player.next_ready = True
            all_ready = all(p.next_ready for p in player.group.get_players())
            if all_ready:
                return {p.id_in_group: {"type": "go_to_next"} for p in player.group.get_players()}
            else:
                return {player.id_in_group: {"type": "waiting"}}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.next_ready = False

class CandidateInformation(Page):
    form_model = 'player'
    form_fields = ['task_load_time_project', 'task_finish_click_time_project','task_end_time_project']

    @staticmethod
    def is_displayed(player: Player):
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'role': player.player_role,
            'taskDuration': C.TASK_PREP_TIME_LIMIT,
        }

    def is_displayed(player: Player):
        order = player.participant.hp_condition_order
        # This page should appear when 'HARD' is the current condition
        return order[player.round_number - 1] == 'HARD'

    @staticmethod
    def live_method(player: Player, data):
        if data.get("type") == "next_clicked":
            player.next_ready = True
            all_ready = all(p.next_ready for p in player.group.get_players())
            if all_ready:
                return {p.id_in_group: {"type": "go_to_next"} for p in player.group.get_players()}
            else:
                return {player.id_in_group: {"type": "waiting"}}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.next_ready = False

def normalize(value, min_value, max_value, higher_is_better=True):
    """
    Normalize a value between 0 and 100, with option to invert for metrics where lower is better.
    """
    if value is None:
        return 0
    normalized = (value - min_value) / (max_value - min_value) * 100
    return normalized if higher_is_better else (100 - normalized)

def set_winning_project(group: Group):
    if group.subsession.round_number != 1:
        return

    projects = C.PROJECTS
    
    # Find min and max values for each metric
    profit_values = [p['profit'] for p in projects]
    env_impact_values = [p['env_impact'] for p in projects]
    market_demand_values = [p['market_demand'] for p in projects]
    salary_values = [p['salary_cost'] for p in projects]
    
    # Calculate normalized scores for each project
    for project in projects:
        # Normalize each metric (note higher_is_better=False for costs and environmental impact)
        profit_score = normalize(
            project['profit'], 
            min(profit_values), 
            max(profit_values), 
            higher_is_better=True
        )
        
        env_score = normalize(
            project['env_impact'], 
            min(env_impact_values), 
            max(env_impact_values), 
            higher_is_better=False  # Lower environmental impact is better
        )
        
        market_score = normalize(
            project['market_demand'], 
            min(market_demand_values), 
            max(market_demand_values), 
            higher_is_better=True
        )
        
        salary_score = normalize(
            project['salary_cost'], 
            min(salary_values), 
            max(salary_values), 
            higher_is_better=False  # Lower salary cost is better
        )
        
        # Calculate weighted benefit (adjust weights based on importance)
        project['benefit'] = (
            0.25 * profit_score +
            0.25 * env_score +
            0.25 * market_score +
            0.25 * salary_score
        )
    
    # Rest of the voting logic remains the same
    sorted_projects = sorted(projects, key=lambda x: x['benefit'], reverse=True)
    
    project_ranking = {
        sorted_projects[0]['name']: 15,  # Best project
        sorted_projects[1]['name']: 10,  # Second best
        sorted_projects[2]['name']: 5,   # Worst
    }
    
    # Determine the chosen project from players' choices
    votes = [p.project_choice for p in group.get_players() if p.project_choice]
    if votes:
        vote_count = {proj: votes.count(proj) for proj in set(votes)}
        winning_project = [proj for proj, count in vote_count.items() if count >= 3]
        
        if winning_project:
            group.chosen_project = winning_project[0]
            group.project_profit = project_ranking[group.chosen_project]
        else:
            group.chosen_project = "No consensus"
            group.project_profit = 0
    else:
        group.chosen_project = "No consensus"
        group.project_profit = 0
        
    # Update each player's payoff
    for player in group.get_players():
        player.player_payoff = group.project_profit

def set_winning_factory(group: Group):
    if group.subsession.round_number != 2:
        return

    factories = C.FACTORIES

    # Werte extrahieren
    construction_cost = [f['construction_cost'] for f in factories]
    energy_cost = [f['energy_cost'] for f in factories]

    # Scoring berechnen
    for factory in factories:
        build_score = normalize(factory['build_cost'], min(construction_cost), max(construction_cost), higher_is_better=False)
        energy_score = normalize(factory['energy_cost'], min(energy_cost), max(energy_cost), higher_is_better=False)
        factory['benefit'] = 0.5 * build_score + 0.5 * energy_score

    # Ranking
    sorted_factories = sorted(factories, key=lambda x: x['benefit'], reverse=True)
    factory_ranking = {
        sorted_factories[0]['name']: 15,
        sorted_factories[1]['name']: 5,
    }

    # Abstimmungsauswertung
    votes = [p.factory_choice for p in group.get_players() if p.factory_choice]
    if votes:
        vote_count = {f: votes.count(f) for f in set(votes)}
        winning_factory = [f for f, count in vote_count.items() if count >= 3]
        if winning_factory:
            group.chosen_factory = winning_factory[0]
            group.factory_points = factory_ranking.get(group.chosen_factory, 0)
        else:
            group.chosen_factory = "No consensus"
            group.factory_points = 0
    else:
        group.chosen_factory = "No consensus"
        group.factory_points = 0

    # Auszahlung
    for player in group.get_players():
        player.player_payoff = group.factory_points

def set_winning_candidate(group: Group):
    if group.subsession.round_number != 3:
        return

    candidates = C.CANDIDATES

    # Werte sammeln
    growth = [c['revenue_growth'] for c in candidates]
    margin = [c['profit_margin'] for c in candidates]
    satisfaction = [c['customer_satisfaction'] for c in candidates]
    headcount = [c['headcount'] for c in candidates]

    # Scoring
    for c in candidates:
        growth_score = normalize(c['revenue_growth'], min(growth), max(growth), higher_is_better=True)
        margin_score = normalize(c['profit_margin'], min(margin), max(margin), higher_is_better=True)
        satisfaction_score = normalize(c['customer_satisfaction'], min(satisfaction), max(satisfaction), higher_is_better=True)
        headcount_score = normalize(c['headcount'], min(headcount), max(headcount), higher_is_better=False)  # weniger = besser
        c['benefit'] = (
            0.25 * growth_score +
            0.25 * margin_score +
            0.25 * satisfaction_score +
            0.25 * headcount_score
        )

    # Ranking
    sorted_candidates = sorted(candidates, key=lambda x: x['benefit'], reverse=True)
    candidate_ranking = {
        sorted_candidates[0]['name']: 15,
        sorted_candidates[1]['name']: 5,
    }

    # Abstimmungsauswertung
    votes = [p.candidate_choice for p in group.get_players() if p.candidate_choice]
    if votes:
        vote_count = {f: votes.count(f) for f in set(votes)}
        winning_candidate = [f for f, count in vote_count.items() if count >= 3]
        if winning_candidate:
            group.chosen_candidate = winning_candidate[0]
            group.candidate_points = candidate_ranking.get(group.chosen_candidate, 0)
        else:
            group.chosen_candidate = "No consensus"
            group.candidate_points = 0
    else:
        group.chosen_candidate = "No consensus"
        group.candidate_points = 0

    # Auszahlung
    for player in group.get_players():
        player.player_payoff = group.candidate_points

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

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

page_sequence = [Introduction,
                 Overview_1, Overview_2, Overview_3,
                 RoleAssignment,
                 WaitForProjectInfo, ProjectInformation, FactoryInformation, CandidateInformation,
                 WaitForRoleAssignment,
                 Discussion,
                 ProjectDecision, FactoryDecision, CandidateDecision, WaitForDecision,
                 TaskSurvey, RestEyesOpen, TaskPhaseSurvey]



