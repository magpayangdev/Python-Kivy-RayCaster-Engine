
from scripts.bases.multi_rect_bases.multi_rect_base import MultiRectBase

_NUM_RECTS, _COLOR, _SIZE, _POS, _OFFSET, _HIDE = 2, (1,1,1,1), (250, 250), (0,0), 1, False

#_S_PROXY = lambda idx, size, offset: size - (2 * idx * offset)
#_P_PROXY = lambda idx, size, pos, offset: pos + (idx * offset)

#_S_L = lambda idx, size, offset: tuple(_S_PROXY(idx, s, offset) for s in size) 
#_P_L = lambda idx, size, pos, offset: tuple(_P_PROXY(idx, size, p, offset) for p in pos)


class NestedRect(MultiRectBase):
	def __init__(self, game, window, num_rects=_NUM_RECTS, size=_SIZE, pos=_POS, offset=_OFFSET, 
					positioning_lambda=None, hide=_HIDE):
				
		_S_PROXY = lambda idx, size, offset: size - (2 * idx * offset)
		_P_PROXY = lambda idx, size, pos, offset: pos + (idx * offset)
					
		size_lambda = lambda idx, size, offset: tuple(_S_PROXY(idx, s, offset) for s in size)
		pos_lambda = lambda idx, size, pos, offset: tuple(_P_PROXY(idx, size, p, offset) for p in pos)
					
		super().__init__(game=game, window=window, num_rects=num_rects, color=_COLOR, size=size, 
							pos=pos, size_lambda=size_lambda, pos_lambda=pos_lambda, 
								positioning_lambda=positioning_lambda, hide=hide)
								
	#<----Base Functions: re_init, update			
	def re_init(self, size=_SIZE, pos=_POS, offset=_OFFSET, positioning_lambda=None, hide=_HIDE):
	
		_S_PROXY = lambda idx, size, offset: size - (2 * idx * offset)
		_P_PROXY = lambda idx, size, pos, offset: pos + (idx * offset)
					
		size_lambda = lambda idx, size, offset: tuple(_S_PROXY(idx, s, offset) for s in size)
		pos_lambda = lambda idx, size, pos, offset: tuple(_P_PROXY(idx, size, p, offset) for p in pos)

		super().re_init(color=_COLOR, size=size, pos=pos, offset=offset, size_lambda=size_lambda, 
							pos_lambda=pos_lambda, positioning_lambda=positioning_lambda, hide=hide)
		
	def update(self,dt):
		pass
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):		
		return
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
