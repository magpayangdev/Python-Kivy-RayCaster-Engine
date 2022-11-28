
import os
from scripts.bases.base import Base


class World(Base):
	""" Class that holds the data about world the game is currently in """
	def __init__(self, game, path=''):
		super().__init__(game=game)
		
		self.graph = {}
				
		self.width = 0
		self.height = 0
		self.string = ''
		
		self.path = 'scripts/resources/docs/default_world_map.txt'

		if os.path.isfile(path):
			self.path = path
		
		self.set_world_dimensions()
	
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
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
		with open(self.path) as f:
			self.width = len(f.readline())
			
		with open(self.path) as f:
			self.height = len(f.read()) // self.width
			
		with open(self.path) as f:
			self.string = f.read()
			
			if self.string[-1] != '\n':
				self.string += '\n'
				
				self.height += 1


