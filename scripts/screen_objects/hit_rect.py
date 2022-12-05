
from scripts.bases.window_objects.rect_base import RectBase

_COLOR, _SIZE, _POS, _HIDE = (1,1,1,0), (100,100), (0,0), True


class HitRect(RectBase):
	def __init__(self, game, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE):
		super().__init__(game=game, window=None, color=color, size=size, pos=pos, hide=hide)
		
		self.size = self.window.size
		self.pos = self.window.pos
		self.color = color
		self.texture = None
			
	#<----Base Functions: re_init, update			
	def re_init(self, color=_COLOR, size=_SIZE, pos=_POS, hide=_HIDE):
		super().re_init(color=color, size=size, pos=pos, hide=hide)
		
		self.size = self.window.size
		self.pos = self.window.pos
		self.color = color
		self.texture = None
				
	def update(self,dt):
		super().update(dt)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
		self.texture=None
		
	def show(self):
		super().show()
					
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()		

		































