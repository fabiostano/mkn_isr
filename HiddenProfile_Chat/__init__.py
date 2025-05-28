from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'HiddenProfile_Chat'
    PLAYERS_PER_GROUP = 3  # CSO, CHRO, CMO, CFO
    NUM_ROUNDS = 1
    BASE_PAYOUT = 200
    TEAM_BONUS = 30
    DEPT_BONUS = 50
    MAX_INFO_SHARING_BONUS = 70
    TASK_TIME_LIMIT = 10 # 3 * 60  # Task Time

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']

    PROJECTS = [
        {'name': 'Project A: E-Track', 'profit': 4, 'env_impact': 60, 'market_demand': 70000, 'salary_cost': 50000,
         'criteria': 'environmental'},
        {'name': 'Project B: T-Sphere', 'profit': 3, 'env_impact': 95, 'market_demand': 80000, 'salary_cost': 60000,
         'criteria': 'salary'},
        {'name': 'Project C: M-Pulse', 'profit': 2, 'env_impact': 40, 'market_demand': 60000, 'salary_cost': 55000,
         'criteria': 'market'}
    ]

    ROLES = ['Chief Sustainability Officer', 'Chief Human Resources Officer', 'Chief Marketing Officer',
             'Chief Financial Officer']
    TIMEOUT_SECONDS = 7 * 60  # 7 minutes in seconds

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    chosen_project = models.StringField(initial=None)
    project_profit = models.CurrencyField(initial=0)

class Player(BasePlayer):
    color = models.StringField(initial="none")
    chat_log = models.LongStringField(initial="")
    player_role = models.StringField()
    personal_interest = models.StringField()
    shared_info = models.StringField()
    project_choice = models.StringField()
    player_payoff = models.CurrencyField(initial=C.BASE_PAYOUT)

    # ----- Timestamps ----- #
    task_load_time = models.StringField(blank=True)
    # rest_load_time = models.StringField(blank=True)

    def make_7p_likert_field(label):
        return models.IntegerField(
            label=label,
            choices=[1, 2, 3, 4, 5, 6, 7],
            widget=widgets.RadioSelectHorizontal
        )

    ### Task Round Survey

     # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

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

    fi1 = make_7p_likert_field('I would love to do this task again.')
    fi2 = make_7p_likert_field('I was thrilled.')
    fi3 = make_7p_likert_field('The task demands were well matched to my ability.')

    # ----- Challenge Skill Balance ----- #
    csb1 = make_7p_likert_field('Compared to all other activities which I partake in, the difficulty of this one is ...')
    csb2 = make_7p_likert_field('I think that my competence in this area is ...')
    csb3 = make_7p_likert_field('For me personally, the task demands were ...')

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

    # ----- Subjective Concentration ----- #
    sc1 = make_7p_likert_field('How well were you concentrating during the task?')
    sc2 = make_7p_likert_field('How hard was it to concentrate during the task?')

    # ----- Social Evaluative Threat ----- #
    set1 = make_7p_likert_field('I was afraid that my performance on the task was being evaluated by others.')
    set2 = make_7p_likert_field('I was afraid that my task performance will be assessed by others at a later time.')

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
    ccsb2 = make_7p_likert_field('I think that our team’s competence in this area is ...')
    ccsb3 = make_7p_likert_field('For us as a team, the task demands were ...')

    # ----- Emotional Contagion ----- #
    ec1 = make_7p_likert_field('How much were you on the same wavelength with your team?')

    # ----- Emotional Synchrony ----- #
    es1 = make_7p_likert_field('We felt stronger emotions than those we normally feel.')
    es2 = make_7p_likert_field('We felt that we were one.')
    es3 = make_7p_likert_field('We felt a strong shared emotion.')
    es4 = make_7p_likert_field('We felt really united, almost melted into one.')
    es5 = make_7p_likert_field('What we were as a group was more important than what we were as individuals.')
    es6 = make_7p_likert_field('We felt more intense emotions because we all went through the same experience.')

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

     # ----- Identity Fusion ----- #
    fusion = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Perceived Social Presence ----- #
    psp1 = make_7p_likert_field('There was a sense of human contact during the group work.')
    psp2 = make_7p_likert_field('There was a sense of personalness during the group work.')
    psp3 = make_7p_likert_field('There was a sense of sociability during the group work.')
    psp4 = make_7p_likert_field('There was a sense of human warmth during the group work.')
    psp5 = make_7p_likert_field('There was a sense of human sensitivity during the group work.')

def creating_session(subsession: Subsession):
    import random
    roles = C.ROLES[:]
    random.shuffle(roles)

    for p in subsession.get_players():
        p.player_role = roles.pop()

        if p.player_role == 'Chief Sustainability Officer':
            p.personal_interest = 'Env Impact'
            p.shared_info = 'Market Demand'
        elif p.player_role == 'Chief Human Resources Officer':
            p.personal_interest = 'Salary Cost'
            p.shared_info = 'None'
        elif p.player_role == 'Chief Marketing Officer':
            p.personal_interest = 'Market Demand'
            p.shared_info = 'Env Impact'
        elif p.player_role == 'Chief Financial Officer':
            p.personal_interest = 'Profit'
            p.shared_info = 'None'

