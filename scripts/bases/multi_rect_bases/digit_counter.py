
from scripts.bases.multi_rect_bases.array_rect import ArrayRect
from scripts.modules.textures import *


class DigitCounter(ArrayRect):
	def __init__(self, game, window, num_rects=3, size=(100,100), pos=(0,0), offset=1, hide=False):
		super().__init__(game, window, num_rects=num_rects, size=size, pos=pos, offset=offset, hide=hide)
		
		a = int(0)

		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry.rect.texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))

	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.flip(value=0)
		
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
		a = int(value)

		for idx, entry in enumerate(self.rects):
			num = a // (100 // (10 ** idx))
			entry.rect.texture = get_digit_texture(str(num))
			a = a % (100 // (10 ** idx))
