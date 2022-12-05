
from scripts.bases.timed_updates.timed_texture import TimedTexture
from settings import *

_IMAGE_NAME, _IMAGE_CATEGORY, _START_ITER, _HIDE = 'white', 'floor', False, False

class BaseFloor(TimedTexture):
	def __init__(self, game, floor_color=_IMAGE_NAME, hide=_HIDE):
		super().__init__(game, window=None, image_name=_IMAGE_NAME, image_category=_IMAGE_CATEGORY,  start_iter=_START_ITER, hide=hide)
	
		self.rect_size = self.game.window.width, self.game.window.height/2
		self.rect_pos = self.game.window.pos

	#<----Base Functions: re_init, update
	def re_init(self, floor_color=_IMAGE_NAME, hide=_HIDE):
		super().re_init(image_name=floor_color, image_category=_IMAGE_CATEGORY,  start_iter=_START_ITER, hide=hide)
		
		self.rect_size = self.game.window.width, self.game.window.height/2
		self.rect_pos = self.game.window.pos
		































