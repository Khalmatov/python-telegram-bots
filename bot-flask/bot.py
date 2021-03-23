from flask import Flask
from flask_sslify import SSLify
from flask import request
from flask import jsonify

import requests
import json
from config import TOKEN

app = Flask(__name__)  # __name__ - ссылка на текущий файл
# sslify = SSLify(app)
# раскомментируй сверху, если бот запущен:
#		1) на хостинге с SSL-сертификатом
#		2) или через туннель localhost.run
URL = f'https://api.telegram.org/bot{TOKEN}/'  # стандартный url для общения с ботом

def write_json(dictionary):
	with open('answer.json', 'w') as file:
		json.dump(dictionary, file, indent=2, ensure_ascii=False)



@app.route('/', methods=['POST', 'GET'])
def index():
	"""
	Функция запускается при поступлении запросов на корневой уровень
	"""

	if request.method == 'POST':
		r = request.get_json()
		write_json(r)

		return jsonify(r)

	elif request.method == 'GET':
		return '<h1>Hello, i\'m a bot. Who are u?</h1>'


if __name__ == '__main__':
	app.run() # 127.0.0.1:5000