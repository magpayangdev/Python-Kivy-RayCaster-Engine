
from scripts.bases.base_sprites.player_sprite import PlayerSprite


class DefaultPlayerSprite(PlayerSprite):
	def __init__(self, game, sprite_id='shot_gun', flip_time=0.1, animate_on_spawn=True, hide=True):	
		super().__init__(game=game, sprite_id=sprite_id, flip_time=flip_time, animate_on_spawn=animate_on_spawn, hide=hide)
