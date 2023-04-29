# -*- coding: utf-8 -*-
from json import loads as de_json, JSONDecodeError
from datetime import datetime
import os.path

LOG_FILE = "log/bot_{}.log".format(datetime.now().strftime("%d.%m.%y_%H-%M-%S"))

def load_json(path):
	if not os.path.isfile(path):
		return None
	try:
		return de_json(open(path).read())
	except JSONDecodeError:
		return None

def set_log():
	global LOG_FILE
	if not os.path.isfile(LOG_FILE):
		f = open(LOG_FILE, "w")
		f.close()

def log(info, user=None):
	if(user == None):
		text = "{0} LOG: {1}".format(datetime.now().strftime("[%d/%b/%Y:%H:%M:%S]"), info)
	else:
		text = "{0} LOG: {1}USER-{2}_{3}".format(datetime.now().strftime("[%d/%b/%Y:%H:%M:%S]"), info, user.id, user.first_name)
	print(text)
	f_log = open(LOG_FILE, 'a')
	f_log.write( "{}\n".format(text) )
	f_log.close()