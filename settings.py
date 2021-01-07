from os import environ

SESSION_CONFIGS = [
    # dict(
    #     name='noa_intro',
    #     display_name="NoA Intro",
    #     num_demo_participants=2,
    #     app_sequence=['noa_intro'],
    # ),
    # dict(
    #     name='noa_room1',
    #     display_name="NoA Room1",
    #     num_demo_participants=2,
    #     app_sequence=['noa_room1'],
    # ),
    # dict(
    #     name='noa_room1_plus_feedback',
    #     display_name="NoA Room1 + Feedback",
    #     num_demo_participants=2,
    #     app_sequence=['noa_room1', 'noa_room1_feedback'],
    # ),
    # dict(
    #     name='noa_room2',
    #     display_name="NoA Room2",
    #     num_demo_participants=2,
    #     app_sequence=['noa_room2'],
    # ),
    # dict(
    #     name='noa_room2_plus_feedback',
    #     display_name="NoA Room2 + Feedback",
    #     num_demo_participants=2,
    #     app_sequence=['noa_room2', 'noa_room2_feedback'],
    # ),
    # dict(
    #     name='noa_rooms_plus_feedback',
    #     display_name="NoA Room 1 + Feedback, Room 2 + Feedback",
    #     num_demo_participants=4,
    #     app_sequence=['noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback'],
    # ),
    # dict(
    #     name='noa_outro',
    #     display_name="NoA Outro",
    #     num_demo_participants=2,
    #     app_sequence=['noa_outro'],
    # ),
    dict(
        name='noa_complete_RA',
        display_name="NoA Complete RA",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='RA'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_AA',
        display_name="NoA Complete AA",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='AA'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_CC_RA',
        display_name="NoA Complete CC_RA",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='CC_RA'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_CC_AA',
        display_name="NoA Complete CC_AA",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='CC_AA'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_RA_NC',
        display_name="NoA Complete RA_NC",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='RA_NC'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_AA_NC',
        display_name="NoA Complete AA_NC",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='AA_NC'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_RA_NC_WTP',
        display_name="NoA Complete RA_NC_WTP",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='RA_NC_WTP'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_AA_NC_WTP',
        display_name="NoA Complete AA_NC_WTP",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='AA_NC_WTP'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_CC_RA_NC_WTP',
        display_name="NoA Complete CC_RA_NC_WTP",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='CC_RA_NC_WTP'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_complete_CC_AA_NC_WTP',
        display_name="NoA Complete CC_AA_NC_WTP",
        num_demo_participants=4,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        # treatment='CC_AA_NC_WTP'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.50,
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'jdklj$t$k95rw)p!rss9q6swd5%^q&!g2o4de9f15_93_v^-o-'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
