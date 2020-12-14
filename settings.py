from os import environ

SESSION_CONFIGS = [
    dict(
        name='noa_intro',
        display_name="NoA Intro",
        num_demo_participants=2,
        app_sequence=['noa_intro'],
        treatment='RA'  # RA, AA, CC_RA, CC_AA, RA_NC, AA_NC, RA_NC_WTP, AA_NC_WTP, CC_RA_NC_WTP, CC_AA_NC_WTP
    ),
    dict(
        name='noa_room1',
        display_name="NoA Room1",
        num_demo_participants=2,
        app_sequence=['noa_room1'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'jdklj$t$k95rw)p!rss9q6swd5%^q&!g2o4de9f15_93_v^-o-'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
