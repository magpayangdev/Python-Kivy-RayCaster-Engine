"""
Seeks files in path provided on settings. returns a dict
"""


from kivy.core.image import Image
from kivy.core.audio import SoundLoader

import os
from settings import *

def key_from_file_name(file_name):
	if file_name:
		return file_name.rsplit('.', 1)[0]
	return ''

def get_filenames(path, tantrum='Invalid path!'):
	if os.path.isdir(path):
		pass
	elif os.path.isfile(path):   
		path = path.rsplit('/', 1)[0]
	else:
		raise Exception(tantrum+" {}".format(path))

	f = lambda file, path : os.path.isfile(os.path.join(path, file)) and not file.startswith('.')
	
	return path, [file for file in os.listdir(path) if f(file, path)]

def audio_dict(paths, tantrum='Invalid path!'):
	""" searches for files in the provided paths, returns key value pair of 
		{string file_name without extension, SoundObect}
	"""
	file_names = []
	path = ''
	set = {}
	
	if isinstance(paths, str):
		paths = [paths]
		
	elif isinstance(paths, tuple):
		paths = paths
		
	else:
		raise Exception(tantrum + " {}".format(paths))
	
	for p in paths:
		path, file_names = get_filenames(p, tantrum)
		
		set.update({name: SoundLoader.load(os.path.join(path, name)) for name in file_names})
	 
	return set
	
def texture_dict(paths, mipmap=True, repeat=False, tantrum='Invalid path!', debug = False):
	""" searches for files in the provided paths, returns key value pair of 
		{string file_name without extension, Image}
	"""
	file_names = []
	path = ''
	set = {}
	
	if isinstance(paths, str):
		paths = [paths]
		
	elif isinstance(paths, tuple):
		paths = paths
		
	else:
		raise Exception(tantrum + " {}".format(paths))
	
	for p in paths:
		path, file_names = get_filenames(p, tantrum)
		set.update({name: Image(os.path.join(path, name), mipmap=mipmap).texture for name in file_names})
	
	if repeat:	
		for key in set.keys():
			set[key].wrap = 'repeat'
	 
	return set
	
def textures_list(path, mipmap=True, repeat=False, tantrum='Invalid path!'):
	path, file_names = get_filenames(path, tantrum)
	
	if repeat:
		list = tuple(Image(os.path.join(path,file_name),mipmap=mipmap).texture for file_name in file_names)
		
		for image in list:
			image.wrap = 'repeat'
		return list
	
	return tuple(Image(os.path.join(path,file_name),mipmap=mipmap).texture for file_name in file_names)
	
def sprite_actions_image_sequences():
	f = lambda key: tuple(textures_list(path, 
						True, False) for path in SPRITE_ID_TO_IMAGES_PATH[key] if  path != EMPTY_PATH)
	return {key: f(key) for key in SPRITE_ID_TO_IMAGES_PATH}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	