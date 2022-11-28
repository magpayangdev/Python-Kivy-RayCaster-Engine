
_game_ref=None
def re_init(game_ref):
	global _game_ref
	_game_ref = game_ref
	
def load_loading_screen():
	from scripts.cards.loading_screen import LoadingScreen
	_game_ref.l_screen = LoadingScreen(_game_ref, **_game_ref.ls_kwargs)
	return 'Loading {}...'.format('Loading Screen')

def load_sky():
	from scripts.user_objects import UserSky
	_game_ref.sky = UserSky(_game_ref, hide=True, **_game_ref.kw_args)
	return 'Loading {}...'.format('Sky')
	
def load_floor():
	from scripts.user_objects import UserFloor
	_game_ref.floor = UserFloor(_game_ref, hide=True)
	return 'Loading {}...'.format('Floor')
	
def load_audio():
	from scripts.user_objects import UserAudio
	UserAudio(_game_ref, **_game_ref.kw_args)
	return 'Loading {}...'.format('Audio')

def load_minimap():
	from scripts.user_objects import UserMap 
	_game_ref.minimap=UserMap(_game_ref,hide=True)	
	return 'Loading {}...'.format('Map')

def load_player():
	from scripts.user_objects import UserPlayer
	_game_ref.player = UserPlayer(_game_ref,**_game_ref.kw_args)
	return 'Loading {}...'.format('Player')

def load_graph():
	from scripts.user_objects import UserGraphManager 
	_game_ref.graph_mngr = UserGraphManager(_game_ref, **_game_ref.kw_args)
	return 'Loading {}...'.format('Graph')

def load_event_manager():
	from scripts.game.event_manager import EventManager
	EventManager(_game_ref)
	return 'Loading {}...'.format('Event Manager')
	
def load_font_manager():
	from scripts.modules import fonts
	return 'Loading {}...'.format('Font Manager')
	
def load_world():
	from scripts.scene_objects.world import World  
	_game_ref.world = World(_game_ref)	
	return 'Loading {}...'.format('World')
	
def load_sprite_space():
	from scripts.spaces.scene_sprites_container import SceneSpritesContainer
	_game_ref.sprite_space = SceneSpritesContainer(_game_ref, hide=True)
	return 'Loading {}...'.format('Sprite Space')
	
def load_primary_loop():
	from scripts.modules.loops import primary_loop as pl
	_game_ref.primary_loop = pl
	_game_ref.primary_loop.re_init(_game_ref)
	return 'loading {}...'.format('Primary Loop') 
	
def load_hud():
	from scripts.bases.timed_updates.timed_quadrant import TimedQuadrant
	_game_ref.hud = TimedQuadrant(_game_ref)
	return 'Loading {}...'.format('Hud')

def load_text_card_manager():
	from scripts.game.card_manager import CardManager
	_game_ref.tc_mngr = CardManager(_game_ref)
	return 'Loading {}...'.format('Text Card Manager')
	
def load_pre_primary_loop():
	from scripts.modules.loops import pre_primary_loop as ppl
	_game_ref.pre_primary_loop = ppl
	_game_ref.pre_primary_loop.re_init(_game_ref)
	return 'Loading {}...'.format('Pre Primary Loop') 
	
def load_secondary_loop():
	from scripts.modules.loops import secondary_loop as scl
	_game_ref.secondary_loop = scl
	_game_ref.secondary_loop.re_init(_game_ref)
	return 'Loading {}...'.format('Secondary Loop') 
	 
							
_load_iterator = (func for func in (
									load_graph, 
									load_font_manager,
									load_pre_primary_loop,
									load_audio,
									load_text_card_manager,
									
									load_primary_loop,
									load_sky,
									load_floor,
									load_world,
									load_sprite_space,
									load_player,
									load_hud,
									
									load_minimap,
									
									load_secondary_loop
									))


def update(dt=0, game_ref=None):	
	if not _game_ref:
		re_init(game_ref)
	
	return next(_load_iterator)(), False
