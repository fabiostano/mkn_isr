from otree.api import models

def rest_fields():
    return dict(
        rest_actions_eo=models.StringField(label=""),
        rest_actions_ec=models.StringField(label=""),
    )

def math_fields():
    return dict(
        math_actions=models.LongStringField(label=''),
        currRound=models.StringField(blank=True),
    )

def tlx_fat_fields():
    return dict(
        mr_mood=models.IntegerField(min=1, max=100),
        mr_sleepy=models.IntegerField(min=1, max=100),
        mr_motivy=models.IntegerField(min=1, max=100),
        mf_single=models.IntegerField(min=1, max=100),
        tlx_single=models.IntegerField(min=0, max=21),
    )

class MathConstants:
    players_per_group = None
    math_levels = [0, 4]
    task_duration_ms = 120 * 1000
    trial_duration_ms = 20 * 1000
    num_rounds = 2 + 2