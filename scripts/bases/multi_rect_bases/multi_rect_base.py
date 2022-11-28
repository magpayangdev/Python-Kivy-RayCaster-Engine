
from scripts.bases.base import Base
from scripts.bases.window_objects.rect_base import RectBase
#from kivy.graphics.context_instructions import Color
#from kivy.graphics.vertex_instructions import Rectangle	


class MultiRectBase(Base):
	""" Contains a tuple of unordered RectBase
			It is up to the children how to format the rectangles
				This class provides utils for bulk resize, show, hide and remove """	
	def __init__(self, game, window, color=(1,1,1,1), num_rects=2, size=(100,100), pos=(0,0), offset=0, hide=False):
	
		super().__init__(game=game)
		self.in_cnvs = False	
		
		self.window=None
		if window:
			self.window = window
		else:
			self.window = self.game.window	

		self.num_rects = num_rects
		self.size = size
		self.pos = pos
		self.color = color
		self.offset = offset
		
		self.rects = tuple(RectBase(self.game, self.window, color, size, pos, hide) for _ in range(num_rects))
		self.in_cnvs = True
			
		if hide:
			self.hide()
			
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		[entry.re_init() for entry in self.rects]
		
	def update(self,dt):
		super().update(dt)
		
		[entry.update(dt) for entry in self.rects]
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		[entry.re_size() for entry in self.rects]
		
	def show(self):
		[entry.show() for entry in self.rects]
		self.in_cnvs = True
			
	def hide(self):
		[entry.hide() for entry in self.rects]
		self.in_cnvs = False
			
	def remove(self):
		[entry.remove() for entry in self.rects]
	
		





















