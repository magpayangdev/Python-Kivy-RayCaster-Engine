
from scripts.bases.base import Base

class WindowObject(Base):
	def __init__(self, game, window):
		super().__init__(game=game)

		self.in_cnvs = False
		self.window = None
		if window:
			self.window=window
		else:
			self.window=game.window
			
	#<----Getters
	@property
	def size(self):
		return self.window.size
		
	@property
	def pos(self):
		return self.window.pos
		
	@property
	def width(self):
		return self.window.width
		
	@property
	def height(self):
		return self.window.height
			
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)
			
	#<----Window Functions, re_size, show, hide, remove
	def re_size(self):
		pass
		
	def show(self):
		pass
				
	def hide(self):
		pass
		
	def remove(self):
		pass


































