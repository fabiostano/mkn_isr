import random
from otree.api import *
c = cu
doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'mathJitsi'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4
    TASK_TIME_LIMIT = 60 * 5  # Task Time
    TRIAL_TIME = 28
    BREAK_TIME = 4  # 4 seconds break
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
    load_time = models.IntegerField()

    # ----- Task Functionality ----- #
    team_role = models.StringField()

    # ----- Timestamps ----- #
    task_load_time = models.StringField(blank=True)
    rest_load_time = models.StringField(blank=True)



    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                   widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                  widget=widgets.RadioSelectHorizontal)


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

class TaskQuestionnaire(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        all_fields = ['pleasure', 'arousal']

        flow_fields = ['sfss1', 'sfss2', 'sfss3', 'sfss4', 'sfss5', 'sfss6', 'sfss7', 'sfss8', 'sfss9', 'sdb1', 'sdb2', 'sdb3']
        random.shuffle(flow_fields)
        all_fields += flow_fields

        mw_fields = ['mws1', 'mws2', 'mws3', 'mws4', 'mws5', 'mws6']
        random.shuffle(mw_fields)
        all_fields += mw_fields

        all_fields += ['tlx', 'control_text_interest', 'control_music_liking', 'control_music_turnoff']

        return all_fields

class Task(Page):
    form_model = 'player'
    form_fields = ['action_log', 'load_time']

    def vars_for_template(player):
        return dict(
            level = 5,
            difficulty = "Optimal",
            id = player.id_in_group,
            timeout_seconds = C.TASK_TIME_LIMIT,
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

        return {}


page_sequence = [Task]