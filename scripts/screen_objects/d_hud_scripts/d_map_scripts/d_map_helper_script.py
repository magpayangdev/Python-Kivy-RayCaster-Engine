#scripts/scene_objects/sprite.py
from scripts.scene_objects.sprite_scripts import sprite
from scripts.game.textures import *
from scripts.engine.helper_scripts import coordinates_converter as coord_cnvrtr

_map=None
_game=None
_graph=None
_window=None
_player=None

_ppx, _ppy = 0,0
_spx, _spy = 0,0
_scale_x, _scale_y = 0, 0
_centre_x, _centre_y = 0, 0

_debug_player_pos_x, _debug_player_pos_y = 0,0


def init(map_ref):
	global _map, _game, _graph, _player, _window
	
	_map = map_ref
	_game = map_ref.game
	_graph = _map.game.graph_mngr
	_window = _map.window
	_player = map_ref.game.player

def update_map_dimensions():
	global _scale_x, _scale_y
	_scale_x, _scale_y = g_block_size()
	_map.offset_x, _map.offset_y = map_centre_o()
	
	_map.map_scr_width = NUMBER_OF_BLOCKS_ACROSS * _scale_x
	_map.map_scr_height = NUMBER_OF_BLOCKS_DOWN * _scale_y
	
	_map.map_width = NUMBER_OF_BLOCKS_ACROSS
	_map.map_height = NUMBER_OF_BLOCKS_DOWN
	_map.half_map_width = NUMBER_OF_BLOCKS_ACROSS / 2
	_map.half_map_height = NUMBER_OF_BLOCKS_DOWN / 2
	
	coord_cnvrtr.init(_graph.world_width, _graph.world_height, _map.map_width, _map.map_height)

def update_character_position():	
	global _ppx, _ppy
	gx, gy = coord_cnvrtr.world_to_grid(_player.pos_x - 0.5, _player.pos_y + 0.5, _player.pos_x, _player.pos_y)
	_ppx, _ppy = coord_cnvrtr.grid_to_screen(gx, gy, _scale_x, _scale_y, _map.offset_x, _map.offset_y)
	_player.mmp_rect.pos = _ppx, _ppy
	
def update_sprites_position():
	global _centre_x, _centre_y
		
	_centre_x, _centre_y = int(_player.pos_x) + 0.5, int(_player.pos_y) + 0.5
	for idx, entry in enumerate(_game.sprite_space.all_sprites):
		if entry.d_f_player <= int(_map.half_map_width):
			update_sprite(entry)
		else:
			remove_sprite_from_mmp(entry)
			
def update_sprite(sprt):
	global _spx, _spy
	global _centre_x, _centre_y, _do_once
	
	if not sprt.in_mmp_cnvs:
		add_sprite_to_mmp(sprt)

	gx, gy = coord_cnvrtr.world_to_grid(sprt.pos_x - 0.5, sprt.pos_y + 0.5, _centre_x, _centre_y)
	_spx, _spy = coord_cnvrtr.grid_to_screen(gx, gy, _scale_x, _scale_y, _map.offset_x, _map.offset_y)
	
	sprt.mmp_rect.pos = _spx, _spy
			
	if DEBUG_MAP_SPRITES:
		draw_sprite_los(sprt)					
				
	if DEBUG_MAP_SPRITES:
		draw_sprite_path(sprt)

def draw_sprite_path(sprt):
	if isinstance(sprt, sprite.NPC) and sprt.path:
		for path in sprt.path:			
			idx = coord_cnvrtr.world_to_grid_index(path[0], path[1], _player.pos_x, _player.pos_y)
			_map.rects[idx][0].rgb = sprt.path_colour

def draw_sprite_los(sprt):
	gx, gy = coord_cnvrtr.world_to_grid(sprt.target_x, sprt.target_y, _centre_x, _centre_y)
	sx, sy = coord_cnvrtr.grid_to_screen(gx, gy, _scale_x, _scale_y, _map.offset_x, _map.offset_y)
		
	sprt.mmp_line.points = _spx + 0.5 * _scale_x, _spy + 0.5 * _scale_y, sx, sy
	
def draw_map_blocks(init=False):
	use_texture = False
	
	if init:
		for idx, entry in enumerate(_map.rects):
			set_block_transforms(entry[1], idx)
			set_block_colour(entry[0], entry[1], idx, False)

	else:
		for idx, entry in enumerate(_map.rects):
			set_block_colour(entry[0], entry[1], idx, False)			
				