class RoleAssignment(Page):
    def vars_for_template(player: Player):
        # Get the project information based on the player's role
        project_info = []  # TODO make this general and use it in project information page!!!

        for project in C.PROJECTS:
            if player.player_role == 'Chief Sustainability Officer':
                project_info.append({
                    'name': project['name'],
                    'market_demand': project['market_demand'],
                    'env_impact': project['env_impact']
                })
            elif player.player_role == 'Chief Human Resources Officer':
                project_info.append({
                    'name': project['name'],
                    'salary_cost': project['salary_cost']
                })
            elif player.player_role == 'Chief Marketing Officer':
                project_info.append({
                    'name': project['name'],
                    'market_demand': project['market_demand'],
                    'env_impact': project['env_impact']
                })
            elif player.player_role == 'Chief Financial Officer':
                project_info.append({
                    'name': project['name'],
                    'profit': project['profit']
                })

        return {
            'role': player.player_role,
            'personal_interest': player.personal_interest,
            'shared_info': player.shared_info,
            'project_info': project_info  # Pass the project info to the template
        }

class WaitForRoleAssignment(WaitPage):
    def is_displayed(self):
        # This ensures that all players must pass through this wait page
        return True

    def before_next_page(self):
        pass

class DiscussionPreface(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Discussion(Page):
    form_model = 'player'
    form_fields = ['task_load_time', 'chat_log']

    def vars_for_template(player):
        return dict(
            id = player.id_in_group,
            color=C.COLORMAP[player.id_in_group - 1],
            taskDuration=C.TASK_TIME_LIMIT
        )

    @staticmethod
    def live_method(player, data):
        group = player.group
        info_type = data.get("info_type")

        # Get the group-level shared dict to track selections
        if not group.session.vars.get("active_selections"):
            group.session.vars["active_selections"] = {}  # { "sol_1": "lightblue", "sol_2": "lightgreen", ... }

        active_selections = group.session.vars["active_selections"]

        # Handle incoming chat messages
        if data["info_type"] == "chat_message":
            return {p.id_in_group: data for p in group.get_players()}

        return {}

class Decision(Page):
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

class WaitForDecision(WaitPage):
    after_all_players_arrive = 'set_winning_project'

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

class GameOverview(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Overview_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Overview_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class Overview_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class GameGoal(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

class ProjectInformation(Page):
    @staticmethod
    def is_displayed(player: Player):
        return True

    def vars_for_template(player: Player):
        return {
            'role': player.player_role,
            'project_info': C.PROJECTS
        }

def normalize(value, min_value, max_value, higher_is_better=True):
    """
    Normalize a value between 0 and 100, with option to invert for metrics where lower is better.
    """
    if value is None:
        return 0
    normalized = (value - min_value) / (max_value - min_value) * 100
    return normalized if higher_is_better else (100 - normalized)

def set_winning_project(group: Group):
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
        fi_fields = ['fi1', 'fi2', 'fi3']
        random.shuffle(fi_fields)
        all_fields += fi_fields
        csb_fields = ['csb1', 'csb2', 'csb3']
        random.shuffle(csb_fields)
        all_fields += csb_fields
        is_fields = ['is1', 'is2', 'is3', 'is4', 'is5']
        random.shuffle(is_fields)
        all_fields += is_fields
        ptp_fields = ['ptp1', 'ptp2', 'ptp3']
        random.shuffle(ptp_fields)
        all_fields += ptp_fields
        sc_fields = ['sc1', 'sc2']
        random.shuffle(sc_fields)
        all_fields += sc_fields
        set_fields = ['set1', 'set2']
        random.shuffle(set_fields)
        all_fields += set_fields
        san_fields = ['san1', 'san2', 'san3']
        random.shuffle(san_fields)
        all_fields += san_fields
        tm_fields = ['tm1', 'tm2', 'tm3']
        random.shuffle(tm_fields)
        all_fields += tm_fields
        ccsb_fields = ['ccsb1', 'ccsb2', 'ccsb3']
        random.shuffle(ccsb_fields)
        all_fields += ccsb_fields
        ec_fields = ['ec1']
        all_fields += ec_fields
        es_fields = ['es1', 'es2', 'es3', 'es4', 'es5', 'es6']
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

    @staticmethod
    def get_form_fields(player: Player):
        import random
        all_fields = []
        ti_fields = ['ti1', 'ti2', 'ti3']
        random.shuffle(ti_fields)
        all_fields += ti_fields
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
        psp_fields = ['psp1', 'psp2', 'psp3', 'psp4', 'psp5']
        random.shuffle(psp_fields)
        all_fields += psp_fields
        fusion_fields = ['fusion']
        all_fields += fusion_fields
        return all_fields

    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

page_sequence = [Introduction,
                 Overview_1, Overview_2, Overview_3,
                 RoleAssignment, ProjectInformation,
                 # DiscussionPreface, # This is the sentiment analysis explanation - we don't want that...
                 WaitForRoleAssignment,
                 Discussion,
                 Decision, WaitForDecision, Results,
                 TaskSurvey, TaskPhaseSurvey]
