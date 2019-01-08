from mycroft import MycroftSkill, intent_file_handler
import requests


class Showhome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('showhome.intent')
    def handle_showhome(self, message):
        loc = message.data['loc']
        state = message.data['state']
        ip = self.settings['ip']
        port = self.settings['port']

        url = 'http://'+ip+':'+str(port)+'/eos/group/apply_preset/label'

        request = requests.put(url, data={'loc': loc, 'state': state})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})


def create_skill():
    return Showhome()

