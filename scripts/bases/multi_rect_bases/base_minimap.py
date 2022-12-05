
from settings import *
from scripts.bases.multi_rect_bases.grid import Grid
from scripts.modules.graph import coord_converter as cc
from scripts.bases.window_objects.textured_rect import TexturedRect

_NUMBER_RECTS, _SIZE, _HIDE = TOTAL_NUMBER_OF_MAP_BLOCKS, map_size(), False
_IMAGE_NAME, _IMAGE_CATEGORY, _COLOR, _SIZE, _POS = 'rockman.png', 'map', (1,1,1,1), (c_block_size(), c_block_size()), (0,0)
_PI_KWARGS = {'image_name':_IMAGE_NAME, 'image_category':_IMAGE_CATEGORY, 'color':_COLOR, 'size':_SIZE, 'pos':_POS}


class BaseMinimap(Grid):
	""" Has a player icon """
	def __init__(self, game, hide=_HIDE, player_icon_kwargs=_PI_KWARGS):
	
		super().__init__(game=game, window=None, num_rects=_NUMBER_RECTS, hide=hide)
		
		self.max_sprite_distance = 7
		
		self.player_icon = TexturedRect(game=self.game, window=self.game.window, hide=hide, **player_icon_kwargs)
		
	#<----Base Functions: re_init, update			
	def re_init(self, hide=_HIDE, player_icon_kwargs=_PI_KWARGS):
		super().re_init(hide=hide)
		
		self.player_icon.re_init(hide=hide, **player_icon_kwargs)
		
		for idx, entry in enumerate(self.game.sprite_space.all_sprites):	
			entry.minimap_icon.hide()		
			
	def update(self,dt):
		super().update(dt)
		if self.in_cnvs:					
			ppx,ppy=self.game.player.pos_x, self.game.player.pos_y
			self.player_icon.rect.pos = cc.world_to_screen_player(ppx, ppy)
			
			for idx, entry in enumerate(self.game.sprite_space.all_sprites):		
				if entry.d_f_player < self.max_sprite_distance:
					if not entry.minimap_icon.in_cnvs:
						entry.minimap_icon.show()		

					entry.minimap_icon.pos = cc.world_to_screen_sprite(entry.pos_x, entry.pos_y, ppx, ppy)

				else:
					entry.minimap_icon.hide()
		
	#<----Rectangle Functions: re_size, show, hide, remove		
	def show(self):			
		super().show()
		
		self.player_icon.show()
		ppx, ppy = self.game.player.pos_x, self.game.player.pos_y
		self.player_icon.rect.pos = cc.world_to_screen_player(ppx, ppy)
		
		for idx, entry in enumerate(self.game.sprite_space.all_sprites):
			if entry.d_f_player < self.max_sprite_distance:
				entry.minimap_icon.show()
				entry.minimap_icon.pos = cc.world_to_screen_sprite(entry.pos_x, entry.pos_y, ppx, ppy)
			
	def hide(self):
		super().hide()

		self.player_icon.hide()
		
		for idx, entry in enumerate(self.game.sprite_space.all_sprites):
			entry.minimap_icon.hide()
			
	def remove(self):
		super().remove()
		
		self.player_icon.remove()
		
		for idx, entry in enumerate(self.game.sprites_space.all_sprites):
			entry.minimap_icon.hide()

	#<----Minimap Funcst		
	def flip(self):
		if self.in_cnvs:
			self.hide()
		else:
			self.show()
					
	def set_block_transforms(self, rect, idx):
		super().set_block_transforms(rect=rect, idx=idx)
		
	def set_block_colour(self, rect, idx, use_texture=False):
		super().set_block_colour(rect, idx, use_texture=use_texture)

