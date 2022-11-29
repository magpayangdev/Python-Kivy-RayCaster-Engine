
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase

class NestedRect(MultiRectBase):
	def __init__(self, game, window, num_rects=2, size=(250,250), pos=(0,0), offset=1, hide=False):

		super().__init__(game=game, window=window, color=(1,1,1,1), num_rects=num_rects, size=size, pos=pos, offset=offset, hide=hide)
		
		self.size = size
		self.pos = (0, 0)
		self.offset = offset
		self.center = self.pos

		for idx, entry in enumerate(self.rects):
			f = lambda i,s: s - (2 * i * self.offset)
			entry.rect.size = tuple(f(idx, s) for s in self.size)
			
			g = lambda idx,p: p + (idx * self.offset)
			entry.rect.pos = tuple(g(idx, p) for p in self.pos)
								
	#<----Base Functions: re_init, update			
	def re_init(self):
		pass
		
	def update(self,dt):
		pass
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):				
		for idx, entry in enumerate(self.rects):
			f = lambda i,s: s - (2 * i * self.offset)
			entry.rect.size = tuple(f(idx, s) for s in self.size)
			
			g = lambda idx,p: p + (idx * self.offset)
			entry.rect.pos = tuple(g(idx, p) for p in self.pos)
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
