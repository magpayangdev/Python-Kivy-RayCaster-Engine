
from settings import *
from scripts.modules.loaders.user_config_loader import *


_exit_button = {}
_left_button = {}
_right_button = {}
_centre_button = {}
_debug_text_kwargs = {}
_hit_rect_kwargs = {}

def init(hud_b):
	global _exit_button
	global _left_button
	global _right_button
	global _centre_button
	global _debug_text_kwargs
	global _hit_rect_kwargs
	
	game = hud_b.game
	
	s_x = float(game.kw_args.get('button_width'))
	s_y = float(game.kw_args.get('button_height'))
	
	_hit_rect_kwargs = {'color':(1,0,0,0),'size':game.window.size,'pos':game.window.pos}

	_debug_text_kwargs = {'text':"Debug Text",'color':DEBUG_TEXT_COLOR,'size_hint':(1,1), 'pos_hint':{'center_x':0.5, 'center_y':0.99}}
	
	pos_x, pos_y =  (scr_width() - s_x / 2) / scr_width(), (scr_height() - s_y / 2) / scr_height() 
	_exit_button =  {'bg_normal':'', 'bg_down':'', 'text':'EXIT', 'color':RED, 'font_name':'AdventureRequest', 'size':(s_x, s_y), 'pos_hint':{'center_x':pos_x,'center_y':pos_y}, 'callback':hud_b.e_b_callback}
	
	pos_x, pos_y = controller_center_left()[0] / 2 / scr_width(), 0.5
	_left_button =  {'bg_normal':'', 'bg_down':'', 'text':'ATK', 'color':RED, 'font_name':'AdventureRequest', 'size':(s_x, s_y), 'pos_hint':{'center_x':pos_x,'center_y':pos_y}, 'callback':hud_b.l_b_callback}	

	pos_x, pos_y = (controller_center_right()[0] + controller_center_left()[0] / 2)  / scr_width(), 0.5		
	_right_button =  {'bg_normal':'', 'bg_down':'', 'text':'ATK', 'color':RED, 'font_name':'AdventureRequest', 'size':(s_x, s_y), 'pos_hint':{'center_x':pos_x,'center_y':pos_y}, 'callback':hud_b.r_b_callback}
	
	pos_x, pos_y = 0.5, 50 / scr_height()
	_centre_button = {'bg_normal':'', 'bg_down':'', 'text':'MAP', 'color':RED, 'font_name':'AdventureRequest', 'size':(s_x, s_y), 'pos_hint':{'center_x':pos_x,'center_y':pos_y}, 'callback':hud_b.centre_button_callback}













