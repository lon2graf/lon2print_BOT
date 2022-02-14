import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config

vk_session = vk_api.VkApi(token = config.MAIN_TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
main_id = config.MAIN_ID



def message_sender(id, text):
	vk.messages.send(user_id = id, message = text, random_id = 0)


for event in longpoll.listen():

	if event.type == VkEventType.MESSAGE_NEW and event.to_me:

		msg = event.text

		id = event.user_id

		if (msg == "начать") or (msg == "Начать"):
			message_sender(id, "Привет, я бот - твой персональный помощник. Я бот, который создан специально для того, чтобы помогать администратору группы vk.com/lon2print . Моя функциональность заключается в том, что быстро проконсультировать пользователей и получившийся заказ немедленно отправить администаратору, который ознакомится с вашим заказом и обслужит вас(по красоте конечно). Для большей информации пиши !помоги")

		if (msg == "!гарантия_безопасности"):
			message_sender(id, "Чтобы убедиться в том, что бот безопасен и безобиден, и в действительности выполняет то, что написано в описании, достаточно посмотреть исходный код бота по ссылке - https://github.com/lon2graf/lon2print_BOT")


		if (msg == "!помоги"):
			message_sender(id, "Команды, которые поддерживает бот :")
			message_sender(id, "!помоги - получение некоторой помощи по боту.")
			message_sender(id, "!гарантия_безопасности - бот доказывает, что в нем нет ничего опасного.")
