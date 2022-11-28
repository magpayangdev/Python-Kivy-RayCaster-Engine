""" Sprite Behaviour """
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from scripts.modules.engine import ray_caster
from scripts.modules.npc_scripts.npc_helper_functions import *


def persistent_follow(npc, dt):
		""" Starts at idle. When sees player, consistenly follows until conditions meet, then attack """
		npc.sees_target, npc.target_x, npc.target_y = ray_caster.can_see_player(npc)
		#return
		
		if npc.current_action == 'die':								#<---- Death
			return
		
		elif npc.current_action == 'hurt':							 #<---- Hurt
			npc.game.graph_mngr.add_npc_location((int(npc.pos_x), int(npc.pos_y)))
			return
			
		elif npc.current_action == 'idle':							 #<---- Idle
			npc.game.graph_mngr.add_npc_location((int(npc.pos_x), int(npc.pos_y)))
			 
			if npc.sees_target:
				if is_player_in_range(npc):
					npc.current_action = 'attack'
					
				else:
					npc.current_action = 'walking'			
			
		elif npc.current_action == 'walking':						  #<---- Walking
			npc.game.graph_mngr.add_npc_location((int(npc.pos_x), int(npc.pos_y)))

			move_to_next_node(npc, dt)
			
			if is_player_in_range(npc):
				if npc.sees_target:
					npc.current_action = 'attack'
					npc.path.clear()
						
				else:
					pass	#<---- Keep Moving
						
			else:
				pass		#<---- Keep Moving
			
		elif npc.current_action == 'attack':							#<---- Attacking
			npc.game.graph_mngr.add_npc_location((int(npc.pos_x), int(npc.pos_y)))
			
			if not npc.sees_target:
				npc.current_action = 'walking'
				
			else:
				if is_player_in_range(npc):
					pass
				else:
					npc.current_action = 'walking'
					
		elif npc.current_action == 'for delete':
			npc.for_del_cntr += dt
			
			if npc.for_del_cntr > npc.f_del_dur:
				npc.for_del_cntr = 0
				npc.event.sprite_for_delete(npc)
			
		else:
			raise Exception('Invalid current action string value!')