
from scripts.modules import textures
from kivy.graphics.texture import Texture

def generate_flr_texture():
	_size = 64 * 64 * 4
	_buf_floor = [255 - int(x * 255 / _size) for x in range(_size)]
	textures._g_textures[0] = Texture.create(size=(64,64))
	textures._g_textures[0].blit_buffer(bytes(_buf_floor), colorfmt='rgba', bufferfmt='ubyte')
	return """ Floor Texture """

func_iter = (func for func in (generate_flr_texture,))

def execute():
	return next(func_iter)()

def update(dt=0, game_ref=None):
	return execute(), False