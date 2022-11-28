
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase
from scripts.modules.textures import *
from settings import *

class Wall(MultiRectBase):
	""" Individual Rectangle Elements are resized, repositioned, and retextured, 
			independently of each other, per frame """
	def __init__(self, game, window, hide=False):

		super().__init__(game, window, color=(1,1,1,1), num_rects=NUMBER_OF_RAYS, size=(100,100), pos=(0,0), offset=0, hide=hide)
		
		self.scr_rect_w = 0
		self.half_scr_h = 0
		self.scr_dist = 0
		
		self.scr_rect_w = scr_rect_w()
		self.half_scr_h = half_scr_h()
		self.scr_dist = scr_distance()
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		#super().re_init() do not call super().re_init
		
		self.scr_rect_w = scr_rect_w()
		self.half_scr_h = half_scr_h()
		self.scr_dist = scr_distance()
		
	def update(self, idx, distance, P_x, P_y, angle, texture_idx, horizontal_scan=True):
		#super().update(dt) do not call super().update
			
		rect = self.rects[idx]
		wt = get_wall_texture(texture_idx)

		w, h = self.scr_rect_w, self.scr_dist / distance
		Px, Py = idx * self.scr_rect_w, self.half_scr_h - h / 2
		c = 70_100 / (100_000 + 2 * distance ** 5)

		if horizontal_scan:
			if math.cos(angle) >= 0:
				o = (P_y % 1)
			else:
				o = 1 - (P_y % 1)
		else:
			if math.sin(angle) >= 0:
				o = (P_x % 1)
			else:
				o = 1 - (P_x % 1)

		rect.rect.size = w, h
		rect.rect.pos = Px, Py

		if True:
			rect.colour.rgb = c,c,c
			rect.rect.texture = wt.get_region((wt.width - w) * o , 0, w, wt.height)
	
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
				
	def show(self):
		super().show()
					
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()
































