
from scripts.bases.base_sprites.static_sprite import StaticSprite
import math

_SPRITE_ID, _MINIMAP_ICON, _WORLD_POS = 'candle_bra', 'cherry.png', (0,0)
_RADIUS, _SCALE, _HEALTH, _INFLUENCE_RANGE, _INFLUENCE_AMOUNT, _HIDE = 0.1, 0.5, 10, 1, 1, False


class BaseGoalSprite(StaticSprite):
	def __init__(self, game, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, world_pos=_WORLD_POS, 
					radius=_RADIUS, scale=_SCALE, health=_HEALTH, influence_range=_INFLUENCE_RANGE, 
						influence_amount=_INFLUENCE_AMOUNT, hide=_HIDE):
		super().__init__(game=game, sprite_id=sprite_id, minimap_icon=minimap_icon, world_pos=world_pos, 
					radius=radius, scale=scale, health=health, influence_range=influence_range, 
						influence_amount=influence_amount, hide=hide)
		self.start()
						
	def re_init(self, sprite_id=_SPRITE_ID, minimap_icon=_MINIMAP_ICON, world_pos=_WORLD_POS, radius=_RADIUS,
					scale=_SCALE, health=_HEALTH, influence_range=_INFLUENCE_RANGE, influence_amount=_INFLUENCE_AMOUNT,
						hide=_HIDE):		
		super().re_init(sprite_id=sprite_id, minimap_icon=minimap_icon, world_pos=world_pos, radius=radius,
					scale=scale, health=health, influence_range=influence_range, influence_amount=influence_amount,
						hide=hide)
		self.start()

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		super().fbf_update(dt)

		if self.d_f_player < self.influence_range:
			self.game.event.reached_goal()
			#self.game.hud.text = 'influence range {0:0.2f}  reached_goal '.format(self.influence_range)
		else:
			pass
			#self.game.hud.text = 'influence range {0:0.2f}  Not Yet '.format(self.influence_range)
