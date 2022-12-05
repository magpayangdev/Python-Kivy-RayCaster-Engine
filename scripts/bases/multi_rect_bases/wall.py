
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase
from scripts.modules.textures import *
from settings import *

_COLOR, _NUM_RECTS, _HIDE = (1,0,1,0), NUMBER_OF_RAYS, False

class Wall(MultiRectBase):
	""" Individual Rectangle Elements are resized, repositioned, and retextured, 
			independently of each other, per frame """
	def __init__(self, game, window, hide=False):
		super().__init__(game, window, num_rects=_NUM_RECTS, color=_COLOR, hide=hide)
		
		self.scr_rect_w = 0
		self.half_scr_h = 0
		self.scr_dist = 0
		
		self.scr_rect_w = scr_rect_w()
		self.half_scr_h = half_scr_h()
		self.scr_dist = scr_distance()
		
	#<----Base Functions: re_init, update			
	def re_init(self, hide=_HIDE):
		super().re_init(color=_COLOR, hide=hide)
		
		self.scr_rect_w = scr_rect_w()
		self.half_scr_h = half_scr_h()
		self.scr_dist = scr_distance()
		
	def update(self, idx, distance, P_x, P_y, angle, texture_idx, horizontal_scan=True):
		#DO NOT RUN SUPER ON UPDATE# super().update(dt)
			
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
			rect.colour.rgba = c,c,c,1
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
































