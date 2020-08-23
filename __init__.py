from mycroft import MycroftSkill, intent_file_handler
import requests


class GestanteMaisAtivaMetgest(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('metgest.ativa.mais.gestante.intent')
	def handle_metgest_ativa_mais_gestante(self, message):

		ipAPI = 'http://177.21.53.138:3000'


		payload = {'user':'publico','password':'123'}
		getToken = requests.post(ipAPI + "/login", data=payload)


		myToken = getToken.content;
		headers = {'x-access-token': myToken}

		r = requests.get(ipAPI + '/metgest/mais-ativa', headers=headers)

		if r.status_code != 200 or len(r.json()) == 0:
			self.speak('Ocorreu algum problema ao me conectar ao servidor de dados. Pode ser, também, que as gestantes não tenham registrado atividades na semana atual. Por favor, verifique as credenciais e tente novamente.')

		else:
			result = r.json()[0]
			result['cpf_gestante'] = " ".join(result['cpf_gestante'])

			result['cpf_gestante'] = result['cpf_gestante'].replace(".", ", ponto, ")
			result['cpf_gestante'] = result['cpf_gestante'].replace("-", ", traço, ")

			self.speak_dialog('metgest.ativa.mais.gestante', data=result)


def create_skill():
	return GestanteMaisAtivaMetgest()

