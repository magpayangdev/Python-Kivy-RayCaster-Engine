"""
sprite
"""
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.image import Image

import os
import math
import random
from collections import deque

from settings import * 
from scripts.game.textures import *    

from scripts.scene_objects.sprite_scripts import npc_animation	
from scripts.scene_objects.sprite_scripts import npc_behavior
from scripts.base_classes.base_sprite import SceneSprite

class StaticSprite(SceneSprite):
	def __init__(self, game, sprite_id='static_sprite', 
				pos=(0,0), radius=0.1, angle=0, scale=0.5, icon='cherry.png'):
		super().__init__(game, sprite_id=sprite_id, 
				pos=pos, radius=radius, angle=angle, scale=scale, icon=icon, hide=False)
				
		with self.window.canvas:
			self.mmp_colour = Color(1,1,1)
			self.mmp_rect = Rectangle(size=(c_block_size(),c_block_size()), texture=get_map_texture(icon))
			self.in_mmp_cnvs = True
	
class AnimatedSprite(StaticSprite):
	""" Handles idle image transistions """
	def __init__(self, game, sprite_id="anim_sprite", pos=(0,0), radius=0.1, angle=0, scale=0.5, icon='fire.png', idle_interval=0.1):
		super().__init__(game, sprite_id, pos, radius, angle, scale, icon)
		self.acc_time = 0.0		
		self.for_del_cntr = 0.0	
		self.f_del_dur = 3
		self.idle_interval = idle_interval									  
		self.anim_interval = self.idle_interval										
		self.idle_i_seq = (image for image in get_image_sequence(self.img_seq_id))
		
	def update(self, dt):
		self.acc_time += dt
		self.fbf_update(dt)
				
		if self.acc_time > self.anim_interval:
			self.acc_time = 0.0
			self.timed_update()
			
	def fbf_update(self,dt):
		pass
		
	def timed_update(self):
		npc_animation.idle_animation(self)	

	def receive_damage(self, damage_amount=1):
		pass

class NPCSprite(AnimatedSprite):
	""" Has additional actions and animation sequences other than idle """
	def __init__(self, game, sprite_id='npc_sprite', pos=(0,0), radius=0.2, angle=0, scale=0.5, icon='monster.png', idle_interval=0.5, walk_interval=0.4, hit_interval=0.2, die_interval=0.08, atk_interval=0.1, health=3, atk_damage=1, atk_range=3, speed=0.5):					
		super().__init__(game, sprite_id, pos, radius, angle, scale, icon, idle_interval)
		self.health = health
		self.speed = speed
		self.atk_range = atk_range
		self.atk_damage = atk_damage
		self.path_colour = 1, random.uniform(0, 1), random.uniform(0, 1)
		
		self.target_x, self.target_y = 0,0
		self.str=''
		self.dist=0
		self.i = 0
				
		self.next_node	  = 0,0
		self.sees_target	= False
		self.current_action = 'idle'
		self.path 	      = []
			
		self.walk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'walk'))
		self.hit_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'hit'))
		self.die_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'death'))
		self.atk_i_seq = (image for image in get_image_sequence(self.img_seq_id, 'attack'))
		
		self.walk_interval = walk_interval
		self.hit_interval = hit_interval
		self.die_interval = die_interval
		self.atk_interval = atk_interval
				
	def update(self, dt):
		super().update(dt)

	def fbf_update(self,dt):
		npc_behavior.persistent_follow(self, dt)
		
	def timed_update(self):
		npc_animation.default_state_machine(self)
					
	def receive_damage(self, damage_amount=1):
		if self.current_action != 'die' and self.current_action != 'for delete':
			super().receive_damage(damage_amount)
			self.health -= damage_amount
			self.current_action = 'hurt'
					