
from scripts.bases.timed_updates.timed_image_sequence import TimedImageSequence
from scripts.bases.window_objects.textured_rect import TexturedRect
from scripts.modules.textures import *
import random


class SceneSprite(TimedImageSequence):
	""" Canvas is always from game.sprite_space
			Precalculated projection constants """
	def __init__(self, game, sprite_id='shot_gun', minimap_icon='cherry.png', initial_mode='idle', color=(1,1,1,1), world_pos=(100,100), scale=1, hide=False, flip_time=1, start_iter=False, speed=1, health=1, radius=0.1, influence_amount=1, influence_range=1):
		super().__init__(game=game, window=game.sprite_space, img_seq_id=sprite_id, initial_mode=initial_mode, color=color, size=(100,100), pos=world_pos, hide=False, flip_time=flip_time, start_iter=start_iter)
		
		#<----References
		self.event = self.game.event
		
		#<----Sprite Attributes (as world objects)
		self.speed = speed
		self.health = health
		self.radius = radius
		self.influence_range = influence_range
		self.influence_amount = influence_amount
		
		#<----Porjection Variables
		self.angle = 0
		self.f_del_dur = 3
		self.d_f_player = 0.0
		self.for_del_cntr = 0.0
		self.pos_x, self.pos_y = world_pos[0], world_pos[1]
		
		#<----Projection Constants
		sample_texture = get_image_sequence(self.img_seq_id)[0]
		self.IMAGE_RATIO = sample_texture.width / sample_texture.height
		self.SCALE_FACTOR = scale * screen_distance()	
		
		#<----Minimaps
		self.minimap_icon = TexturedRect(game=self.game, window=self.game.window, image_name=minimap_icon, image_category='map', color=(1,1,1,1), size=(c_block_size(),c_block_size()), pos=(100,0), hide=False)
		
		if hide:
			self.hide()
			
			self.minimap_icon.hide()

	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
		
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
		self.minimap_icon.remove()
		
		del(self.minimap_icon)

	#<----Textures Functions: reload, change mode
	def reload_texture(self):
		super().reload_texture()
		
	def change_mode(self, new_mode):
		super().change_mode(new_mode)
		
	#<----Projection Functions: project on screen
	def project_on_screen(self, idx):		
		proj_ratio = self.SCALE_FACTOR / self.d_f_player	
		proj_width, proj_height = self.IMAGE_RATIO * proj_ratio, proj_ratio
		
		self.size = proj_width, proj_height
		self.pos = idx * scr_rect_w() - proj_width // 2, half_scr_h() - proj_height
		
	def receive_damage(self, damage_amount=1):
		pass		
		
		
		
		