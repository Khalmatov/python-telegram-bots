from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from telegrambot.config import TOKEN


def log_errors(f):
	"""Ловит ошибки со стороны обработчиков"""
	def inner(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except Exception as e:
			error_message = f'Произошла ошибка: {e}'
			print(error_message)
			raise e
	return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
	chat_id = update.message.chat_id
	text = update.message.text

	reply_text = f"Ваш ID = {chat_id}\nВы написали \"<b>{text}</b>\""
	update.message.reply_text(text=reply_text, parse_mode='html')


class Command(BaseCommand):
	help = 'Команда для запуска telegram-бота'

	def handle(self, *args, **options):

		# 1 - правильное подключение
		request = Request(connect_timeout=0.5, read_timeout=1.0)
		bot = Bot(request=request, token=TOKEN)
		print(bot.get_me())

		# 2 - обработчики
		updater = Updater(bot=bot, use_context=True)

		message_handler = MessageHandler(filters=(Filters.text), callback=do_echo)
		updater.dispatcher.add_handler(message_handler)

		# 3 - запуск бесконечой обработки входящих обновлений
		updater.start_polling()
		updater.idle()