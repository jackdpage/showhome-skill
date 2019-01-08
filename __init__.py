from mycroft import MycroftSkill, intent_file_handler


class Showhome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('showhome.intent')
    def handle_showhome(self, message):
        self.speak_dialog('showhome')


def create_skill():
    return Showhome()

