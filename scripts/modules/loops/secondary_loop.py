#from scripts.game_loops import loop_tools as loop

_accum_time=0
_game=None
def re_init(game_ref):
	global _game, _accum_time
	_game = game_ref
	_accum_time = 0

def update(dt):
	global _accum_time
	
	_game.hud.text = 'ACCUM_TIME {0:0.5F} '.format(_accum_time)
	
	if _game.paused: 
		return
	
	_accum_time += dt

	a,b,c,d = 3,5,15,20	
	if a < _accum_time < a + 1:
		_accum_time = a + 1
		_game.event.level_clean_up()

	if b < _accum_time < b + 1:
		_accum_time = b + 1
		_game.event.show_score()
		
	if b + 1 < _accum_time < c:
		_game.tc_mngr.update(dt)

	if d < _accum_time < d + 1:
		_accum_time = 999
		_game.event.next_level()

