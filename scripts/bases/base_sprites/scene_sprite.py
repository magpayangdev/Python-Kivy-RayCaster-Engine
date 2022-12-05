
from scripts.bases.timed_updates.timed_image_sequence import TimedImageSequence
from scripts.bases.window_objects.textured_rect import TexturedRect
from scripts.modules.textures import *
import random

_FLIP_TIME, _START_ITER = 1, False
_MMP_IMAGE_CATEGORY = 'map'
_COLOR, _WORLD_POS, _SCALE, _HIDE = (1,1,1,1), (0,0), 1, False
_SPRITE_ID, _MINIMAP_ICON, _INITIAL_MODE = 'soldier', 'monster.png', 'idle'
_SPEED, _HEALTH, _RADIUS, _INFLUENCE_AMOUNT, _INFLUENCE_RANGE = 1, 1, 0.1, 1, 1
_MMP_COLOR, _MMP_SIZE, _MMP_POS, _MMP_HIDE = (1,1,1,1), (c_block_size(), c_block_size()), (0,0), True


class SceneSprite(TimedImageSequence):
	""" Canvas is always from game.sprite_space
			Precalculated projection constants """
	def __init__(self, game, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, initial_mode=_INITIAL_MODE, color=_COLOR,
					world_pos=_WORLD_POS, scale=_SCALE, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER, speed=_SPEED,
						health=_HEALTH, radius=_RADIUS, influence_amount=_INFLUENCE_AMOUNT, influence_range=_INFLUENCE_RANGE):
		super().__init__(game=game, window=game.sprite_space, img_seq_id=sprite_id, initial_mode=initial_mode,
							color=color, pos=world_pos, hide=hide, flip_time=flip_time, start_iter=start_iter)
		
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
		self.d_f_player = 9999
		self.for_del_cntr = 0.0
		self.pos_x, self.pos_y = world_pos[0], world_pos[1]
		
		#<----Projection Constants
		sample_texture = get_image_sequence(self.img_seq_id)[0]
		self.IMAGE_RATIO = sample_texture.width / sample_texture.height
		self.SCALE_FACTOR = scale * screen_distance()	
		
		#<----Minimaps
		mmp_icon_hide=_MMP_HIDE
		if self.game.minimap:
			mmp_icon_hide = not self.game.minimap.in_cnvs

		self.minimap_icon = TexturedRect(game=self.game, window=self.game.window, image_name=minimap_icon,
											image_category=_MMP_IMAGE_CATEGORY, color=_MMP_COLOR, size=_MMP_SIZE, 
												pos=_MMP_POS, hide=mmp_icon_hide)

	#<----Base Functions: re_init, update
	def re_init(self, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, initial_mode=_INITIAL_MODE, color=_COLOR,
					world_pos=_WORLD_POS, scale=_SCALE, hide=_HIDE, flip_time=_FLIP_TIME, start_iter=_START_ITER,
						speed=_SPEED, health=_HEALTH, radius=_RADIUS, influence_amount=_INFLUENCE_AMOUNT,
							influence_range=_INFLUENCE_RANGE):
		super().re_init(img_seq_id=sprite_id, initial_mode=initial_mode, color=color, pos=world_pos, hide=hide,
							flip_time=flip_time, start_iter=start_iter)
		
		#<----Sprite Attributes (as world objects)
		self.speed = speed
		self.health = health
		self.radius = radius
		self.influence_range = influence_range
		self.influence_amount = influence_amount
		
		#<----Porjection Variables
		self.angle = 0
		self.f_del_dur = 3
		self.d_f_player = 9999
		self.for_del_cntr = 0.0
		self.pos_x, self.pos_y = world_pos[0], world_pos[1]
		
		#<----Projection Constants
		sample_texture = get_image_sequence(self.img_seq_id)[0]
		self.IMAGE_RATIO = sample_texture.width / sample_texture.height
		self.SCALE_FACTOR = scale * screen_distance()
					
		#<----Minimaps
		mmp_icon_hide=_MMP_HIDE
		if self.game.minimap:
			mmp_icon_hide = not self.game.minimap.in_cnvs
			
		self.minimap_icon.re_init(image_name=_MMP_IMAGE_NAME, image_category=minimap_icon,
									color=_MMP_COLOR, size=_MMP_SIZE, pos=_MMP_POS, hide=mmp_icon_hide)
		
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
		
		
		
		