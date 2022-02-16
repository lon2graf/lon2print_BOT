import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config


def message_sender(id, text):
	vk.messages.send(user_id = id, message = text, random_id = 0)

def get_wantenter(): # функция, которая проверяет готовность заказчика идти дальше по плану
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				if (msg == "Да"):
					want = 1
					return want 	# означает, что пользователь хочет идти дальше
				elif (msg == "Нет"):
					want = 0
					return want # означает, что пользователь не готов идти дальше
				else:
					want = "non"
					return want

def order_gettype(): # фунция составная часть от get_order() используется для получения типа заказа от заказчика
	message_sender(id, "Напишитие пожалуйста тип услуги : \n1.Печать 2.Сканирование 3.Ксерокопия\nПросто напиши цифру")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				if (msg == "1"):
					order_type = 1
					return order_type
				elif (msg == "2"):
					order_type = 2
					return order_type
				elif (msg == "3"):
					order_type = 3
					return order_type
				else:
					message_sender(id, "сори я тебя не понял, пиши пожалуйста так, как я сказал")
					return "non"

#вызывается если услуга связана с печатью
def gettype_print(): # функция для получения типа печати
	message_sender(id, "Напишитие пожалуйста тип печати : \n1.Одностороняя 2.Двухсторонняя\nПросто напиши цифру")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				if (msg == "1"):
					type_print = 1
					return type_print
				elif (msg == "2"):
					type_print = 2
					return type_print
				else:
					type_print = "non"
					return type_print

def get_countsheets():
	message_sender(id, "Напиши пожалуйста количество страниц к печати(в виде числа без лишних символов)")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				try:
					count_sheets = int(msg)
					return count_sheets
				except:
					count_sheets = "non"
					return count_sheets

def get_price(type_print, count_sheets):
	if (type_print == 1):
		price = count_sheets * 6
		return price
	else:
		price = (count_sheets // 2) * 8 + (count_sheets % 2) * 6
		return price

def get_difint():
	message_sender(id,"Напишите пожалуйста еще немного дополнительной информации, которая вам придет в голову.")
	i = 0
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			msg = event.text
			i += 1
			if (i == 1):
				something = msg
				return something


def get_order(): #функция в которой вызываются все остальные функции для заказа и обрабатываются
	message_sender(id, "приступаем к заказу? Напиши либо \"Да\" либо \"Нет\" без кавычек.")
	enter = get_wantenter()

	if enter == 0: #пользователь не хочет приступать к оформлению заказа
		message_sender(id,"ладно как хочешь")

	elif enter == 1: # пользователь хочет приступить к выполнению заказа

		# получение типа заказа
		print("хочет заказ")
		type_ord = order_gettype()
		if (type_ord == "non"):
			while type_ord == "non":
				type_ord = order_gettype()
		print("тип заказа - " + str(type_ord))

		#получение типа печати, количества страниц, цены если услуга = 1 или 3
		if ((type_ord == 1) or (type_ord == 3)):
			type_print = gettype_print()
			if (type_print == "non"):
				while (type_print == "non"):
					type_print = gettype_print()
			print("тип печати - " + str(type_print))
			count_sheets = get_countsheets()
			if (count_sheets == "non"):
				while (count_sheets == "non"):
					count_sheets = get_countsheets()
			print("колво страниц - " + str(count_sheets))

			#получение приблизительной цены
			if (type_print == 1):
				money = get_price(1,count_sheets)
			elif (type_print == 2):
				money = get_price(2, count_sheets)


			info_dop = get_difint()
			message_sender(id, "Приблизительная цена(потому что не учитвается много факторов): " + str(money))
			zakaz = "Ссылка : vk.com/id" + str(id) + "\n"+ "Номер заказа: " + str(type_ord) +"\n"+ "Тип печати:" + str(type_print) +"\n"+ "Доп-информация: " + info_dop +"\n" +"Примерная цена: " + str(money)
			print(money)

		elif (type_ord == 2):
			message_sender(id, "К сожалению пока, на данное время, на данную услугу цену бот определять не умеет")
			info_dop = get_difint()
			zakaz = "Ссылка : vk.com/id" + str(id) + "\nНомер заказа: " + str(type_ord) + "\nДоп-информация: " + info_dop


		message_sender(id, "Согласны вы ли отправить свой заказ администратору для дальнейшего обслуживания?(\"Да\" \"Нет\")")
		agreement = get_wantenter()
		if (agreement == 1):
			message_sender(main_id, zakaz)
		elif (agreement == 0):
			message_sender(id, "Ладно бывает")
		elif (agreement == "non"):
			while (agreement == "non"):
				agreement == get_wantenter()


	else:
		message_sender(id, "Прости, я не понял тебя. ")
		get_order()




vk_session = vk_api.VkApi(token = config.MAIN_TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
main_id = config.MAIN_ID
print(id)

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		msg = event.text
		id = event.user_id

		if (msg == "начать"):
			message_sender(id,"дарова пиши заказ")

		elif (msg == "заказ"):
			get_order()
