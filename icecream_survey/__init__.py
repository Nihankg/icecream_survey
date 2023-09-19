from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'icecream_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(
        label='What is your name?'
    )
    age = models.IntegerField(
        label='What is your age?',
        min=13,
        max=125
    )
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Non-binary', 'Non-binary']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    Ice_cream_Q = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Do you like ice cream?',
        widget=widgets.RadioSelect,
    )
    Pizza_Q = models.StringField(
        label='''
        Do You like pizza?
        '''
    )
    Pizza_type_Q = models.StringField(
        label='''
        What is your favorite type of pizza?
        '''
    )
# PAGES


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender']


class RealQPage(Page):
    form_model = 'player'
    form_fields = ['Ice_cream_Q', 'Pizza_Q', 'Pizza_type_Q']


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        result = player.Pizza_type_Q
        if result.lower() == "pepperoni":
            return {'result': "Mine too!"}
        else:
            return {'result': 'Mine is pepperoni!'}


page_sequence = [MyPage, RealQPage, Results]
