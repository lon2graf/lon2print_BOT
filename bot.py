import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config


def message_sender(id, text):
	vk.messages.send(user_id = id, message = text, random_id = 0)

def start_send_1():
	message_sender(id, "Привет, я бот - твой персональный помощник. Я бот, который создан специально для того, чтобы помогать администратору группы vk.com/lon2print . Моя функциональность заключается в том, что быстро проконсультировать пользователей и получившийся заказ немедленно отправить администаратору, который ознакомится с вашим заказом и обслужит вас(по красоте конечно). Для большей информации пиши !помоги")

def send_help_2():
	message_sender(id, "Команды, которые поддерживает бот :")
	message_sender(id, "!помоги - получение некоторой помощи по боту.")
	message_sender(id, "!гарантия_безопасности - бот доказывает, что в нем нет ничего опасного.")

def send_safety_3():
	message_sender(id, "Чтобы убедиться в том, что бот безопасен и безобиден, и в действительности выполняет то, что написано в описании, достаточно посмотреть исходный код бота по ссылке - https://github.com/lon2graf/lon2print_BOT")

def zakaz_yes_4():
	zakaz_get_type_5()




def zakaz_get_type_5():
	message_sender(id, "Напиши пожалуйста тип заказа(1,2,3,):\n1.Печать 2.Сканирование 3. Ксерокопия\nПросто напиши цифру")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				break
	try:
		if (int(msg) <= 0) or (int(msg) > 3):
			message_sender(id,"Напиши пожалуйста цифру от 1 до 3")
			zakaz_get_type_5()
	except:
		message_sender(id,"Напиши так, как я сказал, пожалуйста")
		zakaz_get_type_5()

	global type_zk
	if (int(msg) == 1):
		type_zk = "\nТип заказа 1.Печать"
		zakaz_gettype_print()

	if (int(msg) == 2):
		type_zk = "\nТип заказа 2.Сканирование"
		get_somethingelse()

	if (int(msg) == 3):
		type_zk = "\nТип заказа 3.Ксерокопия"
		get_somethingelse()

	return type_zk


def zakaz_gettype_print():
	message_sender(id, "Напиши пожалуйста тип печати(1,2,):\n1.Односторонняя 2.Двухстороняя\nПросто напиши цифру")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				break
	try:
		if (int(msg) <= 0) or (int(msg) > 2):
			message_sender(id,"Напиши пожалуйста цифру либо 1 либо 2")
			zakaz_gettype_print()
	except:
		message_sender(id,"Напиши так, как я сказал, пожалуйста")
		zakaz_gettype_print()

	global type_pr
	if(int(msg) == 1):
		type_pr =  "\nПечать Односторонняя\nКол-во страниц "
		get_k_str()
		return type_pr
	if(int(msg) == 2):
		type_pr =  "\nПечать Двухстороняя\nКол-во страниц "
		get_k_str()
		return type_pr




def get_k_str():
	message_sender(id, "Напиши пожалуйста количество страниц необходимых для печати(Просто введи целое число)")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				break
	try:
		global k_str
		k_str = int(msg)
	except:
		message_sender(id,"Напиши так, как я сказал, пожалуйста")
		get_k_str()
	print (zakaz + type_zk + type_pr + str(k_str))
	get_price_print()
	return k_str

def get_price_print():
	global price
	if ((type_zk == "\nТип заказа 1.Печать")):
		if (type_pr == "\nПечать Односторонняя\nКол-во страниц "):
			price = k_str * 6
		if (type_pr == "\nПечать Двухстороняя\nКол-во страниц "):
			price = (k_str // 2) * 8 + (k_str % 2) * 6
		message_sender(id, "Заполнение заказа почти окончено")
		message_sender(id, str(price) + "рублей - цена(примерная потому что не учитывается много факторов) ")
		get_somethingelse()
		return price
	else:
		return 0
def get_somethingelse():
	message_sender(id, "Напишите пожалуйста еще немного информации про заказ(про необходимость доставки, сроков печати и тд то что придет в голову)")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			global get_somethingelse
			get_somethingelse = msg
			if (i == 1):
				break
	end_zakaz()
	return get_somethingelse

def end_zakaz():
	message_sender(id, "Заполнение заказа готово. Документ для заказа скидывать не нужно, администратор сам его у вас спросит, когда свяжется с вами. Отправить администратору ваш заказ?(пиши либо \"Да\" либо \"Нет\" без кавычек))")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				break
	if ((type_zk == "\nТип заказа 2.Сканирование") or (type_zk == "\nТип заказа 2.Ксерокопия")):
		if (msg == "Да"):
			message_sender(main_id, zakaz + type_zk + "\n" + get_somethingelse)
			message_sender(id, "Ваш заказ успешно отправлен администратору. Вскором времени он свяжется с вами(Убедитесь, что у вас открыта личка). К сожалению пока что для данного типа заказа автоматически расчитать цену нельзя, но администратор работает над этим")
			return 1
		elif (msg == "Нет"):
			message_sender(id, "Ладно")
			return 0
		else:
			message_sender(id,"Напиши так, как я сказал, пожалуйста")
			end_zakaz()
	else:
		if (msg == "Да"):
			message_sender(main_id, zakaz + type_zk + type_pr + str(k_str) +"\n"+ get_somethingelse + "\n" + str(price) + "рублей - цена(примерная потому что не учитывается много факторов) " )
			message_sender(id, "Ваш заказ успешно отправлен администратору. Вскором времени он свяжется с вами(Убедитесь, что у вас открыта личка). ")
			return 1
		elif (msg == "Нет"):
			message_sender(id, "Ладно")
			return 0
		else:
			message_sender(id,"Напиши так, как я сказал, пожалуйста")
			end_zakaz()



def message_anchor(equal,n):
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			if (msg == equal):
				if (n == 1):
					start_send_1()
					return 1
				if (n == 2):
					send_help_2()
					return 1
				if (n == 3):
					send_safety_3()
					return 1
				if (n == 4):
					zakaz_yes_4()
					return 1
			else:
				if (msg == "Нет"):
					message_sender(id, "Ну ладно, бывает")
					return 0
				message_sender(id, "Сорри я тебя не понял")
				return 0

vk_session = vk_api.VkApi(token = config.MAIN_TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
main_id = config.MAIN_ID

for event in longpoll.listen():

	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		msg = event.text
		id = event.user_id
		zakaz = "Ссылка: vk.com/id" + str(id)

		if (msg == "начать") or (msg == "Начать"):
			start_send_1()

		elif (msg == "!гарантия_безопасности"):
			send_safety_3()

		elif (msg == "!помоги"):
			send_help_2()

		elif (msg == "!заказ"):
			message_sender(id, "Точно приступаем?(пиши либо \"Да\" либо \"Нет\" без кавычек)")
			message_anchor("Да", 4)
		else:
			message_sender(id, "Сорри я тебя не понял")
