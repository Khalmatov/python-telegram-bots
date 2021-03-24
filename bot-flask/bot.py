from flask import Flask
from flask_sslify import SSLify
from flask import request
from flask import jsonify
from flask import Response

import requests
import json
from config import TOKEN

app = Flask(__name__)  # __name__ - ссылка на текущий файл
# sslify = SSLify(app)
# раскомментируй сверху, если бот запущен:
#		1) на хостинге с SSL-сертификатом
#		2) или через туннель localhost.run
URL = f'https://api.telegram.org/bot{TOKEN}/'  # стандартный url для общения с ботом


def send_message(chat_id, text='Подождите секунду, пожалуйста..'):
	"""
	Принимает два аргумента:
		chat_id - id пользователя Telegram
		text - строку (не обязательный аргумент)

	Отправляет на указанный chat_id сообщение из text
	"""

	url = URL + f'sendMessage?chat_id={chat_id}&text={text}'
	requests.get(url)


@app.route('/', methods=['GET'])
def index():
	"""
	Функция запускается при поступлении get-запросов на корневой уровень
	"""
	return '<h1>Hello, i\'m a bot. Who are u?</h1>'


@app.route(f'/{TOKEN}', methods=['POST'])
def bot():
	"""
	Функция запускается при поступлении post-запросов от телеграм

	В поступившем JSON-е от Telegram парсится chat_id и текст сообщения
	Отправителю высылается его же сообщение
	"""
	try:
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		text = r['message']['text']
		send_message(chat_id, text)
	except Exception as e:
		print(repr(e))
		return '<h1>Hello, i\'m a bot. Who are u?</h1>'
	else:
		return Response(status = 200)


if __name__ == '__main__':
	app.run() # 127.0.0.1:5000