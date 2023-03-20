from mycroft import MycroftSkill, intent_file_handler


class Mynametwo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mynametwo.intent')
    def handle_mynametwo(self, message):
        self.speak_dialog('mynametwo')


def create_skill():
    return Mynametwo()

