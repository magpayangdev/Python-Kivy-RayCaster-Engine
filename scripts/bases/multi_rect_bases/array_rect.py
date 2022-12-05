
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase

_NUM_RECTS, _COLOR, _SIZE, _POS, _OFFSET, _HIDE = 3, (1,1,1,1), (100,100), (0,0), 0, False


class ArrayRect(MultiRectBase):
	def __init__(self, game, window, num_rects=_NUM_RECTS, 
					color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
						size_lambda=None, positioning_lambda=None, hide=_HIDE):
		
		pos_lambda = lambda idx, size, pos, offset: (pos[0] + (offset + size[0]) * idx, pos[1])
		
		super().__init__(game=game, window=window, num_rects=num_rects, 
							color=color, size=size, pos=pos, offset=offset, 
								size_lambda=size_lambda, pos_lambda=pos_lambda, positioning_lambda=positioning_lambda, hide=hide)
								
	#<----Base Functions: re_init, update
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
					size_lambda=None, positioning_lambda=None, hide=_HIDE):
		
		pos_lambda = lambda idx, size, pos, offset: (pos[0] + (offset + size[0]) * idx, pos[1])
		
		super().re_init(color=color, size=size, pos=pos, offset=offset, 
							size_lambda=size_lambda, pos_lambda=pos_lambda, positioning_lambda=positioning_lambda, hide=hide)
								
	def update(self,dt):
		super().update(dt)

	#<----Properties		
	@property
	def total_width(self):
		return (self.rects[0].size[0] + self.offset) * self.num_rects
		
	@property
	def total_height(self):
		return self.rects[0].size[1]
		
	#<----Rectangle Functions: re_size, show, hide, remove							
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
			

