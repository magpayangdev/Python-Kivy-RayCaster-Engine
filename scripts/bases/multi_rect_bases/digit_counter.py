
from scripts.bases.multi_rect_bases.array_rect import ArrayRect
from scripts.modules.textures import *

_COLOR, _NUM_RECTS, _SIZE, _POS, _OFFSET, _HIDE = (1,1,1,1), 3, (100,100), (0,0), 0, False


class DigitCounter(ArrayRect):
	def __init__(self, game, window, num_rects=_NUM_RECTS, 
					color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
						size_lambda=None, positioning_lambda=None, hide=_HIDE):
						
		super().__init__(game=game, window=window, num_rects=num_rects, 
							color=color, size=size, pos=pos, offset=offset, 
								size_lambda=size_lambda, positioning_lambda=positioning_lambda, hide=hide)
		
		a = int(0)

		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry.rect.texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))

	#<----Base Functions: re_init, update			
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, 
					size_lambda=None, positioning_lambda=None, hide=_HIDE):
					
		super().re_init(color=color, size=size, pos=pos, offset=offset, 
							size_lambda=size_lambda, positioning_lambda=positioning_lambda, hide=hide)
		
		a = int(0)

		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry.rect.texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))
		
	def update(self,dt):
		pass
		
	#<----Rectangle Functions: re_size, show, hide, remove	
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()

	def flip(self, value=0):
		a = int(value)

		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry.rect.texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))
