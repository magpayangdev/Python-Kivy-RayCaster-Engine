
from scripts.bases.multi_rect_bases.base_controller import BaseController


class LeftController(BaseController):
	def __init__(self, game):
		super().__init__(game, orientation='left')
		
	#<----Base Functions: re_init, update			
	def re_init(self, orientation='left'):
		super().re_init(orientation=orientation)
		
	def flip_func(self):		
		super().flip_func()
		
		self.game.minimap.flip()
		
class RightController(BaseController):
	def __init__(self, game):
		super().__init__(game, orientation='right')
		
	#<----Base Functions: re_init, update			
	def re_init(self, orientation='right'):
		super().re_init(orientation=orientation)
		
	def flip_func(self):	
		super().flip_func()	
		
		self.game.hud.player_sprite.attack()
