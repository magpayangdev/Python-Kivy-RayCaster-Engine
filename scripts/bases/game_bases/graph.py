
from scripts.bases.base import Base
from scripts.bases.game_bases.world import World
from scripts.modules.graph import coord_converter

_WORLD_PATH = 'scripts/resources/docs/default_world_map.txt'


class Graph(Base):
	def __init__(self, game, world_path=_WORLD_PATH, **kwargs):
		""" Contains the tree representation of the world """
		super().__init__(game=game)
		
		self.world = World(game=self.game, world_path=world_path)

		coord_converter.init(self.game, self)
		
		self.graph={}		
		self.create_graph()
		
	#<----Base Functions: re_init, update		
	def re_init(self, world_path=_WORLD_PATH, **kwargs):
		super().re_init()
		
		self.world.re_init(world_path=world_path)
		
		coord_converter.init(self.game, self)
		
		self.graph={}		
		self.create_graph()
				
	def update(self, dt):
		super().update(dt)		
		
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

	#<----Initializers
	def create_graph(self):	
		self.graph.clear()
		
		VALID_DIRECTIONS = [-1, 0], [0, -1], [1, 0], [0, 1]
		
		f = lambda x,y: [(x+dx, y+dy) for dx, dy in VALID_DIRECTIONS if self.is_valid_position(x+dx, y+dy)]
		
		for i in range(self.world.width * self.world.height):
			x, y = i %  self.world.width, i // self.world.width
			
			if self.is_valid_position(x, y):
				self.graph[(x, y)] = self.graph.get((x, y), []) + f(x, y)		
