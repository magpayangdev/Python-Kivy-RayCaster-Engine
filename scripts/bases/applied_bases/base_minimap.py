from scripts.modules.graph import coord_converter as cc
from settings import *
from scripts.bases.multi_rect_bases.grid import Grid
from scripts.bases.window_objects.textured_rect import TexturedRect


class BaseMinimap(Grid):
	def __init__(self, game, hide=True):
		super().__init__(game=game, window=None, num_rects=TOTAL_NUMBER_OF_MAP_BLOCKS, size=map_size(), hide=False)
		
		self.player_icon = TexturedRect(game=self.game, window=self.game.window, image_name='rockman.png', image_category='map', color=(1,1,1,1), size=(c_block_size(),c_block_size()), pos=(0,0), hide=False)
		
		if hide:
			self.hide()
		
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
			
	def update(self,dt):
		super().update(dt)
		if self.in_cnvs:					
			ppx,ppy=self.game.player.pos_x, self.game.player.pos_y
			self.player_icon.rect.pos = cc.world_to_screen_player(ppx, ppy)
			
			for idx, entry in enumerate(self.game.sprite_space.all_sprites):				
				if entry.d_f_player < 7:
					if not entry.minimap_icon.in_cnvs:
						entry.minimap_icon.show()		
					entry.minimap_icon.pos = cc.world_to_screen_sprite(entry.pos_x, entry.pos_y, ppx, ppy)	
				else:
					entry.minimap_icon.hide()
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
	def show(self):
		super().show()
		
		self.player_icon.show()
		
		for idx, entry in enumerate(self.game.sprite_space.all_sprites):
			if entry.d_f_player<5:
				entry.minimap_icon.show()
			
	def hide(self):
		super().hide()

		self.player_icon.hide()
		
		for idx, entry in enumerate(self.game.sprite_space.all_sprites):
			entry.minimap_icon.hide()
			
	def remove(self):
		super().remove()
		
	def flip(self):
		super().flip()
		
	def set_block_transforms(self, rect, idx):
		super().set_block_transforms(rect=rect, idx=idx)
		
	def set_block_colour(self, rect, idx, use_texture=False):
		super().set_block_colour(rect, idx, use_texture=use_texture)

