
from scripts.bases.multi_rect_bases.digit_counter import DigitCounter
from settings import *

class HealthIndicator(DigitCounter):
	def __init__(self, game, hide=True):
		super().__init__(game, window=None, num_rects=3, size=(100,100), pos=(0,0), offset=1, hide=hide)
	
		self.pos = 1, self.window.size[1] - self.size[1] - 1
		offset = 1

		self.re_size()

	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()

	def flip(self, value=0):	
		super().flip(self.game.player.health)	
		
		
		