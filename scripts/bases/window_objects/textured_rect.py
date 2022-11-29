
from scripts.bases.window_objects.rect_base import RectBase
from scripts.modules.textures import *

class TexturedRect(RectBase):
	def __init__(self, game, window, image_name, image_category, color, size, pos, hide=False):
		super().__init__(game=game, window=window, color=color, size=size, pos=pos, hide=hide)
		
		self.image_name = image_name
		self.image_category = image_category
		
		self.texture=None	
		if self.image_category == 'sky':
			self.texture=get_sky_texture(self.image_name)
			
		elif self.image_category == 'controller':
			self.texture=get_controller_texture(self.image_name)
			
		elif self.image_category == 'wall':
			self.texture=get_wall_texture(self.image_name)
			
		elif self.image_category == 'map':
			self.texture=get_map_texture(self.image_name)
			
		elif self.image_category == 'digit':
			self.texture=get_digit_texture(self.image_name)
			
		elif self.image_category == 'menu':
			self.texture=get_menu_texture(self.image_name)
			
		elif self.image_category == 'game':
			self.texture=get_game_texture(self.image_name)
			
		elif self.image_category == 'floor':
			self.texture=flr_texture()
			
		else:
			raise Exception('Invalid	 image_category')
			
		self.rect.texture=self.texture

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

























