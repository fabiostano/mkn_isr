from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=15)
SESSION_CONFIGS = [dict(name='math_jitsi', num_demo_participants=3, app_sequence=['mathJitsi']),
                   dict(name='math_chat', num_demo_participants=3, app_sequence=['mathChat']),
                   dict(name='hidden_profile', num_demo_participants=3, app_sequence=['Hidden_profile'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'kd2lab4ever'

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

DEBUG = True

OTREE_AUTH_LEVEL = 'STUDY'

OTREE_PRODUCTION = False