from settings import *

_proceed_button = {}
_skip_button = {}


def init(text_card):
	global _proceed_button
	global _skip_button

	_proceed_button = {'font_name':'AdventureRequest', 'font_size':'20sp', 'text':"PROCEED", 'size':(300.0,100.0), 'pos_hint':{'center_x':0.5, 'y':0}, 'callback':text_card.proceed}	
	
	_skip_button = {'font_name':'AdventureRequest', 'font_size':'20sp', 'text':'SKIP', 'size':(300.0,100.0), 'pos_hint':{'right':1, 'y':0}, 'callback':text_card.skip}