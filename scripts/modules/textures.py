"""
"""

from kivy.graphics.texture import Texture
from settings import *
import os


""" image caches """
_controller_icons = {}
_map_icons = {}
_wall_textures = {}
_sky_textures = {}
_digit_textures = {}
_menu_textures = {}
_game_textures = {}
_image_sequences = {}

_container_paths_pair = ((_controller_icons, PATH_CONTROLLER_ICONS), (_map_icons, PATH_MAP_ICONS), (_wall_textures, PATH_WALL_TEXTURES), (_sky_textures, PATH_SKY_TEXTURES), (_digit_textures, DIGIT_TEXTURES), (_game_textures, GAME_TEXTURES), (_menu_textures, MENU_TEXTURES))

_container_paths_iter = (entry for entry in _container_paths_pair)

#<---- Functions
def get_texture(image_name='', image_category=''):

	texture=None	
	
	if image_category == 'sky':
		if image_name.rsplit('.', 1)[-1] == 'png':
			texture = get_sky_texture(image_name)
		else:
			texture = flr_texture(image_name)
		
	elif image_category == 'controller':
		texture = get_controller_texture(image_name)
			
	elif image_category == 'wall':
		texture = get_wall_texture(image_name)
			
	elif image_category == 'map':
		texture = get_map_texture(image_name)
			
	elif image_category == 'digit':
		texture = get_digit_texture(image_name)
			
	elif image_category == 'menu':
		texture = get_menu_texture(image_name)
			
	elif image_category == 'game':
		texture = get_game_texture(image_name)
		
	elif image_category == 'floor':
		texture = flr_texture(image_name)
			
	else:
		raise Exception('Invalid image_category')
			
	return texture
	
def get_image_sequence(id='npc_sprite', action_type='idle'):
	if id in _image_sequences:
		if action_type == 'idle':
			return _image_sequences.get(id)[0]
			
		elif action_type == 'walk':
			try:
				return _image_sequences.get(id)[1]
			except:
				return _image_sequences.get(id)[0]
			
		elif action_type == 'hit':
			try:
				return _image_sequences.get(id)[2]
			except:
				return _image_sequences.get(id)[0]
							
		elif action_type == 'attack':
			try:
				return _image_sequences.get(id)[3]
			except:
				return _image_sequences.get(id)[0]
			
		elif action_type == 'death':
			try:
				return _image_sequences.get(id)[4]
			except:
				return _image_sequences.get(id)[0]
			
		else:
			valid_actions = "idle, walk, hit, attack, death"
			raise Exception("Invalid action type {}. Must be type: {}".format(action_type, valid_actions))
	else:
		raise Exception("Invalid id: {}".format(id))

#<---- supporting functions
def flr_texture(floor_color='white'):
	texture = None

	_size = 64 * 64 * 4
	_buf_floor = []
	
	max_brightness = 155
	min_brightness = 55
	
	f = lambda x: int(x * max_brightness / _size)
	g = lambda x: max_brightness - f(x)
	
	if floor_color=='white':
		_buf_floor = [g(x) for x in range(_size)]
		
	elif floor_color == 'i_white':
		_buf_floor = [f(x) for x in range(_size)]
		
	elif floor_color=='yellow':	
		_buf_floor = [min_brightness if x % 4 == 2 else g(x) for x in range(_size)]
				
	elif floor_color == 'i_yellow':
		_buf_floor = [min_brightness if x % 4 == 2 else f(x) for x in range(_size)]

	else:
		raise Exception('Floor Color not Found')
	
	texture = Texture.create(size=(64,64))
	texture.blit_buffer(bytes(_buf_floor), colorfmt='rgba', bufferfmt='ubyte')

	return texture
									   
def blank_texture():
	texture = None
	
	_size = 64 * 64 *4
	_buf = [255 for x in range(_size)]
	texture = Texture.create(size=(64, 64))
	texture.blit_buffer(bytes(_buf), colorfmt='rgba', bufferfmt='ubyte')
	
	return texture
	
def backrooms_texture():
	texture = None
	_size = 64 * 64 * 4
	_buf = []
	
	for x in range(_size):
		if x % 4 == 2:
			_buf.append(0)
		else:
			_buf.append(int(150 * x / _size))
			
	texture = Texture.create(size=(64, 64))
	texture.blit_buffer(bytes(_buf), colorfmt='rgba', bufferfmt='ubyte')
	
	return texture
	
def get_sky_texture(str):
	return _sky_textures.get(str, _sky_textures.get("default_sky.png"))
	
def get_controller_texture(str="dotted_circle.png"):
	return _controller_icons.get(str)

def get_wall_texture(str="x"):
	return _wall_textures.get("{}{}".format(str,'.png'), _wall_textures.get('x.png'))

def get_map_texture(str):
	return _map_icons.get(str)
	
def get_digit_texture(str='0'):
	return _digit_textures.get("{}{}".format(str,'.png'))
	
def get_menu_texture(str='victory.png'):
	return _menu_textures.get(str)
	
def get_game_texture(str='py.png'):
	return _game_textures.get(str)
						