
from scripts.modules.textures import *
from scripts.bases.timed_updates.timed_update import TimedUpdate
from scripts.bases.window_objects.textured_rect import TexturedRect

_FLIP_TIME, _START_ITER = 1, False
_IMG_NAME, _IMG_CATEGORY = 'python.png', 'game'
_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False
_IMAGE_NAME, _IMAGE_CATEGORY, _HIDE = 'dark_night_sky.png', 'sky', False


class TimedTexture(TimedUpdate):
	""" A TimedUpdate that spawns a TexturedRect"""
	def __init__(self, game, window, flip_time=_FLIP_TIME, start_iter=_START_ITER, image_name=_IMAGE_NAME, image_category=_IMAGE_CATEGORY, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE):
		super().__init__(game, flip_time=flip_time, start_iter=start_iter)
		
		self.rect = TexturedRect(game=game, window=window, image_name=image_name, image_category=image_category, color=color, size=size, pos=pos, hide=hide)
		
	#<----Rectangle properties
	@property
	def rect_size(self):
		return self.rect.size

	@property
	def rect_pos(self):
		return self.rect.pos
		
	@property
	def rect_color(self):
		return self.rect.color

	@property
	def rect_texture(self):
		return self.rect.texture
		
	#<----Setter
	@rect_size.setter
	def rect_size(self, value):
		self.rect.size = value

	@rect_pos.setter
	def rect_pos(self, value):
		self.rect.pos = value
		
	@rect_color.setter
	def rect_color(self, value):
		self.rect.color = value
		
	@rect_texture.setter
	def rect_texture(self, value):
		self.rect.texture = value

	#<----Base Functions: re_init, update
	def re_init(self, flip_time=_FLIP_TIME, start_iter=_START_ITER, image_name=_IMAGE_NAME, image_category=_IMAGE_CATEGORY, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE):
		super().re_init(flip_time=flip_time, start_iter=start_iter)
		
		self.rect.re_init(image_name=image_name, image_category=image_category, color=color, size=size, pos=pos, hide=hide)
		
	def update(self, dt):
		super().update(dt)
		self.rect.update(dt)

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)
		
	def timed_update(self):
		super().timed_update()
		
	#<----Timed Update Functions: do_once_func, try_func, stop_iteration_func	
	def do_once_func(self):
		super().do_once_func()
			
	def try_func(self):
		super().try_func()
		
	def stop_iteration_func(self):
		super().stop_iteration_func()
		
	#<----Loop Controls: start, resume, loop, stop	
	def start(self):
		super().start()
		
	def resume(self):		
		super().resume()
		
	def loop(self):
		super().loop()
		
	def stop(self):
		super().stop()	
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		self.rect.re_size()
		
	def show(self):
		self.rect.show()
					
	def hide(self):
		self.rect.hide()
					
	def remove(self):
		self.rect.remove()
	

		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		