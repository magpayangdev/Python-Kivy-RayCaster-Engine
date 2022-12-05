
import random
from scripts.modules.textures import *
from scripts.modules.npc_scripts import npc_behavior
from scripts.modules.npc_scripts import npc_animation
from scripts.bases.base_sprites.scene_sprite import SceneSprite

_COLOR, _WORLD_POS, _SCALE, _HIDE = (1,1,1,1), (0,0), 0.5, False
_SPRITE_ID, _MINIMAP_ICON, _INITIAL_MODE = 'soldier', 'monster.png', 'idle'
_START_ITER, _HEALTH, _SPEED, _RADIUS, _ATK_DAMAGE, _ATK_RANGE = True, 1, 1, 0.1, 1, 1
_IDLE_INTERVAL, _WALK_INTERVAL, _HIT_INTERVAL, _DIE_INTERVAL, _ATK_INTERVAL = 1,1,1,1,1


class NPCSprite(SceneSprite):
	def __init__(self, game, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, initial_mode=_INITIAL_MODE, color=_COLOR, world_pos=_WORLD_POS, scale=_SCALE, hide=_HIDE, idle_interval=_IDLE_INTERVAL, walk_interval=_WALK_INTERVAL, hit_interval=_HIT_INTERVAL, die_interval=_DIE_INTERVAL, atk_interval=_ATK_INTERVAL, start_iter=_START_ITER, health=_HEALTH, speed=_SPEED, radius=_RADIUS, attack_damage=_ATK_DAMAGE, attack_range=_ATK_RANGE):
	
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon=minimap_icon, initial_mode=initial_mode, color=color, world_pos=world_pos, scale=scale, hide=hide, flip_time=idle_interval, start_iter=start_iter, health=health, speed=speed, radius=radius, influence_amount=attack_damage, influence_range=attack_range)

		#<----NPC Variables
		self.path = []
		self.next_node = 0,0
		self.sees_target = False
		self.current_action = initial_mode
		self.target_x, self.target_y = 0,0
		self.path_colour = 1, random.uniform(0, 1), random.uniform(0, 1)

		#<----Animation Sequences
		self.walk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'walk'))
		self.hit_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'hit'))
		self.die_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'death'))
		self.atk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'attack'))
		
		#<----Animation intervals
		self.idle_interval = idle_interval
		self.walk_interval = walk_interval
		self.hit_interval = hit_interval
		self.die_interval = die_interval
		self.atk_interval = atk_interval
		
		self.loop()

	#<----Base Functions: re_init, update
	def re_init(self, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, initial_mode=_INITIAL_MODE, color=_COLOR, world_pos=_WORLD_POS, scale=_SCALE, hide=_HIDE, idle_interval=_IDLE_INTERVAL, walk_interval=_WALK_INTERVAL, hit_interval=_HIT_INTERVAL, die_interval=_DIE_INTERVAL, atk_interval=_ATK_INTERVAL, start_iter=_START_ITER, health=_HEALTH, speed=_SPEED, radius=_RADIUS, attack_damage=_ATK_DAMAGE, attack_range=_ATK_RANGE):
	
		super().re_init(sprite_id=sprite_id, minimap_icon=minimap_icon, initial_mode=initial_mode, color=color, world_pos=world_pos, scale=scale, hide=hide, flip_time=idle_interval, start_iter=start_iter, health=health, speed=speed, radius=radius, influence_amount=attack_damage, influence_range=attack_range)

		#<----NPC Variables
		self.path = []
		self.next_node = 0,0
		self.sees_target = False
		self.current_action = initial_mode
		self.target_x, self.target_y = 0,0
		self.path_colour = 1, random.uniform(0, 1), random.uniform(0, 1)

		#<----Animation Sequences
		self.walk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'walk'))
		self.hit_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'hit'))
		self.die_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'death'))
		self.atk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'attack'))
		
		#<----Animation intervals
		self.idle_interval = idle_interval
		self.walk_interval = walk_interval
		self.hit_interval = hit_interval
		self.die_interval = die_interval
		self.atk_interval = atk_interval
		
		self.loop()
		
	def update(self, dt):
		super().update(dt)

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		#super().fbf_update(dt)
		npc_behavior.persistent_follow(self, dt)
		
	def timed_update(self):
		#super().timed_update()
		npc_animation.default_state_machine(self)	
		
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
		if self.current_action != 'die' and self.current_action != 'for delete':
			super().receive_damage(damage_amount)
			self.health -= damage_amount
			self.current_action = 'hurt'		