
from scripts.bases.timed_updates.timed_image_rect import TimedImageRect
from settings import *

class Temp(TimedImageRect):
	def __init__(self, game, window, hide=False):
	
		super().__init__(game=game, window=window, image_name='py.png', image_category='game', image_color=(1,1,1,1), image_size=(100,100), image_pos=(0,0), color=(1,1,1,1), size=(100,100), pos=(0,0), hide=hide, flip_time=1, start_iter=False)
			
		self.image.rect.size = self.window.height, self.window.height
		self.image.rect.pos = self.window.pos
		
		self.rect.rect.size = self.window.size
		self.rect.rect.pos = self.window.pos
		
		self.rect.colour.rgba = (0,0.5,0.3,1)
