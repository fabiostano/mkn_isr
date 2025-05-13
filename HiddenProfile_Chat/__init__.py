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

    # ----- FLOW ----- #
    fss01 = make_7p_likert_field('I felt just the right amount of challenge.')
    fss02 = make_7p_likert_field('My thoughts/activities ran fluidly and smoothly.')
    fss03 = make_7p_likert_field('I didn’t notice time passing.')
    fss04 = make_7p_likert_field('I had no difficulty concentrating.')
    fss05 = make_7p_likert_field('My mind was completely clear.')
    fss07 = make_7p_likert_field('The right thoughts/movements occurred of their own accord.')
    fss10 = make_7p_likert_field('I was completely involved in the task.')
    fss06 = make_7p_likert_field('I was totally absorbed in what I was doing.')
    fss08 = make_7p_likert_field('I knew what I had to do each step of the way.')
    fss09 = make_7p_likert_field('I felt that I had everything under control.')

    # ----- TLX ------
    # "Please indicate on each scale at the point that best indicates your experience of the last few minutes."
    tlx_single = models.IntegerField(
        # Low | High
        # label = "How much mental and perceptual activity was required (e.g. thinking, deciding, calculating, remembering, looking, searching, etc)? Was the task easy or demanding, simple or complex, exacting or forgiving?",
        min=0,
        max=21
    )

    difficulty = make_7p_likert_field('How difficult was this task for you?')

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
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['fss01', 'fss02', 'fss03', 'fss04', 'fss05', 'fss06', 'fss07', 'fss08', 'fss09', 'fss10']
        random.shuffle(flow_fields)
        all_fields = flow_fields + ['tlx_single', 'difficulty']
        return all_fields

page_sequence = [Introduction,
                 Overview_1, Overview_2, Overview_3,
                 RoleAssignment, ProjectInformation,
                 # DiscussionPreface, # This is the sentiment analysis explanation - we don't want that...
                 WaitForRoleAssignment,
                 Discussion,
                 Decision, WaitForDecision, Results,
                 TaskSurvey]
