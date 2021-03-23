import requests
import time
from config import TOKEN


URL = f'https://api.telegram.org/bot{TOKEN}/'  # стандартный url для общения с ботом


def get_updates():
	""" Запрашивает и получает обновления от бота

		Функция возвращает объект - словарь Python
	"""
	url = URL + 'getUpdates' 
	r = requests.get(url) # делаем запрос и получаем объект Response
	return r.json()

def get_message():
	"""
	Извлекает из полученных обновлений chat_id и текст последнего отправителя
	и возвращает их из функции в виде словаря
	"""
	data = get_updates()

	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	update_id = data['result'][-1]['update_id']

	message = {	'chat_id': chat_id,
				'text': message_text,
				'update_id': update_id }

	return message


def send_message(chat_id, text='Подождите секунду, пожалуйста..'):
	"""
	Принимает два аргумента:
		chat_id - id пользователя Telegram
		text - строку (не обязательный аргумент)

	Отправляет на указанный chat_id сообщение из text
	"""

	url = URL + f'sendMessage?chat_id={chat_id}&text={text}'
	requests.get(url)


def main():
	"""
	Запускает бесконечный цикл, который проверяет наличие новых обновлений
	Если обновление обнаружено, отвечает последнему написавшему боту пользователю его же сообщением
	"""


	old_update_id = None

	while True:
		print('Жду 10 сек')
		time.sleep(10)  # ожидание 10 сек, чтобы не спамить по 1000 запросов/сек

		message = get_message()

		if old_update_id != message['update_id']:
			print('Обнаружено новое обновление, отвечу-ка я')
			chat_id = message['chat_id']
			text = message['text']
			send_message(chat_id, text)

		old_update_id = message['update_id']



if __name__ == '__main__':
	main()