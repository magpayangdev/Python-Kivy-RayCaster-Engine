
from settings import *

_start_button_kwargs = None



def init(menu):
	pass

def re_init(menu):
	global _start_button_kwargs
	
	_start_button_kwargs = None

	button_width, button_height = 320, 175
	
	screen_width, screen_height = menu.game.window.size
	
	h_s_w = screen_width / 2
	h_s_h = screen_height / 2
		
	pos_x = 0.5
	pos_y = (screen_height / 2 - button_height - button_height / 2) / screen_height
	
	_start_button_kwargs = {'bg_normal':'', 'bg_down':'', 'text':'Start Game', 'color':(1,1,1), 'font_name':'AdventureRequest', 'size':(button_width, button_height), 'pos_hint':{'center_x':pos_x, 'center_y': pos_y}, 'callback':menu.button_cb}
	
	