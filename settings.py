from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=15)

SESSION_CONFIGS = [
                   dict(name='Chat_Math_HP', num_demo_participants=3, app_sequence=['Intro','mathChat', 'HiddenProfile_Chat', 'Outro']),
                   dict(name='Chat_HP_Math', num_demo_participants=3, app_sequence=['Intro', 'HiddenProfile_Chat', 'mathChat', 'Outro']),
                   dict(name='Jitsi_Math_HP', num_demo_participants=3, app_sequence=['Intro','mathJitsi', 'HiddenProfile_Jitsi', 'Outro']),
                   dict(name='Jitsi_HP_Math', num_demo_participants=9, app_sequence=['Intro', 'HiddenProfile_Jitsi', 'mathJitsi', 'Outro']),
                   dict(name='MathJitsiTest', num_demo_participants=3, app_sequence=['mathJitsi']),
                   dict(name='HPTest1', num_demo_participants=3, app_sequence=['HiddenProfile_Chat'])
                   ]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ["condition_order", "calibrated_difficulty", "selected_difficulty"]
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