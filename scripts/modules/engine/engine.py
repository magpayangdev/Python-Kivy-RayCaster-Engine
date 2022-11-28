""" engine """

from settings import *
from scripts.modules.engine import ray_caster

_game=None
_i_a_d=None

def re_init(game_ref):
	global _game
	_game = game_ref

def pre_run_prep(dt):
	global _i_a_d
	
	_game.sprite_space.get_FOV_s()
		 	
	_i_a_d = ((idx, _game.player.angle + HALF_FOV - DELTA_ANGLE * idx, dt) for idx in range(NUMBER_OF_RAYS))
		
def run():
	idx, angle, dt = next(_i_a_d)
	dist, Px, Py, wall, hor = ray_caster.cast_ray(angle)
	_game.world.update(idx, dist, Px, Py, angle, wall, hor)
	_game.sprite_space.update(idx, dist, angle)
