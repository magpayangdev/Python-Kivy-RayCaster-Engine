
from scripts.bases.timed_updates.timed_texture import TimedTexture
from settings import *
import math

class Sky(TimedTexture):
	def __init__(self, game, image_name='dark_night_sky.png', hide=False):
		super().__init__(game, window=None, image_name=image_name, image_category='sky', color=(1,1,1,1), size=(100,100), pos=(0,0), hide=hide, flip_time=1, start_iter=True)
		
		self.flip_time = self.rect.texture.width

		self.rect_size = self.game.window.width, self.game.window.height/2
		self.rect_pos = self.game.window.pos[0], self.game.window.height/2

	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)
		
		if self.game.player:
			yaw = self.game.player.yaw
		else:
			yaw = self.accum_time
		
		uv_pos = (0,0)
		if yaw == 0:
			uv_pos = ((self.rect_texture.uvpos[0] + 1 * dt * 0.005) % self.rect_texture.width, 
						self.rect_texture.uvpos[1])

		else:
			uv_pos = ((self.rect_texture.uvpos[0] + 0.001 * dt * yaw) % self.rect_texture.width, 
						self.rect_texture.uvpos[1])

		self.rect_texture.uvpos = uv_pos
		self.rect_texture = self.rect_texture
		
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
		super().re_size()
		
	def show(self):
		super().show()
					
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()































