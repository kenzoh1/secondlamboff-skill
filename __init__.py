from mycroft import MycroftSkill, intent_file_handler


class Secondlamboff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('secondlamboff.intent')
    def handle_secondlamboff(self, message):
        self.speak_dialog('secondlamboff')


def create_skill():
    return Secondlamboff()