def set_block_transforms(rect, idx):
	col = idx % _map.map_width
	row = idx // _map.map_height
	
	Px = (col + 0.1) * _scale_x + _map.offset_x
	Py = (_map.map_height - 0.9 - row) * _scale_y + _map.offset_y

	rect.size = n_block_size()
	rect.pos  = Px, Py 
		
def set_block_colour(colour, rect, idx, use_texture=False):
	gx, gy = coord_cnvrtr.grid_idx_to_grid(idx)
	wx, wy = coord_cnvrtr.grid_to_world(gx, gy, _player.pos_x + 0.5, _player.pos_y + 0.5)

	w_string = _graph.get_string(int(wx) + int(wy) * _graph.world_width)

	if use_texture:          
		if w_string in '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' : 
			rect.texture = get_map_texture('brick_wall.png')
			
		elif w_string == ".": 
			rect.texture = get_map_texture('brick_wall.png')
			
		else: 
			colour.rgb = MAP_INVALID_COLOUR
	else:
		if w_string in '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' : 
			colour.rgb = BROWN
			
		elif w_string == ".": 
			colour.rgb = MAP_FLOOR_COLOUR
			
		else: 
			colour.rgb = MAP_INVALID_COLOUR
#<---- Update			
def update_object_positions():
	update_character_position()
	update_sprites_position()
	
def draw_map(init=False):
	if init:
		set_map_bg()
		set_player_icon()
		draw_map_blocks(init=True)											
	else:
		draw_map_blocks(False)
	
def set_map_bg():
	_map.bg_colour.rgb = MAP_BACKGROUND_COLOUR
	_map.bg_rectangle.size = map_size()
	_map.bg_rectangle.pos = map_centre_o()
	
def set_player_icon():
	_player.mmp_rect.size = (c_block_size(), c_block_size())
	_player.mmp_rect.texture = get_map_texture('rockman.png')						
					
def add_player_to_mmp():
	if _map.in_cnvs and not _player.in_mmp_cnvs:
		_window.canvas.add(_player.mmp_colour)
		_window.canvas.add(_player.mmp_rect)
		_window.canvas.add(_player.mmp_line)
		_player.in_mmp_cnvs = True
	
def remove_player_from_mmp():
	if _player.in_mmp_cnvs:
		_window.canvas.remove(_player.mmp_colour)
		_window.canvas.remove(_game.player.mmp_rect)
		_window.canvas.remove(_game.player.mmp_line)
		_player.in_mmp_cnvs = False
			
def add_sprite_to_mmp(sprt):
	if _map.in_cnvs and not sprt.in_mmp_cnvs:
		sprt.in_mmp_cnvs = True
		_window.canvas.add(sprt.mmp_colour)
		_window.canvas.add(sprt.mmp_rect)
		if DEBUG_MAP_SPRITES:
			_window.canvas.add(sprt.mmp_line_colour)
			_window.canvas.add(sprt.mmp_line) 

def remove_sprite_from_mmp(sprt):
	if sprt.in_mmp_cnvs:
		sprt.in_mmp_cnvs = False
		_window.canvas.remove(sprt.mmp_colour)
		_window.canvas.remove(sprt.mmp_rect)
		if DEBUG_MAP_SPRITES:
			_window.canvas.remove(sprt.mmp_line_colour)
			_window.canvas.remove(sprt.mmp_line)
		
def show_all_sprites_to_mmp():
	for entry in _game.sprite_space.all_sprites:
		add_sprite_to_mmp(entry)
		
def hide_all_sprites_from_mmp():
	for entry in _game.sprite_space.all_sprites:
		remove_sprite_from_mmp(entry)
		
def d_add_mmp_to_game_cnvs():
	_window.canvas.add(_map.bg_colour)
	_window.canvas.add(_map.bg_rectangle)

	for idx, entry in enumerate(_map.rects):
		for inst in entry:
			_window.canvas.add(inst)
			
	_map.in_cnvs = True	
	
def d_remove_mmp_from_game_cnvs():
	_window.canvas.remove(_map.bg_colour)
	_window.canvas.remove(_map.bg_rectangle)

	for entry in _map.rects:
		for inst in entry:
			_window.canvas.remove(inst)
		
	remove_player_from_mmp()
	
	remove_all_sprites_from_mmp()
			
	_map.in_cnvs = False	
	

				