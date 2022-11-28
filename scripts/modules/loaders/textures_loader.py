	
""" Non sprites images. Format: {'key_1.png': ImageObject1<>, 'key_2.png': ImageObject2<>,....}
	<image name as key>: <image texture object>
	! This is not unit tested. Mother Fucker!
"""
from scripts.modules.loaders import universal_files_loader as u_loader
from kivy.core.image import Image
from scripts.modules import textures
import os

_fname=[]
_path=''	

_files_iterator = None
_container_ref = None

_container_paths_iterator = None
_path_iterator = None
_has_re_init = False

def next_container_paths_iterator(container_paths_iter=None):
	global _container_paths_iterator, _path_iterator, _container_ref    #, paths
	
	if container_paths_iter:
		_container_paths_iterator = container_paths_iter
	
	try:
		_container_ref, paths = next(_container_paths_iterator)
	except Exception as stp:
		raise stp
	else:
		_path_iterator = (path for path in paths)
		
def next_paths_filenames_iterator():
	global _path, _files_iterator
	
	p = ''
	try:
		while p== '':
			p = next(_path_iterator)
	except Exception:
		next_container_paths_iterator()
	else:
		_path, file_name = u_loader.get_filenames(p, 'Invalid Path')
		
		f = lambda p,n,mmp: Image(os.path.join(p, n)).texture
		
		_files_iterator = ({name: f(_path, name, True)} for name in file_name)
		
def next_textures_dict():
	r_string = ''
	try:
		key_value_pair = next(_files_iterator)
		r_string = list(key_value_pair)[0]
		key_value_pair.get(r_string).wrap='repeat'
		_container_ref.update(key_value_pair)
		
	except Exception:
		next_paths_filenames_iterator()
		
	return os.path.join(_path, r_string)

_do_once=False	
def update(dt=0, game_ref=None):	
	global _has_re_init, _do_once
	
	if _do_once:
		_do_once = False
		return
	
	if not _has_re_init:
		next_container_paths_iterator(textures._container_paths_iter)
		next_paths_filenames_iterator()
		_has_re_init = True
		return 'Loading Textures', False
	
	
	return next_textures_dict(), False




