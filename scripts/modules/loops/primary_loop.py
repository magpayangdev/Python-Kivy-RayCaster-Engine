
from scripts.modules.engine import engine as engine

_game=None

def invalid_func():
	9/0

def re_init(game_ref):
	global _game
	_game = game_ref

_accum_time=0
def update(dt):
	global _accum_time
	
	if _game.paused: 
		return
					
	_accum_time += dt
		
	_game.hud.update(dt)
	_game.player.update(dt)
	_game.graph_mngr.update(dt)
	_game.sky.update(dt)
	_game.sprite_space.update_sprites(dt)
	_game.minimap.update(dt)

	engine.pre_run_prep(dt)
	while True:
		try:
			engine.run()
		except StopIteration:
			break

	if _accum_time > 0.1: #DEBUG_TEXT_REFRESH_RATE:
		_accum_time = 0.0
		_game.hud.text = 'FPS {0:0.2f} '.format(1/dt)
		
		
		