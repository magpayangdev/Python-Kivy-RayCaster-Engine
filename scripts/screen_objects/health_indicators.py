
from scripts.bases.multi_rect_bases.digit_counter import DigitCounter
from settings import *

_COLOR, _NUM_RECTS, _SIZE, _POS, _OFFSET, _HIDE = (1,1,1,1), 3, (100,100), (0,0), 0, True

class DefaultHealthIndicator(DigitCounter):
	def __init__(self, game, window=None, num_rects=_NUM_RECTS, color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, hide=_HIDE):
						
		positioning_lambda = lambda window, size, pos, offset: (0, window.height - size[1])
		
		super().__init__(game=game, window=window, num_rects=num_rects, color=color, size=size, pos=pos, offset=offset, size_lambda=None, positioning_lambda=positioning_lambda, hide=hide)
	
	#<----Base Functions: re_init, update			
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, offset=_OFFSET, hide=_HIDE):
						
		positioning_lambda = lambda window, size, pos, offset: (0, window.height - size[1])
			
		super().re_init(color=color, size=size, pos=pos, offset=offset, size_lambda=None, positioning_lambda=positioning_lambda, hide=hide)
			
	#<----Rectangle Functions: re_size, show, hide, remove
	def flip(self, value=0):	
		super().flip(self.game.player.health)
		
	def get_pos(self, window, size):
		if window:
			return 0, window.height - size[1]
		else:
			return 0, self.window.height - size[1]
		