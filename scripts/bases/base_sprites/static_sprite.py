
from scripts.bases.base_sprites.scene_sprite import SceneSprite

_SPRITE_ID, _MINIMAP_ICON, _WORLD_POS = 'candle_bra', 'cherry.png', (0,0)
_RADIUS, _SCALE, _HEALTH, _INFLUENCE_RANGE, _INFLUENCE_AMOUNT, _HIDE = 0.1, 0.5, 10, 1, 1, False


class StaticSprite(SceneSprite):
	def __init__(self, game, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, world_pos=_WORLD_POS, 
					radius=_RADIUS, scale=_SCALE, health=_HEALTH, influence_range=_INFLUENCE_RANGE, 
						influence_amount=_INFLUENCE_AMOUNT, hide=_HIDE):
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon=minimap_icon, initial_mode='idle',
							color=(1,1,1,1), world_pos=world_pos, scale=scale, hide=hide, flip_time=999,
								start_iter=False, speed=0, health=health, radius=radius, 
									influence_amount=influence_amount, influence_range=influence_range)
		
		self.stop()
	
	#<----Base Functions: re_init, update
	def re_init(self, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, world_pos=_WORLD_POS, radius=_RADIUS,
					scale=_SCALE, health=_HEALTH, influence_range=_INFLUENCE_RANGE, influence_amount=_INFLUENCE_AMOUNT,
						hide=_HIDE):
		super().re_init(sprite_id=sprite_id, minimap_icon=minimap_icon, initial_mode='idle', color=(1,1,1,1),
							world_pos=world_pos, scale=scale, hide=hide, flip_time=999, start_iter=False, speed=0,
								health=health, radius=radius, influence_amount=influence_amount, influence_range=influence_range)
		
		self.stop()
		
	def update(self, dt):
		super().update(dt)

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
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()

	#<----Textures Functions: reload, change mode
	def reload_texture(self):
		super().reload_texture()
		
	def change_mode(self, new_mode):
		super().change_mode(new_mode)
		
	#<----Projection Functions: project on screen
	def project_on_screen(self, idx):		
		super().project_on_screen(idx)
				
	def receive_damage(self, damage_amount=1):
		super().receive_damage(damage_amount)
		