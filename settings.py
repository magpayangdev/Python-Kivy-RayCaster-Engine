"""
settings
"""
import math


""" References """
game=None

""" Screen """
_screen_width, _screen_height = 0, 0
_half_screen_width = 0
_half_screen_height = 0
_screen_element_width = 0

""" Debug """
_debug_mode = False
_render_map = True
_render_rays = _render_map and False
DEBUG_TEXT_REFRESH_RATE = 0.5
MAX_NUMBER = 9999

DEBUG_MAP_SPRITES = False		

""" Ray Casting """
FOV	= math.pi / 3
HALF_FOV = FOV / 2
NUMBER_OF_RAYS = 301
DELTA_ANGLE = FOV / (NUMBER_OF_RAYS - 1)
TAU = math.tan(FOV / 2)
_tau = 0.0 # screen distance from player
RAY_STEPS = 1
RAYCAST_COLLISION_PEAK_DISTANCE = 0.1
_rectangle_texture_width = 0.0

""" Angles """
ZERO_DEGREES = 0.0
P_90_DEGREES = math.pi / 2
P_180_DEGREES = math.pi
P_270_DEGREES = 3 * math.pi / 2
P_360_DEGREES = 2 * math.pi

M_90_DEGREES = -P_90_DEGREES
M_180_DEGREES = -P_180_DEGREES
M_270_DEGREES = -P_270_DEGREES
M_360_DEGREES = -P_360_DEGREES

""" Map """
MAP_SIZE = 1 #[1-takes entire screen, 2-half the screen height, and so on..]
BLOCK_OFFSET = 5
NUMBER_OF_BLOCKS_ACROSS = 15
NUMBER_OF_BLOCKS_DOWN = NUMBER_OF_BLOCKS_ACROSS
MAX_MAP_INDEX_ACROSS = NUMBER_OF_BLOCKS_ACROSS - 1
MAX_MAP_INDEX_DOWN = NUMBER_OF_BLOCKS_DOWN   - 1
TOTAL_NUMBER_OF_MAP_BLOCKS = NUMBER_OF_BLOCKS_ACROSS * NUMBER_OF_BLOCKS_DOWN
MAX_LINE_OF_SIGHT_DISTANCE = math.sqrt((NUMBER_OF_BLOCKS_ACROSS ** 2) + (NUMBER_OF_BLOCKS_DOWN ** 2))

_map_size = 0, 0
_net_block_size = 0.0 
_gross_block_size = 0.0
_character_block_size = 0
_half_c_block_size = 0
_map_center = 0.0, 0.0
_map_center_offset_x = 0.0
_map_center_offset_y = 0.0

MAP_LOCATION = 'top_mid' #'top_left' #'center_mid' #'bot_mid'

""" Player """
PLAYER_FORWARD_VECTOR_LEN = 1
PLAYER_RADIUS = 0.1
GUN_ANIMATION_DURATION = 0.15
PLAYER_CAN_DIE = True
MAX_PLAYER_HEALTH = 100

NPC_RADIUS = 0.2
SPRITE_DEBUG = False

""" Colours """
RED = 1, 0, 0
DARK_RED = 0.5,0.1,0
BROWN = 0.5,0.2,0
YELLOW = 1, 1, 0
GREEN = 0, 1, 0
WHITE = 1, 1, 1
BLACK_a = 0,0,0,1
BLACK = 0, 0, 0
GREY = 0.5, 0.5, 0.5
GREY25 = 0.25, 0.25, 0.25
GREY75 = 0.75, 0.75, 0.75
GREY80 = 0.8, 0.8, 0.8
PINK = 1, 0, 1
TRANSPARENT_BLACK = 0,0,0,0.5
DIRT_COLOUR = 0.25, 0.2, 0.1

PLAYER_COLOUR = WHITE
RAY_COLOUR = WHITE
INTERSECTION_COLOUR = GREY
DEBUG_TEXT_COLOR = GREEN
MAP_WALL_COLOUR = BLACK
MAP_FLOOR_COLOUR = WHITE
MAP_INVALID_COLOUR = PINK
MAP_BACKGROUND_COLOUR = BLACK
CONTROLLER_BACKGROUND_COLOUR = 0,0,0,1
CONTROLLER_STICK_COLOUR = 1,1,1,1
WORLD_FLOOR_COLOUR = GREY
WORLD_SKY_COLOUR = GREY

