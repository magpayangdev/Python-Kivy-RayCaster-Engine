
from scripts.bases.base_sprites.scene_sprite import SceneSprite
from scripts.modules.npc_scripts import npc_behavior
from scripts.modules.npc_scripts import npc_animation
from scripts.modules.textures import *
import random


class NPCSprite(SceneSprite):
	def __init__(self, game, sprite_id='soldier', minimap_icon='monster.png', initial_mode='idle', color=(1,1,1,1), world_pos=(100,100), scale=0.5, hide=False, idle_interval=1, walk_interval=1, hit_interval=1, die_interval=1, atk_interval=1, start_iter=True, health=1, speed=1, radius=0.1, attack_damage=1, attack_range=1):
	
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon=minimap_icon, initial_mode=initial_mode, color=color, world_pos=world_pos, scale=scale, hide=hide, flip_time=idle_interval, start_iter=start_iter, health=health, speed=speed, radius=radius, influence_amount=attack_damage, influence_range=attack_range)

		#<----NPC Variables
		self.path = []
		self.next_node = 0,0
		self.sees_target = False
		self.current_action = initial_mode
		self.target_x, self.target_y = 0,0
		self.path_colour = 1, random.uniform(0, 1), random.uniform(0, 1)

		#<----Animation Sequences
		self.walk_i_seq = (image for image in get_image_sequence(self.init_img_seq_id, 'walk'))
		self.hit_i_seq = (image for image in get_image_sequence(self.init_img_seq_id, 'hit'))
		self.die_i_seq = (image for image in get_image_sequence(self.init_img_seq_id, 'death'))
		self.atk_i_seq = (image for image in get_image_sequence(self.init_img_seq_id, 'attack'))
		
		#<----Animation intervals
		self.idle_interval = idle_interval
		self.walk_interval = walk_interval
		self.hit_interval = hit_interval
		self.die_interval = die_interval
		self.atk_interval = atk_interval
		
		self.loop()

	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
		
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