
from scripts.bases.window_objects.rect_base import RectBase
from scripts.modules.textures import *

class SequenceTexturedRect(RectBase):
	def __init__(self, game, window, img_seq_id, initial_mode, color=(1,1,1,1), size=(100,100), pos=(0,0), hide=False):	
		super().__init__(game=game, window=window, color=color, size=size, pos=pos, hide=hide)		
		self.init_mode = initial_mode
		self.img_seq_id = img_seq_id

		self.seq_texture = (image for image in get_image_sequence(self.img_seq_id, self.init_mode))
		self.rect.texture = next(self.seq_texture)

	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()

		self.reload_texture()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		pass
				
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()

	#<----Textures Functions: reload, change mode
	def reload_texture(self):

		self.seq_texture = (image for image in get_image_sequence(self.img_seq_id, self.init_mode))
		self.rect.texture = next(self.seq_texture)
		
	#def change_mode(self, new_mode):
		#self.init_mode = new_mode
		#self.reload_texture()
		
		#self.seq_texture = (image for image in get_image_sequence(self.img_seq_id, new_mode))
		#self.rect.texture = next(self.seq_texture)




























