
from scripts.modules.loaders import universal_files_loader as u_loader
from kivy.core.image import Image
from scripts.modules import textures
from settings import *
import os
_sprite_id_to_path_iterator = ({kv_p:SPRITE_ID_TO_IMAGES_PATH[kv_p]} for kv_p in SPRITE_ID_TO_IMAGES_PATH)

_sprite_id=''
_path = ''

_file_names_iterator = None
_path_iterator = None

_img_accumulator = []	
_img_actions_accumulator = []
_img_seq_dict = {}	

def next_sprite_id_paths_iterator():
	global _sprite_id, _path_iterator	
	
	try:
		_ = next(_sprite_id_to_path_iterator)
		_sprite_id = list(_.keys())[0]
		paths = _.get(_sprite_id)
		
	except StopIteration as stp:
		raise stp
	else:
		_path_iterator = (path for path in paths)

def next_path_iterator():
	global _path, _file_names_iterator
	global _img_seq_dict, _key, _img_actions_accumulator, _sprite_id

	try:
		p = ''
		while p=='':
			p = next(_path_iterator)

	except Exception:
		if _img_actions_accumulator:
			textures._image_sequences.update({_sprite_id: tuple(_img_actions_accumulator)})
			_sprite_id = ''
			_img_actions_accumulator = []
			
		next_sprite_id_paths_iterator()
	else:
		_path, file_names = u_loader.get_filenames(p, 'Invalid Path')
		_file_names_iterator = (fname for fname in file_names)
		
def next_fname_iterator():
	global _img_accumulator
		
	fname = ''
	try:
		fname = next(_file_names_iterator)
	except Exception:
		if _img_accumulator:
			_img_actions_accumulator.append(tuple(_img_accumulator))
			_img_accumulator = []
			
		next_path_iterator()
	else:
		_img_accumulator.append(Image(os.path.join(_path, fname)).texture)
		
	return os.path.join(_path, fname)
		
def update(dt=0, game_ref=None):
	return next_fname_iterator(), False




























