#from scripts.game_loops import loop_tools as loop

_accum_time=0
_game=None
def re_init(game_ref):
	global _game, _accum_time
	_game = game_ref
	_accum_time = 0
	
def set_accum_time(value):
	global _accum_time
	
	_accum_time = value
	
_debug_int=0
import random 
def update(dt):
	global _accum_time, _debug_int

	if _game.paused: 
		return
		
	_accum_time += dt
	_game.hud.text = 'Accumulted Time {0:0.5f}'.format(_accum_time)
		
	a,b,c,d = 3,5,15,22
	if a < _accum_time < a + 1:
		_accum_time = a + 1
		_game.event.level_clean_up()

	elif b < _accum_time < b + 1:
		_accum_time = b + 1
		_game.event.show_score()
				
	elif b + 1 < _accum_time < 15:
		_game.tc_mngr.update(dt)

	elif d < _accum_time < d + 999:
		_accum_time = 999
		_game.event.next_level()
	
	else:
		pass
		
		

