
from scripts.modules.graph import coord_converter as coord_cnvrtr
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase
from settings import *

class Grid(MultiRectBase):
	""" individual elememts are positioned and size at init once
			colour are updated every frame to get the illusion of scrolling """
	def __init__(self, game, window, num_rects, size, hide=False):

		super().__init__(game=game, window=window, color=(1,1,1,1), num_rects=num_rects, size=size, pos=(0,0), offset=0, hide=hide)
	
		self.scale_x, self.scale_y = 0,0
		self.offset_x, self.offset_y = 0,0
		
		self.scr_width = 0
		self.scr_height = 0
		
		self.width = 0
		self.height = 0
		self.half_width = 0
		self.half_height = 0

		self.re_init()
		self.re_size()
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		
		self.scale_x, self.scale_y = g_block_size()
		self.offset_x, self.offset_y = map_centre_o()
		
		self.scr_width = NUMBER_OF_BLOCKS_ACROSS * self.scale_x
		self.scr_height = NUMBER_OF_BLOCKS_ACROSS * self.scale_y
		
		self.width = NUMBER_OF_BLOCKS_ACROSS
		self.height = NUMBER_OF_BLOCKS_DOWN
		self.half_width = NUMBER_OF_BLOCKS_ACROSS / 2
		self.half_height = NUMBER_OF_BLOCKS_DOWN / 2
			
	def update(self,dt):
		super().update(dt)
		
		for idx, entry in enumerate(self.rects):
			self.set_block_colour(entry, idx, False)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		#super().re_size()
		
		for idx, entry in enumerate(self.rects):
			self.set_block_transforms(entry, idx)
			self.set_block_colour(entry, idx, False)
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
		
	def flip(self):
		if self.in_cnvs:
			self.hide()
		else:
			self.show()

	def set_block_transforms(self, rect, idx):
		col = idx % self.width
		row = idx // self.height
		
		Px = (col + 0.1) * self.scale_x + self.offset_x
		Py = (self.height - 0.9 - row) * self.scale_y + self.offset_y

		rect.rect.size = n_block_size()
		rect.rect.pos  = Px, Py 
		
	def set_block_colour(self, rect, idx, use_texture=False):
		gx, gy = coord_cnvrtr.grid_idx_to_grid(idx)
		wx, wy = coord_cnvrtr.grid_to_world(gx, gy, self.game.player.pos_x + 0.5, self.game.player.pos_y + 0.5)

		w_string = self.game.graph_mngr.get_string(int(wx) + int(wy) * self.game.graph_mngr.world_width)

		if use_texture:          
			if w_string in '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' : 
				rect.texture = get_map_texture('brick_wall.png')
			
			elif w_string == ".": 
				rect.rect.texture = get_map_texture('brick_wall.png')
			
			else: 
				colour.rgb = MAP_INVALID_COLOUR
		else:
			if w_string in '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' : 
				rect.colour.rgb = BROWN
			
			elif w_string == ".": 
				rect.colour.rgb = MAP_FLOOR_COLOUR
			
			else: 
				rect.colour.rgb = MAP_INVALID_COLOUR	

