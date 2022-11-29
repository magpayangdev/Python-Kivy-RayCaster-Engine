

from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase

class ArrayRect(MultiRectBase):
	def __init__(self, game, window, num_rects=3, size=(100,100), pos=(0,0), offset=1, hide=False):

		super().__init__(game=game, window=window, color=(1,1,1,1), num_rects=num_rects, size=size, pos=pos, offset=offset, hide=hide)
		
		fpos = lambda idx: (self.pos[0] + (self.offset + self.size[0]) * idx, self.pos[1])
		for idx, entry in enumerate(self.rects):
			entry.rect.size = self.size
			entry.rect.pos = fpos(idx)
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.re_size()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		fpos = lambda idx: (self.pos[0] + (self.offset + self.size[0]) * idx, self.pos[1])
		for idx, entry in enumerate(self.rects):
			entry.rect.size = self.size
			entry.rect.pos = fpos(idx)
							
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
			

