# Telegram-боты от А до Я
<p>Реализация телеграм-ботов различными методами, начиная от написания бота на чистом Python без внешних фреймворков и заканчивая реализацией бота внутри фреймворка Django
<p>Проект находится в стадии разработки и будет регулярно дополняться

## Оглавление
0. [Настройка рабочей среды](#Настройка-рабочей-среды)
1. [Хардкор-бот без фреймворков](#Хардкор-бот-без-фреймворков)
2. [Бот с webhook на Flask](#Бот-с-webhook-на-Flask)
	1. [Запуск бота на сервере](#Запуск-бота-на-сервере)
		1. [С SSL](#Запуск-на-сервере-с-установленным-сертификатом-SSL)
		2. [Без SSL](#Запуск-на-localhost-или-на-сервере-без-SSL)
	2. [Установка вебхука](#Установка-вебхука)
3. [Бот на Django](#Бот-на-Django)
	1. [Настройка рабочей среды Django](#Настройка-рабочей-среды-Django)
	2. [Запуск бота Django](#Запуск-бота-Django)
4. [Полезные ресурсы](#полезные-ресуры)

## Настройка рабочей среды

Для начала необходимо установить и активировать виртуальную среду, обновить pip и установить все зависимости:
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## Хардкор-бот без фреймворков

Простой эхо-бот. Умеет работать только с `GET`-запросами.
Для этого он использует библиотеку `requests`.  
Для получения обновлений от Telegram используется метод `getUpdates`.
Исходники лежат [здесь](https://github.com/Khalmatov/python-telegram-bots/tree/master/bot-hardcore).

> Предполагается, что токен лежит в файле `config.py` в папке `bot-hardcore`


## Бот с webhook на Flask

Разница между предыдущим ботом и этим в методе получения обновлений от Telegram.
Здесь бот вместо того, чтобы периодически спамить сервера Telegram методом `getUpdates` для получения обновлений,
работает по принципу `Webhook`.  
Исходники лежат [здесь](https://github.com/Khalmatov/python-telegram-bots/tree/master/bot-flask).

> Предполагается, что токен лежит в файле `config.py` в папке `bot-flask`

1. ### Запуск бота на сервере
	1. #### Запуск на сервере с установленным сертификатом SSL 

	Для этого на сервере необходимо настроить связку Flask + UWSGI + Nginx  
	В этом вам поможет [статья на *DigitalOcean*](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04-ru)

	2. #### Запуск на localhost или на сервере без SSL

	Telegram требует, чтобы url-адрес для вебхука начинался с `https://`.
	Поэтому для установки бота на локальный сервер или на сервер без SSL-сертификата
	вам понадобится установить "туннель" через сторонние сервисы типа [**localhost.run**](https://localhost.run) или [**ngrok**](https://ngrok.com).
	Рассмотрим пример установки с localhost.run.


	Например, если в ваш web-сервер на Flask с телеграм-ботом внутри запущен по адресу `127.0.0.1:5000` (по умолчанию),
	вам достаточно ввести в терминале эту команду:
	```bash
	ssh -R 80:localhost:5000 localhost.run
	```
	В ответ вы получите url-адреса вида `https://f6773f9edca4d5.localhost.run`,
	по которому извне можно будет получить доступ к локальным файлам вашего компьютера

2. ### Установка вебхука

Для установки вебхука необходимо послать get-запрос такого формата:
```url
https://api.telegram.org/{token}/setWebhook?url={url}
```
Где:
* **token** - это токен, который вы получили от BotFather
* **url** - это url-адрес, на который будут приходить обновления в виде POST-запроса

Например:
```url
https://api.telegram.org/bot123445:FJFIOEJFIOER/setWebhook?url=https://bot.mysite.com
```

Чтобы послать get-запрос скопируйте url выше (**изменив данные на свои**) и:
* либо вставьте url в поле ввода адреса вашего браузера и нажмите <kbd>Enter</kbd>
* либо в терминале пошлите запрос через `curl`:
	```bash
	curl -X GET https://api.telegram.org/bot123445:FJFIOEJFIOER/setWebhook?url=https://f6773f9edca4d5.localhost.run
	```

В ответ вы должны получить:
```json
{
  "ok":true,
  "result":true,
  "description":"Webhook was set"
}
```


## Бот на Django

Бот, который реализован внутри приложения Django и запускаетя по команде `python manage.py bot`.  
Используется фреймворк [**python-telegram-bot**](https://github.com/python-telegram-bot/python-telegram-bot)  
Исходники лежат [здесь](https://github.com/Khalmatov/python-telegram-bots/tree/master/bot-django).

> Предполагается, что токен лежит в файле `config.py` в папке `bot-django`

0. ### Настройка рабочей среды Django

Для того, чтобы бот работал, он должен находиться внутри зарегистрированного приложения Django. Если у вас уже есть готовый проект на Django, переходите сразу на шаг №2. В ином случае:

1. Создайте проект Django в терминале:
```bash
django-admin startproject myproject
cd ./myproject
```

2. Скопируйте `bot-django` в родительскую папку проекта Django (в моем случае это папка `myproject`) и зарегистрируйте приложение в настройках по пути `myproject/settings.py':
```python
...
INSTALLED_APPS = [
	...
	'bot-django',
	]
...
```

1. ### Запуск бота Django
Если все прошло успешно, при наборе в терминале команды `python manage.py --help` вы должны увидеть что-то подобное:
```bash
Type 'manage.py help <subcommand>' for help on a specific subcommand.
Available subcommands:
...
[bot-django]
    bot
```
Как вы, наверное, уже догадались, запуск бота осуществляется командой `python manage.py bot`.
Если бот успешно запущен, вы должны увидеть в терминале такой ответ:
```python
{'id': 1234567890, 'first_name': 'Крутой-бот', 'is_bot': True, 'username': 'very_cool_bot', 'can_join_groups': False, 'can_read_all_group_messages': False, 'supports_inline_queries': False}
```

## Полезные ресурсы
1. [Официальная документация Telegram Bot API *in English*](https://core.telegram.org/bots/api)
2. [Документация Telegram Bot API *на русском*](https://tlgrm.ru/docs/bots/api)
3. [Уроки про Telegram-боты от Олега Молчанова *на YouTube*](https://youtube.com/playlist?list=PLlWXhlUMyooaTZA4vxU9ZRZQPCFxUq9VA)
4. [Уроки по фреймворку Aiogram от Physics is Simple *на YouTube*](https://youtube.com/playlist?list=PLwVBSkoL97Q3phZRyInbM4lShvS1cBl-U)