DISTANCE_FACTOR = 5 * 0.00002

""" Controller """
_controller_center_left_x = 0 
_controller_center_left_y = 0
_controller_center_right_x = 0
_controller_center_right_y = 0

_controller_center_left = 0.0, 0.0
_controller_center_right = 0.0, 0.0
_controller_size = 0.0, 0.0
_controller_stick_size = 0.0, 0.0

""" PATHS """
EMPTY_PATH = ''

USER_CONFIG_PATH = 'user_config.csv'
#WORLD_OBJECTS_LIST = 'world_objects_list.csv'

AUDIO_PATHS = 'scripts/resources/audio','resources/sound/'

PATH_MAP_ICONS = "scripts/resources/textures/minimap/","resources/textures/map/"
PATH_CONTROLLER_ICONS="scripts/resources/textures/controller/","resources/textures/controller/"
MENU_TEXTURES = "scripts/resources/textures/menu/","resources/textures/menu/"
GAME_TEXTURES = "scripts/resources/textures/game/","resources/textures/game/"
DIGIT_TEXTURES = "scripts/resources/textures/digits/","resources/textures/digits/"
PATH_WALL_TEXTURES = "scripts/resources/textures/wall/","resources/textures/wall/"
PATH_SKY_TEXTURES = "scripts/resources/textures/sky","resources/textures/sky/"

# Default Path for Sprites
_PLAYER_SPRITE = 'scripts/resources/textures/shotgun/'

_NPC_HIT = 'scripts/resources/textures/npc_sprites/pain/0.png'
_NPC_IDLE = 'scripts/resources/textures/npc_sprites/idle/0.png'
_NPC_WALK = 'scripts/resources/textures/npc_sprites/walk/0.png'
_NPC_ATTACK = 'scripts/resources/textures/npc_sprites/attack/0.png'
_NPC_DEATH = 'scripts/resources/textures/npc_sprites/death/POSSM0.png'

_PATH_ANIM_SPRITE = 'scripts/resources/textures/animated_sprites/0.png'
_PATH_STATIC_SPRITE = 'scripts/resources/textures/static_sprites/static_sprite.png'

SPRITE_ID_TO_IMAGES_PATH = {
	'candle_bra': [_PATH_STATIC_SPRITE, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH],
	'flame': [_PATH_ANIM_SPRITE, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH],
	'soldier' : [_NPC_IDLE, _NPC_WALK, _NPC_HIT, _NPC_ATTACK, _NPC_DEATH],
	'shot_gun' : [_PLAYER_SPRITE, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH, EMPTY_PATH]
	}
# # is replaced with \n
SAMPLE_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.#"

FONT_1 = 'AdventureRequest'


""" Settings """
def distance_to_intensity(distance):
	# light intensity as a function of distance
	return 100000 / (100000 + 2 * distance ** 5)
	
def scr_width():
	# update screen width
	return _screen_width

def scr_height():
	# updated screen height
	return _screen_height

def half_scr_w():
	# updated half screen width
	return _half_screen_width
		
def half_scr_h():
	# updated half screen height
	return _half_screen_height	

def scr_rect_w():
	# width of each screen element
	return _screen_element_width
	
def screen_distance():
	# screen distance from player
	return _tau
	
def scr_distance():
	# screen distance from player
	return _tau
	
def g_block_size():
	# map block size with the offset
	return _gross_block_size
	
def n_block_size():
	# map block size without the offset
	return _net_block_size
	
def c_block_size():
	# character rectangle block size on map
	return _character_block_size
	
def hc_block_size():
	return _half_c_block_size
		
def debug_mode():
	return _debug_mode
	
def render_map():
	# is map enabled?
	return _render_map
	
def render_rays():
	# is draw casted rays enabled?
	return _render_rays
	
def map_size():
	# map size
	return _map_size
	
def map_centre_o():
	# map center offset screen coordinates
	return _map_center_offset_x, _map_center_offset_y
	
def controller_center_left():
	return _controller_center_left
	
def controller_center_right():
	return _controller_center_right
	
def controller_size():
	return _controller_size
	
def controller_stick_size():
	return _controller_stick_size


