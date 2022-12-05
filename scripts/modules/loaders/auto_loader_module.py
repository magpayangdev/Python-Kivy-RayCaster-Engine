
from scripts.modules.loaders import audio_loader as audio_loader
from scripts.modules.loaders import modules_loader as modules_loader
from scripts.modules.loaders import textures_loader as textures_loader
from scripts.modules.loaders import re_init_modules as re_init_modules
from scripts.modules.loaders import modules_re_loader as modules_re_loader
from scripts.modules.loaders import user_config_loader as user_config_loader
from scripts.modules.loaders import generated_textures as generated_textures
from scripts.modules.loaders import sprites_textures_loader as sprite_textures_loader

											
_reload_sequence_iterator = None

_load_sequence_iterator = None


_func = None
_debug_int = 0
_game_ref = None

def re_init(game_ref=None):
	global _game_ref, _reload_sequence_iterator, _load_sequence_iterator
	_game_ref = game_ref

	_reload_sequence_iterator = (func for func in (re_init_modules.update, user_config_loader.update, modules_re_loader.update))

	_load_sequence_iterator = (func for func in (textures_loader.update, generated_textures.update, sprite_textures_loader.update, audio_loader.update, re_init_modules.update, user_config_loader.update, modules_loader.update))


def create_loading_screen(_game_ref):
	modules_loader.re_init(_game_ref)
	modules_loader.load_loading_screen()
	modules_loader.load_event_manager()
	
def next_load_sequence_iterator():
	global _func
	_func = next(_load_sequence_iterator)

def execute_func(dt=0, game_ref=None):
	global _func
	
	kwargs = {'dt':0, 'game_ref':_game_ref}
	
	try:
		return _func(**kwargs)
			
	except StopIteration: #<-- I will only accept StopIteration
		try:
			next_load_sequence_iterator()
			
		except StopIteration:
			return 'Finished Loading...', True
			
		else:
			return '', False

_do_once = True
def update(dt): 
	global _do_once
	
	if _do_once:
		_do_once = False
		next_load_sequence_iterator()
	
	if not _game_ref:
		return

	finished_loading = False		
	_game_ref.l_screen.text, finished_loading = execute_func(dt, _game_ref)	

	if finished_loading:
		_game_ref.event.finished_loading()	
		_do_once = True


#<---- Reload
def reload_loading_screen(game_ref):
	re_init(game_ref)
	
	user_config_loader.re_init()
	
	modules_re_loader.re_init(game_ref)
	modules_re_loader.re_init_loading_screen()

def re_load(dt):
	global _do_once

	if _do_once:
		_do_once = False

		next_reload_sequence_iterator()
		
	if not _game_ref:
		return
		
	finished_reloading = False
	_game_ref.l_screen.text, finished_reloading = execute_reload_func(dt, _game_ref)
	
	if finished_reloading:
		_game_ref.event.finished_reinit()
		_do_once = True
		
def execute_reload_func(dt=0, game_ref=None):
	global _func
	
	try:
		return _func()
		
	except StopIteration:
		try:
			next_reload_sequence_iterator()
			
		except StopIteration:
			return 'Finished Re Loading...', True
			
		else:
			return 'Reloading', False
			
def next_reload_sequence_iterator():
	global _func
	_func = next(_reload_sequence_iterator)
