
from scripts.bases.layout_bases.scene_sprites_layout import SceneSpritesLayout

class SpritesSpace(SceneSpritesLayout):
	def __init__(self, game, window, hide=False):
		super().__init__(game=game, window=window, hide=hide)
		
		#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)
		
	def reload_sprites(self):
		super().reload_sprites()
		
	#<---- Projection Funcs
	#def get_FOV_s(self):		
			
	#def next_c_t_s(self):		
			
	#def update_sprites(self, dt):
			
	#def update(self, idx, dist, r_a):		
			
	#def is_in_view(self, sprite):													
		
	#<---- Events	
	#def player_attack(self):

	#<----Sprites Func Show, Remove Sprites
	def show_sprite(self, sprite):
		super().show_sprite(sprite)
			
	def hide_sprite(self, sprite):
		super().hide_sprite(sprite)

	def remove_sprite(self, sprite):
		super().remove_sprite(sprite)
		
	def remove_all_sprites(self):
		super().remove_all_sprites()
		
	def remaining_sprites(self):
		super().remaining_sprites()
		
		#<----Layout Funcs
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
		
	def hide(self):
		super().hide()
		
	def remove(self):
		super().remove()