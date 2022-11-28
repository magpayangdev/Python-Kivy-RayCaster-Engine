

_game=None
	
def re_init_settings():
	import settings as settings
	
	settings.re_init(_game)
	
	return "Re-initializing Settings..."
	
def re_init_engine():
	import scripts.modules.engine.engine as engine
	
	engine.re_init(_game)
	
	return "Re-initializing Engine"
	
def re_init_ray_caster():
	import scripts.modules.engine.ray_caster as ray_caster
	
	ray_caster.re_init(_game)
	
	return "Re-initializing RayCaster"
	
def re_init_grid_settings():
	pass
	
def re_init_path_finding():
	pass
	
func_iter = (func for func in (re_init_settings,re_init_engine,re_init_ray_caster,))

def execute():
	return next(func_iter)()

def update(dt=0, game_ref=None):
	global _game
	
	if not _game:
		_game = game_ref
		
	return execute(), False	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	