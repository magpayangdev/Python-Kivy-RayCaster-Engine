
import os
import csv
#from scripts.scene_objects.sprite_scripts.sprite import *
from scripts.screen_objects.sprites import *
from settings import *

_DEFAULT_PATH = 'scripts/scene_objects/resources/docs/default_sprites_list.csv'

def init(load_list):
	file_name = _DEFAULT_PATH
	
	if os.path.isfile(WORLD_OBJECTS_LIST):
		file_name = WORLD_OBJECTS_LIST

	with open(file_name, newline='') as f:
		f_reader = csv.reader(f)
	
		next(f_reader)
		for row in f_reader:
			f = lambda x,y: (float(x), float(y))		
			try:
				load_list.append((row[0], row[1], f(row[2], row[3])))	
			except Exception:
				pass

def load_objects(game, load_list, all_sprites):
	for idx, entry in enumerate(load_list):
		if entry[0][0] == '#':
			continue 

		if entry[0] == 'static_sprite':
			if game.graph_mngr.is_valid_position(*entry[2]):
				sprt = DefaultStaticSprite(game, sprite_id=entry[1], world_pos = entry[2])
				all_sprites.append(sprt)
					
			else:
				raise Exception('Conflict detected in sprite location {} {}'.format(entry[0], entry[2]))
						
		elif entry[0] == 'animated_sprite':
			if game.graph_mngr.is_valid_position(*entry[2]):
				sprt = DefaultAnimatedSprite(game, sprite_id=entry[1], world_pos = entry[2])
				all_sprites.append(sprt)
					
			else:
				raise Exception('Conflict detected in animated sprite location {} {}'.format(entry[0], entry[2]))
					
		elif entry[0] == 'npc_sprite':
			if game.graph_mngr.is_valid_position(*entry[2]):
				sprt = DefaultNPCSprite(game, sprite_id=entry[1], world_pos = entry[2])
				all_sprites.append(sprt)
						
			else:
				raise Exception('Conflict detected in npc sprite location {} {}'.format(entry[0], entry[2]))
				
		else:
			raise Exception('Invalid sprite type!: at index: {} entry name: {}'.format(idx, entry[0]))