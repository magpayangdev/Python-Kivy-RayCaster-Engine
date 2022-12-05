
from scripts.bases.window_objects.rect_base import RectBase
from scripts.modules.textures import *


_IMG_NAME, _IMG_CATEGORY = 'python.png', 'game'
_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False


class TexturedRect(RectBase):
	def __init__(self, game, window, image_name=_IMG_NAME, image_category=_IMG_CATEGORY, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().__init__(game=game, window=window, size=size, pos=pos, color=color, hide=hide)
		
		self.image_name = image_name
		self.image_category = image_category
		self.rect.texture = get_texture(self.image_name, self.image_category)

	#<----Base Functions: re_init, update			
	def re_init(self, image_name=_IMG_NAME, image_category=_IMG_CATEGORY, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().re_init(size=size, pos=pos, color=color, hide=hide)
		
		self.image_name = image_name
		self.image_category = image_category
		self.rect.texture = get_texture(self.image_name, self.image_category)
		
	def update(self, dt):
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

























