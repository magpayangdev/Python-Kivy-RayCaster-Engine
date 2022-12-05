
from scripts.bases.base_player import BasePlayer

_PX, _PY, _A, _R, _H, _REGEN = 1.5, 1.5, 0, 0.1, 789, 1 

class DefaultPlayer(BasePlayer):
	def __init__(self, game, player_pos_x=_PX, player_pos_y=_PY, player_angle=_A,
					player_radius=_R, player_health=_H, player_regen=_REGEN, **kwargs):
		super().__init__(game=game, pos_x=float(player_pos_y), pos_y=float(player_pos_y), 
							angle=float(player_angle), radius=float(player_radius), health=float(player_health), 
								regen=float(player_regen))
		
	def re_init(self, player_pos_x=_PX, player_pos_y=_PY, player_angle=_A, player_radius=_R, 
						player_health=_H, player_regen=_REGEN, **kwargs):
		super().re_init(pos_x=float(player_pos_x), pos_y=float(player_pos_y), angle=float(player_angle), 
							radius=float(player_radius), health=float(player_health), regen=float(player_regen))
		