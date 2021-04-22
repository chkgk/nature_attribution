from os import environ

SESSION_CONFIGS = [
    dict(
        name='noa_complete_RA',
        display_name="NoA Complete Baseline",
        num_demo_participants=8,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='BL',  # BL, IM, FI
        max_pay=3,  # x+y
        red_balls=40,  # p=0.4
        green_balls=60,
        announce_q=True
    ),
    dict(
        name='noa_complete_RA_NC_WTP1',
        display_name="NoA Complete Interim",
        num_demo_participants=8,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='IM',  # BL, IM, FI
        max_pay=3,  # x+y
        red_balls=40,  # p=0.6
        green_balls=60,
        announce_q=True
    ),
    dict(
        name='noa_complete_RA_NC_WTP2',
        display_name="NoA Complete Final",
        num_demo_participants=8,
        app_sequence=['noa_intro', 'noa_room1', 'noa_room1_feedback', 'noa_room2', 'noa_room2_feedback', 'noa_outro'],
        treatment='FI',  # BL, IM, FI
        max_pay=3,  # x+y
        red_balls=40,  # p=0.6
        green_balls=60,
        announce_q=True
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.80,
    'doc': "",
    'mturk_hit_settings': dict(
        keywords='bonus, study, research, decision making',
        title='Short Research Study (ca. 10min)',
        description='Participate in a game and a short survey. Please note that the task is to be completed within 10-15 minutes as you are matched with a co-player.',
        frame_height=700,
        template='noa_intro/mturk_template.html',
        minutes_allotted_per_assignment=20,
        expiration_hours=3,
        qualification_requirements=[
            {
                'QualificationTypeId': '00000000000000000071',
                'Comparator': 'EqualTo',
                'LocaleValues': [{'Country': "US"}]
            },
            # qualification granted by Christian's runs
            {
                'QualificationTypeId': '3X4G950TG9JM27SOMLGT6VJ1IU8P1C',
                'Comparator': 'DoesNotExist'
            },
            # qualification granted by Florian's Experiments
            {
                'QualificationTypeId': "3DA2M59FDW8FXK3OTJT76I16UG0RXG",
                'Comparator': "DoesNotExist",
            }
        ],
        grant_qualification_id='3X4G950TG9JM27SOMLGT6VJ1IU8P1C',  # to prevent retakes
    )
}

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

# AWS
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
