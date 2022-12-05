
_game_ref=None
_load_iteratory=None

def re_init(game_ref):
	global _game_ref, _load_iterator
	_game_ref = game_ref

	_load_iterator = (func for func in (re_init_graph, re_init_pre_primary_loop, re_init_audio, re_init_text_card_manager, re_init_primary_loop, re_init_sky, re_init_floor, re_init_world, re_init_sprite_space, re_init_player, re_init_hud, re_init_minimap, re_init_secondary_loop))

def update(dt=0, game_ref=None):
	if not _game_ref:
		re_init(game_ref)
	
	return next(_load_iterator)(), False

def re_init_loading_screen():
	from scripts.cards.loading_screen import LoadingScreen
	_game_ref.l_screen = LoadingScreen(_game_ref)
	return 'Re-loading {}...'.format('Loading Screen')

def re_init_audio():
	_game_ref.audio.re_init(**_game_ref.kw_args)
	return 'Re-loading {}...'.format('Audio')

def re_init_event_manager():
	_game_ref.event.re_init()
	return 'Re-loading {}...'.format('Event Manager')

def re_init_floor():
	_game_ref.floor.re_init(**_game_ref.kw_args)
	return 'Re-loading {}...'.format('Floor')

def re_init_graph():
	_game_ref.graph_mngr.re_init(**_game_ref.kw_args)
	return 'Re-loading {}...'.format('Graph')

def re_init_hud():
	_game_ref.hud.re_init(hide=True)
	return 'Re-loading {}...'.format('Hud')

def re_init_minimap():
	_game_ref.minimap.re_init(hide=True)
	return 'Re-loading {}...'.format('Map')

def re_init_player():
	_game_ref.player.re_init(**_game_ref.kw_args)
	return 'Re-loading {}...'.format('Player')

def re_init_pre_primary_loop():
	_game_ref.pre_primary_loop.re_init(_game_ref)
	return 'Re-loading {}...'.format('Pre Primary Loop')

def re_init_primary_loop():
	_game_ref.primary_loop.re_init(_game_ref)
	return 'Re-loading {}...'.format('Primary Loop')

def re_init_text_card_manager():
	_game_ref.tc_mngr.re_init()
	return 'Re-loading {}...'.format('Text Card Manager')

def re_init_secondary_loop():
	_game_ref.secondary_loop.re_init(_game_ref)
	return 'Re-loading {}...'.format('Secondary Loop') 

def re_init_sky():
	_game_ref.sky.re_init(hide=True, **_game_ref.kw_args)
	return 'Re-loading {}...'.format('Sky')

def re_init_sprite_space():
	_game_ref.sprite_space.re_init(hide=True)
	return 'Re-loading {}...'.format('Sprite Space')

def re_init_world():
	_game_ref.world.re_init(hide=True)
	return 'Re-loading {}...'.format('World')