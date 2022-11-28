
from scripts.bases.window_objects.rect_base import RectBase

class HitRect(RectBase):
	def __init__(self, game, hide=True):
		super().__init__(game=game, window=None, color=(1,0,0,0), size=game.window.size, pos=game.window.pos, hide=hide)
			
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.size = self.window.size
		self.pos = self.window.pos
		
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

		































