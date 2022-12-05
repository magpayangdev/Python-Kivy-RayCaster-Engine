
from scripts.bases.base import Base
from scripts.bases.window_objects.rect_base import RectBase

_COLOR, _NUM_RECTS, _SIZE, _POS, _OFFSET, _HIDE = (1,1,1,1), 2, (100,100), (0,0), 0, False

_PNG_L = lambda window, size, pos, offset: pos
_POS_L = lambda idx, size, pos, offset: pos
_SIZE_L = lambda idx, size, offset: size


class MultiRectBase(Base):
	""" Contains a tuple of unordered RectBase
			It is up to the children how to format the rectangles
				This class provides utils for bulk resize, show, hide and remove """
	def __init__(self, game, window, num_rects=_NUM_RECTS, 
					color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
						size_lambda=None, pos_lambda=None, positioning_lambda=None, hide=_HIDE):
	
		super().__init__(game=game)
		
		self.window=None
		if window:
			self.window = window
		else:
			self.window = self.game.window
			
		if not size_lambda:
			size_lambda = _SIZE_L
	
		if not pos_lambda:
			pos_lambda = _POS_L
			
		if not positioning_lambda:
			positioning_lambda = _PNG_L
		
		pos = positioning_lambda(self.window, size, pos, offset)
		
		self.rects = tuple(RectBase(self.game, self.window, color, size_lambda(idx, size, offset), pos_lambda(idx, size, pos, offset), hide) for idx in range(num_rects))
		
	#<----Properties
	@property
	def total_width(self):
		return self.rects[0].size[0]
		
	@property
	def total_height(self):
		return self.rects[0].size[1]
		
	@property
	def num_rects(self):
		return len(self.rects)
		
	@property
	def size(self):
		return self.rects[0].size
		
	@property
	def pos(self):
		return self.rects[0].pos

	@property
	def in_cnvs(self):
		return self.rects[0].in_cnvs
	
	#<----Multi Rect Funcs
	def set_rect_tansforms(self, idx, entry):
		pass
		
	def set_rect_color(self, idx, entry, use_texture=False):
		pass
				
	#<----Base Functions: re_init, update
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
						size_lambda=None, pos_lambda=None, positioning_lambda=None, hide=_HIDE):
	
		super().re_init()

		if not size_lambda:
			size_lambda = _SIZE_L
	
		if not pos_lambda:
			pos_lambda = _POS_L
			
		if not positioning_lambda:
			positioning_lambda = _PNG_L
		
		pos = positioning_lambda(self.window, size, pos, offset)
		
		[entry.re_init(size=size_lambda(idx, size, offset),
							 pos=pos_lambda(idx, size, pos, offset), color=color, hide=hide) for idx, entry in enumerate(self.rects)]
		
	def update(self,dt):
		super().update(dt)
		
		[entry.update(dt) for entry in self.rects]
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def show(self):
		[entry.show() for entry in self.rects]
			
	def hide(self):
		[entry.hide() for entry in self.rects]
			
	def remove(self):
		[entry.remove() for entry in self.rects]
	
		





















