"""
WorldRenderer
"""
from scripts.bases.multi_rect_bases.wall import Wall


class World(Wall):
	def __init__(self, game):
		super().__init__(game, window=None, hide=True)
						
	def re_size(self):
		super().re_size()
		
	def re_init(self):
		super().re_init()
				
	def update(self, idx, distance, P_x, P_y, angle, texture_idx, horizontal_scan=True):
		super().update(idx, distance, P_x, P_y, angle, texture_idx, horizontal_scan)
		
	def show(self):
		super().show()
				
	def hide(self):
		super().hide()
		
	def remove(self):
		super().remove()	
			

						