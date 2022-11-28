
from scripts.bases.game_bases.graph import Graph
from scripts.modules.graph import bfs

class GameGraph(Graph):
	def __init__(self, game, world_path=''):
		super().__init__(game=game, world_path=world_path)
		
		bfs.init(self.game, self)
	
		self.npc_locs = []
		
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)	
		
		self.npc_locs.clear()	
		
	#<----Getters
	def get_string(self, idx):
		return self.world.get_string(idx)
		
	def is_valid_position(self, world_x, world_y):
		return self.world.is_valid_position(world_x, world_y)
		
	def get_adjacent_nodes(self, key):
		return self.graph[key]

	#<----World Properties		
	@property
	def world_width(self):
		return self.world.width
		
	@property	
	def world_height(self):
		return self.world.height

	#<----
	def add_npc_location(self, in_loc):
		self.npc_locs.append(in_loc)































