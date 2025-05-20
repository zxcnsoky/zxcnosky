import telebot
import os

bot = telebot.TeleBot(token=os.environ.get('8150653471:AAFNN43qlOUkHqmN_GrTXmlFlLwHGmOWDS8'))
bot.remove_webhook()


