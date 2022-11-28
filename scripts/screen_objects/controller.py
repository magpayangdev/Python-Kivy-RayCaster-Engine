
from scripts.bases.multi_rect_bases.controller import Controller

class LeftController(Controller):
	def __init__(self, game):
		super().__init__(game, orientation='left')
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
	def update(self,dt):
		super().update(dt)
			
	def start_counting(self):
		super().start_counting()
		
	def stop_counting(self):
		super().stop_counting()
		
	def flip(self):
		super().flip()
		
		if self.accum_time < 1:			
			self.game.minimap.flip()
			
			self.stop_counting()
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()	
		
	def move_stick(self, Px, Py):
		super().move_stick(Px, Py)
		
	def reset_stick(self):
		super().reset_stick()
		
class RightController(Controller):
	def __init__(self, game):
		super().__init__(game, orientation='right')
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
	def update(self,dt):
		super().update(dt)
			
	def start_counting(self):
		super().start_counting()
		
	def stop_counting(self):
		super().stop_counting()
		
	def flip(self):
		super().flip()
		
		if self.accum_time < 1:
			self.game.hud.player_sprite.attack()
			self.stop_counting()
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()	
		
	def move_stick(self, Px, Py):
		super().move_stick(Px, Py)
		
	def reset_stick(self):
		super().reset_stick()


