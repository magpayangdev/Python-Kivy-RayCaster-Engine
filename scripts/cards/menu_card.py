
from scripts.cards.card import Card
from scripts.bases.window_objects.drop_down_base import DropDownBase

_bgkwargs = {'color':(0.5,0.1,0.3,1), 'size':(100,100), 'pos':(0,0)}
_ikwargs = {'image_name':'py.png', 'image_category':'game', 'color':(1,1,1,0), 'size':(100,100), 'pos':(0,0)}
_tkwargs = {'text':'Game Title', 'font_name':'AdventureRequest', 'halign':'center', 'valign':'top', 'font_size':200,  'text_color':(1,1,1,1), 'text_size':(0,0), 'padding_x':100, 'padding_y':0}
_bkwargs = {'text':'Start', 'bg_color':(1,1,1,1), 'font_name':'AdventureRequest', 'font_size':100, 'text_color':(1,1,1,1), 'size':(500,200), 'pos':(0,0), 'nomal_callback':None, 'down_callback':None}
_bmkwargs = {'text':'Game Mode', 'bg_color':(1,1,1,1), 'font_name':'AdventureRequest', 'font_size':70, 'text_color':(1,1,1,1), 'size':(0,0), 'pos':(0,0), 'callback':None}


class MenuCard(Card):
	def __init__(self, game, window, hide=False, bgkwargs=_bgkwargs, ikwargs=_ikwargs, tkwargs=_tkwargs, bkwargs=_bkwargs):
		super().__init__(game=game, window=window, hide=hide, bgkwargs=bgkwargs, ikwargs=ikwargs, tkwargs=tkwargs, bkwargs=bkwargs)
		
		self.dd_list = ['Arena', 'Back Rooms']
		
		#<---- Text Settings
		self.text_size = self.window.width, self.window.height
		self.padding_y = self.window.height / 3

		#<---- Button Settings
		self.button_pos = self.window.width / 2 , self.window.height / 3
		
		#<---- DropDown Settings
		size = 700, 100
		pos = self.window.width / 2, self.window.height / 6
		_bmkwargs.update({'size':size, 'pos':pos, 'on_select':self.drop_down_selected})
		self.dp_down_comp = DropDownBase(self.game, dd_list=self.dd_list, **_bmkwargs)
		
		self.all_buttons.append(self.dp_down_comp)
	
	#<----Button Funcs
	def drop_down_selected(self, *args):
		pass

	def button_down(self):
		super().button_down()
		
	def button_up(self):
		super().button_up()
		
		try:		
			text = self.dp_down_comp.text
			self.game.mode = self.dd_list.index(text)
			
		except ValueError:
			raise Exception('Invalid Game Mode Selection: {}'.format(text))

		self.game.event.re_init_game()

	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.dp_down_comp.re_init()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def show(self):
		super().show()
		
		self.dp_down_comp.show()
			
	def hide(self):
		super().hide()
		
		self.dp_down_comp.hide()
			
	def remove(self):
		super().remove()
		
		self.dp_down_comp.remove()
		
		