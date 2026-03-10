from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=15)

SESSION_CONFIGS = [
                   # dict(name='dev', num_demo_participants=3, app_sequence=['Outro']),
                   dict(name='Math_Chat_Jitsi', num_demo_participants=3, app_sequence=['Intro', 'mathChat', 'mathJitsi', 'Outro']),
                   dict(name='Math_Jitsi_Chat', num_demo_participants=3, app_sequence=['Intro', 'mathJitsi', 'mathChat', 'Outro'])
                  ]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ["condition_order",
                      "calibrated_difficulty_chat", "calibrated_difficulty_jitsi",
                      "selected_difficulty_chat", "selected_difficulty_jitsi",
                      "hp_condition_order"]
SESSION_FIELDS = []
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'kd2lab4ever'

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

DEBUG = False

OTREE_AUTH_LEVEL = 'STUDY'

OTREE_PRODUCTION = False