def re_init(game_ref):
	global game
	game = game_ref

	""" Screen """	
	global _screen_width, _screen_height
	global _half_screen_width, _half_screen_height
	global _screen_element_width, _tau

	_screen_width, _screen_height = game.window.size
	_half_screen_width, _half_screen_height = _screen_width / 2, _screen_height / 2
	_screen_element_width = _screen_width / NUMBER_OF_RAYS
	_tau = _half_screen_width / TAU
	screen_column_divisions, screen_row_divisions = 4, 3
	
	""" Controller """
	global _controller_center_left_x,   _controller_center_left_y  ,_controller_center_left
	global _controller_center_right_x,  _controller_center_right_y ,_controller_center_right
	global _controller_size, _controller_stick_size
	
	_controller_center_left_x = _screen_width  / screen_column_divisions / 2
	_controller_center_left_y = _screen_height / screen_row_divisions    / 2
	_controller_center_left = _controller_center_left_x, _controller_center_left_y

	_controller_center_right_x = _screen_width - _controller_center_left_x
	_controller_center_right_y = _controller_center_left_y
	_controller_center_right = _controller_center_right_x, _controller_center_right_y
	
	_controller_size = _screen_width / 5, _screen_width / 5
	_controller_stick_size = tuple(i / 5 for i in _controller_size)

	""" Map """	
	global _map_size
	
	_map_size = 0
	if _screen_width > _screen_height:
		_map_size = _screen_height // MAP_SIZE, _screen_height // MAP_SIZE
	else:
		_map_size = _screen_width // MAP_SIZE, _screen_width // MAP_SIZE
	
	""" Block Sizes """	
	global _gross_block_size, _net_block_size
	global _character_block_size, _half_c_block_size
	
	_gross_block_size = (0,0)
	_net_block_size = (0,0)
	_character_block_size = 0
	_half_c_block_size = 0
	_gross_block_size = tuple(i / NUMBER_OF_BLOCKS_ACROSS for i in _map_size)
	_net_block_size = tuple(i - BLOCK_OFFSET for i in _gross_block_size)
	_character_block_size = _gross_block_size[0]
	_half_c_block_size = _character_block_size / 2

	""" Map Center """
	global _map_center, _map_center_offset_x, _map_center_offset_y
	
	_map_center = 0, 0
	_map_center_offset_x, _map_center_offset_y = 0, 0
	if MAP_LOCATION.lower() == 'top_left':
		_map_center = 0, 0
		_map_center_offset_x = 1
		_map_center_offset_y = 1 + _screen_height - (_gross_block_size[0] * NUMBER_OF_BLOCKS_DOWN)
		
	elif MAP_LOCATION.lower() == 'top_mid':
		_map_center = _screen_width / 2, _screen_height
		_map_center_offset_x = _map_center[0] - (_gross_block_size[0] * NUMBER_OF_BLOCKS_ACROSS / 2)
		_map_center_offset_y = _map_center[1] - (_gross_block_size[0] * NUMBER_OF_BLOCKS_DOWN) 
		
	elif MAP_LOCATION.lower() == 'top_right':
		pass
		
	elif MAP_LOCATION.lower() == 'center_left':
		pass
		
	elif MAP_LOCATION.lower() == 'center_mid':
		_map_center = _screen_width / 2 , _screen_height / 2
		_map_center_offset_x = _map_center[0] - (_gross_block_size[0] * NUMBER_OF_BLOCKS_ACROSS) / 2
		_map_center_offset_y = _map_center[1] - (_gross_block_size[0] * NUMBER_OF_BLOCKS_DOWN) / 2
		
	elif MAP_LOCATION.lower() == 'center_right':
		pass
		
	elif MAP_LOCATION.lower() == 'bot_left':
		_map_center = 0, 0			
		_map_center_offset_x = 0
		_map_center_offset_y = 0
		
	elif MAP_LOCATION.lower() == 'bot_mid':
		_map_center = _screen_width / 2 , _controller_center_left_x	
		_map_center_offset_x = _map_center[0] - (_gross_block_size[0] * NUMBER_OF_BLOCKS_ACROSS) / 2
		_map_center_offset_y = 0
		
	elif MAP_LOCATION.lower() == 'bot_right':
		pass
		
	else:
		raise Exception('Invalid map location: {}'.format(MAP_LOCATION))

	""" Textures """
	global _rectangle_texture_width
	
	_rectangle_texture_width = _screen_width / (NUMBER_OF_RAYS - 1)	





