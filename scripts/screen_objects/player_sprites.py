
from scripts.bases.base_sprites.player_sprite import PlayerSprite


_D_SI, _D_FT, _D_AOS, _D_H = 'shot_gun', 0.1, True, True

class DefaultPlayerSprite(PlayerSprite):
	def __init__(self, game, sprite_id=_D_SI, flip_time=_D_FT, animate_on_spawn=_D_AOS, hide=_D_H):	
		super().__init__(game=game, sprite_id=sprite_id, flip_time=flip_time, animate_on_spawn=animate_on_spawn, hide=hide)

	def re_init(self, sprite_id=_D_SI, flip_time=_D_FT, animate_on_spawn=_D_AOS, hide=_D_H):
		super().re_init(sprite_id=sprite_id, flip_time=flip_time, animate_on_spawn=animate_on_spawn, hide=hide)
		
