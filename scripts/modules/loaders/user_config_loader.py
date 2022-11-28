import csv
import os
from settings import *



_default_user_config = 'scripts/resources/docs/default_user_config.csv'
_user_config_path = _default_user_config
_config_dict={}

_game=None
def get_config():
	global _config_dict, _user_config_path
	
	if os.path.isfile(USER_CONFIG_PATH):
		_user_config_path = USER_CONFIG_PATH
	
	with open(_user_config_path, newline='') as f:
		f_reader = csv.reader(f)
	
		for row in f_reader:
			try:
				row_key = row[0]
				if row_key[0] == '#':
					continue
				
				_config_dict[row[0]] = (row[1], row[2])
					
			except Exception as a:
				continue
				
	return "Reading Config File: {}".format(_user_config_path)
		
def get_kwargs():
	if _game.mode == 'mode 1':
		_game.kw_args = {key: _config_dict.get(key)[0] for key in _config_dict}

	elif _game.mode == 'mode 2':
		_game.kw_args = {key: _config_dict.get(key)[1] for key in _config_dict}
		
	return "Setting Config KV Pair"
		
		
func_iter = (func for func in (get_config,get_kwargs))

def execute():
	return next(func_iter)()

def update(dt=0, game_ref=None):
	global _game
	
	if not _game:
		_game = game_ref
		
	return execute(), False	
