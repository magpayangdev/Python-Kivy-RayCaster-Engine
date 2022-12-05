
import os
from scripts.bases.base import Base

_WORLD_PATH = 'scripts/resources/docs/default_world_map.txt'


class World(Base):
	""" Class that holds the data about world the game is currently in """
	def __init__(self, game, world_path='', **kwargs):
		super().__init__(game=game)
		
		self.graph = {}
		self.width = 0
		self.height = 0
		self.string = ''
		self.world_path = _WORLD_PATH
		
		if os.path.isfile(world_path):
			self.world_path = world_path
		
		self.set_world_dimensions()
	
	#<----Base Functions: re_init, update		
	def re_init(self, world_path = '', **kwargs):
		super().re_init()
		self.graph = {}
		self.width = 0
		self.height = 0
		self.string = ''
		self.world_path = _WORLD_PATH
		
		if os.path.isfile(world_path):
			self.world_path = world_path
		
		self.set_world_dimensions()
				
	def update(self, dt):
		super().update(dt)
		
	#<----Getters
	def get_string(self, idx):
		return self.string[idx]

	def is_valid_position(self, Px, Py):	
		idx = int(Px) + int(Py) * self.width
		
		return True if self.get_string(idx) == '.' else False

	#<-----Initializer		
	def set_world_dimensions(self):
		with open(self.world_path) as f:
			self.width = len(f.readline())
			
		with open(self.world_path) as f:
			self.height = len(f.read()) // self.width
			
		with open(self.world_path) as f:
			self.string = f.read()
			
			if self.string[-1] != '\n':
				self.string += '\n'
				
				self.height += 1


