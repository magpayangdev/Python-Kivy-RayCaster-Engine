
from settings import *
from scripts.base_classes.loop_doonce_iter_timed_base import SeqImageLoopDoOnceIterRect

from scripts.base_classes.base_sprite import ScreenSprite
		
class PlayerSprite(ScreenSprite):
	def __init__(self, game, window=None, start_animating=False, hide=True):
		super().__init__(game=game, window=window, sprite_id='shot_gun', start_iter=start_animating, screen_size=(100,100), screen_pos=(0,0), hide=hide)

		self.flip_time = 0.15

		self.size = controller_size()
		self.pos = (scr_width() - controller_size()[0]) / 2, 0

		self.re_size()	
		
	def re_size(self):
		super().re_size()

	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()

	def re_init(self):
		super().re_init()
		
	def update(self, dt):
		super().update(dt)
		
	def fbf_update(self, dt):
		super().fbf_update(dt)
		
	def timed_update(self):
		super().timed_update()
		
	def do_once_func(self):
		super().do_once_func()
		self.game.event.player_attack()
					
	def try_func(self):
		super().try_func()
		
	def stop_iteration_func(self):
		super().stop_iteration_func()
		
	def start(self):
		super().start()
		
	def resume(self):
		super().resume()
				
	def loop(self):
		super().loop()
				
	def stop(self):
		super().stop()		
		
	#<---- Textures Func
	def reload_texture(self):
		super().reload_texture()
				
	def change_mode(self, new_mode):
		super().change_mode(new_mode)	
		
	#<---- Player Sprite Func
	def attack(self):
		self.resume()
		
	def attack_loop(self):
		self.loop()
		
	def stop_attack(self):
		self.stop()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		