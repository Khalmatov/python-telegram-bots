from flask import Flask
from flask_sslify import SSLify 


app = Flask(__name__) # __name__ - ссылка на текущий файл
# sslify = SSLify(app) # раскомментируй, если бот лежит на хостинге с SSL-сертификатом


@app.route('/')
def index():
	return('<h1>test flask</h1>')



if __name__ == '__main__':
	app.run()