
from scripts.bases.timed_updates.timed_update import TimedUpdate
from scripts.bases.window_objects.textured_rect import TexturedRect
from scripts.modules.textures import *

class TimedTexture(TimedUpdate):
	def __init__(self, game, window, image_name, image_category, color=(1,1,1,1), size=(100,100), pos=(0,0), hide=False, flip_time=1, start_iter=False):
		super().__init__(game, flip_time=flip_time, start_iter=start_iter)
		
		self.rect = TexturedRect(game=game, window=window, image_name=image_name, image_category=image_category, color=color, size=size, pos=pos, hide=hide)

	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
		self.rect.re_init()
		
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
	
	#<----Rectangle properties	
	@property
	def rect_size(self):
		return self.rect.size
		
	@rect_size.setter
	def rect_size(self, value):
		self.rect.rect.size = self.rect.size = value
		
	@property
	def rect_pos(self):
		return self.rect.pos
		
	@rect_pos.setter
	def rect_pos(self, value):
		self.rect.rect.pos = self.rect.pos = value
		
	@property
	def rect_texture(self):
		return self.rect.texture
		
	@rect_texture.setter
	def rect_texture(self, value):
		self.rect.rect.texture = self.rect.texture = value
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		