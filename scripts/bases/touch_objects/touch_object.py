
from scripts.bases.base import Base


class TouchObject(Base):
	def __init__(self, game):
		super().__init__(game=game)
		
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)

	#<----TouchFunctions: on_touch_down, on_touch_move, on_touch_up
	def on_touch_down(self, touch):
		pass
	
	def on_touch_move(self, touch):
		pass
		
	def on_touch_up(self, touch):
		pass