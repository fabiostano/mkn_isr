from otree.api import *
c = cu
doc = ''

class C(BaseConstants):
    name_in_url = 'Headphones_Shared'

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

class HeadphonesSetup(Page):
    form_model = 'player'

class RecordingSetup(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {"token": player.participant.code}

class RecordingStop(Page):
    form_model = 'player'

page_sequence = [HeadphonesSetup, RecordingSetup, RecordingStop]