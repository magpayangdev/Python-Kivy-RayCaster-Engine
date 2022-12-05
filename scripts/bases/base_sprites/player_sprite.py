
from scripts.bases.base_sprites.screen_sprite import ScreenSprite
from settings import *

_SPRITE_ID, _FLIP_TIME, _ANIMATE_ON_SPAWN, _HIDE = 'shot_gun', 1, False, True


class PlayerSprite(ScreenSprite):
	def __init__(self, game, sprite_id=_SPRITE_ID, flip_time=_FLIP_TIME, animate_on_spawn=_ANIMATE_ON_SPAWN, hide=_HIDE):
		super().__init__(game=game, window=None, sprite_id=sprite_id, initial_mode='idle', color=(1,1,1,1), screen_size=(100,100),
							screen_pos=(100,100), hide=hide, flip_time=flip_time, start_iter=animate_on_spawn)
		
		self.init_size = controller_size()	
		self.init_pos = (scr_width() - controller_size()[0]) / 2, 0

		self.size = self.init_size
		self.pos = self.init_pos
		
	def re_size(self):
		super().re_size()

	def re_init(self, sprite_id=_SPRITE_ID, flip_time=_FLIP_TIME, animate_on_spawn=_ANIMATE_ON_SPAWN, hide=_HIDE):
		super().re_init(sprite_id=sprite_id, initial_mode='idle', color=(1,1,1,1), screen_size=(100,100), screen_pos=(100,100),
							hide=hide, flip_time=flip_time, start_iter=animate_on_spawn)
		
		self.size = controller_size()
		self.pos = (scr_width() - controller_size()[0]) / 2, 0
		
	def update(self, dt):
		super().update(dt)

	#<---- Update Func			
	def fbf_update(self, dt):
		super().fbf_update(dt)
		
	def timed_update(self):
		super().timed_update()
		
	#<---- Timed Update Func	
	def do_once_func(self):
		super().do_once_func()
		self.game.event.player_attack()
			
	def try_func(self):
		super().try_func()
		
	def stop_iteration_func(self):
		super().stop_iteration_func()
		
	#<---- Loop Controls	
	def start(self):
		super().start()
		
	def resume(self):		
		super().resume()
		
	def loop(self):
		super().loop()
		
	def stop(self):
		super().stop()
		
	#<---- Rect Functs
	def show(self):
		super().show()
				
	def hide(self):
		super().hide()
				
	def remove(self):
		super().remove()

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
