"""
"""

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


_g_textures = [None,]

_container_paths_pair = (
						(_controller_icons, PATH_CONTROLLER_ICONS), 
						(_map_icons, PATH_MAP_ICONS), 
						(_wall_textures, PATH_WALL_TEXTURES), 
						(_sky_textures, PATH_SKY_TEXTURES), 
						(_digit_textures, DIGIT_TEXTURES), 
						(_game_textures, GAME_TEXTURES), 
						(_menu_textures, MENU_TEXTURES)
						)

_container_paths_iter = (entry for entry in _container_paths_pair)

									   
def flr_texture():
	return _g_textures[0]

"""
	_size = 64 * 64 * 4
	_buf_floor = [255 - int(x * 255 / _size) for x in range(_size)]
	_ = Texture.create(size=(64,64))
	_.blit_buffer(bytes(_buf_floor), colorfmt='rgba', bufferfmt='ubyte')
	return _
"""
	
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
			raise Exception("Invalid action type {}. Must be type: idle, walk, hit, attack, death".format(action_type))
	else:
		raise Exception("Invalid id: {}".format(id))		

	
		
			
				
					
							