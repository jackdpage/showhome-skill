from mycroft import MycroftSkill, intent_handler
import requests


class Showhome(MycroftSkill):

    def initialize(self):
        ip = self.settings.get('ip')
        port = self.settings.get('port')
        self.base_url = 'http://'+ip+':'+str(port)

    @intent_handler('eos.apply.intent')
    def handle_eos(self, message):
        loc = message.data['loc']
        state = message.data['state']

        url = self.base_url+'/eos/group/apply_preset/label'

        request = requests.put(url, data={'loc': loc, 'state': state})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})

    @intent_handler('x32.send.intent')
    def handle_x32_on(self, message):
        src = message.data['src']
        dest = message.data['dest']

        url = self.base_url+'/x32/ch/on/label'

        request = requests.put(url, data={'src': src, 'dest': dest})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})

    @intent_handler('x32.stop.intent')
    def handle_x32_off(self, message):
        src = message.data['src']
        dest = message.data['dest']

        url = self.base_url+'/x32/ch/off/label'

        request = requests.put(url, data={'src': src, 'dest': dest})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})


def create_skill():
    return Showhome()

