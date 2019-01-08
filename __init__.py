from mycroft import MycroftSkill, intent_file_handler
import requests


class Showhome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        ip = self.settings['ip']
        port = self.settings['port']
        self.base_url = 'http://'+ip+':'+str(port)

    @intent_file_handler('eos.apply.intent')
    def handle_eos(self, message):
        loc = message.data['loc']
        state = message.data['state']

        url = self.base_url+'/eos/group/apply_preset/label'

        request = requests.put(url, data={'loc': loc, 'state': state})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})

    @intent_file_handler('x32.send.intent')
    def handle_x32_on(self, message):
        src = message.data['src']
        dest = message.data['dest']

        url = self.base_url+'/x32/ch/on/label'

        request = requests.put(url, data={'src': src, 'dest': dest})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})

    @intent_file_handler('x32.stop.intent')
    def handle_x32_off(self, message):
        src = message.data['src']
        dest = message.data['dest']

        url = self.base_url+'/x32/ch/off/label'

        request = requests.put(url, data={'src': src, 'dest': dest})

        if request.text != 'null':
            self.speak_dialog('showhome.error', {'text': request.text})


def create_skill():
    return Showhome()

