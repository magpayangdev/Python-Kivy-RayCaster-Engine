
from scripts.bases.window_objects.rect_base import RectBase
from scripts.modules.textures import *

_IMG_SEQ_ID, _INIT_MODE = 'python.png', 'game'
_COLOR, _SIZE, _POS, _HIDE = (1,1,1,1), (100,100), (0,0), False


class SequenceTexturedRect(RectBase):
	def __init__(self, game, window, img_seq_id=_IMG_SEQ_ID, initial_mode=_INIT_MODE, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):	
		super().__init__(game=game, window=window, color=color, size=size, pos=pos, hide=hide)		
		
		self.img_seq_id = img_seq_id
		self.init_mode = initial_mode

		self.seq_texture = (image for image in get_image_sequence(self.img_seq_id, self.init_mode))
		self.rect.texture = next(self.seq_texture)

	#<----Base Functions: re_init, update			
	def re_init(self, img_seq_id=_IMG_SEQ_ID, initial_mode=_INIT_MODE, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().re_init(color=color, size=size, pos=pos, hide=hide)

		self.img_seq_id = img_seq_id
		self.init_mode = initial_mode

		self.seq_texture = (image for image in get_image_sequence(self.img_seq_id, self.init_mode))
		self.rect.texture = next(self.seq_texture)
		
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
