from mycroft import MycroftSkill, intent_file_handler


class GestanteMaisAtivaMetgest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('metgest.ativa.mais.gestante.intent')
    def handle_metgest_ativa_mais_gestante(self, message):
        self.speak_dialog('metgest.ativa.mais.gestante')


def create_skill():
    return GestanteMaisAtivaMetgest()

