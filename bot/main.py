# -*- coding: utf-8 -*-
import telebot
from functions import log, set_log
from bottoken import token

botApp = telebot.TeleBot(token)

@botApp.callback_query_handler(lambda call: call.game_short_name == 'bapple')
def play_bad_apple(call):
	log('bad_apple-', call.from_user)
	botApp.answer_callback_query(call.id, url="https://skillmasters.ru/")

@botApp.callback_query_handler(lambda call: call.game_short_name == 'tictactoe')
def play_tictactoe(call):
	log('tictactoe-', call.from_user)
	botApp.answer_callback_query(call.id, url="https://abelidze.github.io/XOGame/")


if __name__ == '__main__':
	botApp.remove_webhook()
	set_log()
	log("BlazorBot started! <-> ['Ctrl+C' to shutdown]")
	botApp.infinity_polling(skip_pending=True)
	log("Bye Bye!")
