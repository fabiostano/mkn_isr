from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=15)

SESSION_CONFIGS = [
                   # dict(name='dev', num_demo_participants=3, app_sequence=['Outro']),
                   # dict(name='Math_Chat_Jitsi', num_demo_participants=3, app_sequence=['Intro', 'mathChat', 'mathJitsi', 'Outro']),
                   # dict(name='Math_Jitsi_Chat', num_demo_participants=3, app_sequence=['Intro', 'mathJitsi', 'mathChat', 'Outro'])
                   dict(name='Integrated', num_demo_participants=1, app_sequence=['DeviceComp_Intro', 'DeviceComp_ExG', 'DeviceComp_Smart', 'DeviceComp_Waves',
                                                                                  'Intro',
                                                                                  'Block1_Home_Start', 'Block1_Home_End',
                                                                                  'Block2_Outdoor_Start', 'Block2_Outdoor_End',
                                                                                  'Block3_Meeting_Start', 'mathJitsi',
                                                                                  'Outro'
                                                                                  ])
                  #  dict(name='Devices_Comparison', num_demo_participants=1, app_sequence=['DeviceComp_Intro', 'DeviceComp_ExG', 'DeviceComp_Smart', 'DeviceComp_Waves']),
                  #  dict(name='Main_Study', num_demo_participants=3, app_sequence=['Intro',
                  #                                                                 'Block1_Home_Start', 'Block1_Home_End',
                  #                                                                 'Block2_Outdoor_Start', 'Block2_Outdoor_End',
                  #                                                                 'Block3_Meeting_Start', 'mathJitsi',
                  #                                                                 'Outro'])
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
ROOMS = [
    dict(
        name='study',
        display_name='Two-part study',
        participant_label_file='_rooms/study.txt',
        use_secure_urls=True,
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'kd2lab4ever'

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

DEBUG = False

OTREE_AUTH_LEVEL = 'STUDY'

OTREE_PRODUCTION = False