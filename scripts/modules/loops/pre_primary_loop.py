from kivy.clock import Clock

_game=None
def re_init(_game_ref):
	global _game
	_game = _game_ref
	
	
_accum_time=0
def update(dt):
	global _accum_time
	
	if _game.paused: 
		return
			
	_accum_time += dt
	
	if _game.menu:
		_game.menu.update(dt)
		
	if _game.tc_mngr:
		_game.tc_mngr.update(dt)
			
	if _accum_time > 0.1:
		_accum_time = 0.0
















			