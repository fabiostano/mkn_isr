import random
from otree.api import *
c = cu
doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'mathChat'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4
    TASK_TIME_LIMIT = 3 * 60 # Task Time
    TRIAL_TIME = 28
    BREAK_TIME = 4
    MIN_DIFFICULTY = 1  # Start difficulty level
    MAX_DIFFICULTY = 16  # Highest difficulty level

    COLORMAP = ['lightcoral', 'lightgreen', 'lightblue']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    color = models.StringField(initial="none")
    action_log = models.LongStringField(initial="")
    answer_history = models.StringField(initial="")
    level_history = models.StringField(initial="")
    chat_log = models.LongStringField(initial="")

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

class Explanation(Page):
    form_model = 'player'
    def is_displayed(player: Player):
        return player.round_number == 1

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions']

class BeforeTask(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "round_number": player.round_number
        }

    def is_displayed(player: Player):
        return player.round_number < 4

    def before_next_page(player, timeout_happened):
        player.color = C.COLORMAP[player.id_in_group-1]

class Wait_Page(WaitPage):
    form_model = 'player'
    title_text = "Please wait until all other team members are ready."
    body_text = "You will be redirected automatically."

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

class Task(Page):
    form_model = 'player'
    form_fields = ['action_log', 'task_load_time', 'level_history', 'chat_log']
    # timeout_seconds = 5

    # @staticmethod
    # def before_next_page(player, timeout_happened):
    #     if timeout_happened:
    #         print("Timeout should have happened now...")

    def vars_for_template(player):
        return dict(
            level = 10,
            min_level = C.MIN_DIFFICULTY,
            max_level = C.MAX_DIFFICULTY,
            difficulty = "Optimal",
            id = player.id_in_group,
            taskDuration = C.TASK_TIME_LIMIT,
            trialDuration=C.TRIAL_TIME,
            breakDuration=C.BREAK_TIME,
            color = C.COLORMAP[player.id_in_group-1]
        )

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
            if selected_id in active_selections:
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

        elif info_type == "timeUp":
            return {p.id_in_group: data for p in group.get_players()}

        # Handle incoming chat messages
        elif data["info_type"] == "chat_message":
            return {p.id_in_group: data for p in group.get_players()}

        return {}

page_sequence = [BeforeTask, Task, TaskSurvey]