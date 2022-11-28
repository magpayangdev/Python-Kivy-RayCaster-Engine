""" npc animations """
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from scripts.bases.base_sprites.scene_sprite import SceneSprite
from scripts.modules.textures import *

def idle_animation(npc):
	try:
		npc.rect.texture = next(npc.idle_i_seq)

	except StopIteration:
		npc.idle_i_seq = (image for image in get_image_sequence(npc.init_img_seq_id))
		npc.rect.texture = next(npc.idle_i_seq)

def default_state_machine(npc):
	""" Default npc animation routine """
	if npc.current_action == 'die':						#<---- Death Anim
		npc.flip_time = npc.die_interval
		try:
			npc.rect.texture = next(npc.die_i_seq)

		except StopIteration:
			npc.path.clear()
			npc.event.sprite_has_died(npc)
			npc.current_action = 'for delete'
					
	elif npc.current_action == 'hurt':					 #<---- Hurt Anim
		npc.flip_time = npc.hit_interval
		try:
			npc.rect.texture = next(npc.hit_i_seq)
			
		except StopIteration:				
			npc.event.sprite_hit()
			
			npc.hit_i_seq = (image for image in get_image_sequence(npc.init_img_seq_id, 'hit'))
			npc.rect.texture = next(npc.hit_i_seq)
			npc.current_action = 'walking'

		if npc.health <= 0:
			npc.current_action = 'die'
			
			
	elif npc.current_action == 'idle':					 #<---- Idle Anim
		npc.flip_time = npc.idle_interval
		super(SceneSprite, npc).timed_update()
			
	elif npc.current_action == 'walking':				  #<---- Death Anim
		npc.flip_time = npc.walk_interval
		try:
			npc.rect.texture = next(npc.walk_i_seq)
			
		except StopIteration:
			npc.walk_i_seq = (image for image in get_image_sequence(npc.init_img_seq_id, 'walk'))
			npc.rect.texture = next(npc.walk_i_seq)
			
	elif npc.current_action == 'attack':				   #<---- Attack Anim
		npc.flip_time = npc.atk_interval
		try:
			npc.rect.texture = next(npc.atk_i_seq)
				
		except StopIteration:
			npc.event.sprite_attack(npc)				

			npc.atk_i_seq  = (image for image in get_image_sequence(npc.init_img_seq_id, 'attack'))
			npc.rect.texture = next(npc.atk_i_seq)
			
	elif npc.current_action == 'for delete':
		pass
		
	else:
		raise Exception('Invalid current action string value!')