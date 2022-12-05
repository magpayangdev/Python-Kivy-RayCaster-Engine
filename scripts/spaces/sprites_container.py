
from scripts.spaces.layout_base import LayoutBase
from scripts.screen_objects.sprites import *

_HIDE=False

class SpritesContainer(LayoutBase):
	def __init__(self, game, hide=_HIDE, **kwargs):
		super().__init__(game=game, hide=hide, **kwargs)
		
		self.all_sprites=[]
		
	#<----Sprites Func Show, Remove Sprites
	def show_sprite(self, sprite):
		sprite.show()
			
	def hide_sprite(self, sprite):
		sprite.hide()

	def remove_sprite(self, sprite):
		sprite.remove()
		self.all_sprites.remove(sprite)

	def remove_all_sprites(self):
		[self.remove_sprite(sprt) for sprt in list(self.all_sprites)]
		
	def remaining_sprites(self):
		n = 0
		for i in self.all_sprites:
			if isinstance(i,DefaultNPCSprite)and(i.current_action!='die'and i.current_action!='for delete'):
				n += 1		
		return n
		
	#<----Base Functions: re_init, update		
	def re_init(self, hide=_HIDE):
		super().re_init(hide=hide)
		
		[entry.re_init(hide=hide) for entry in self.all_sprites]
				
	def update(self, dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
				
	def hide(self):
		super().hide()
		
	def remove(self):
		super().remove()
