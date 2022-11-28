
from scripts.cards.card import Card

_bgkwargs = {'color':(0.5,0.1,0.3,1), 'size':(100,100), 'pos':(0,0)}
_ikwargs = {'image_name':'py.png', 'image_category':'game', 'color':(1,1,1,0), 'size':(100,100), 'pos':(0,0)}
_tkwargs = {'text':'Game Title', 'font_name':'AdventureRequest', 'halign':'center', 'valign':'middle', 'font_size':200,  'text_color':(1,1,1,1), 'text_size':(2000,1000), 'padding_x':100, 'padding_y':100}
_bkwargs = {'text':'Start', 'background_color':(1,1,1,1), 'font_name':'AdventureRequest', 'font_size':100, 'text_color':(1,1,1,1), 'size':(500,200), 'pos':(0,0), 'callback':None}


class MenuCard(Card):
	def __init__(self, game, window, hide=False, bgkwargs=_bgkwargs, ikwargs=_ikwargs, tkwargs=_tkwargs, bkwargs=_bkwargs):
		super().__init__(game=game, window=window, hide=hide, bgkwargs=bgkwargs, ikwargs=ikwargs, tkwargs=tkwargs, bkwargs=bkwargs)

		self.button_pos = self.window.width / 2 , self.window.height / 4
	
	#<----Button Funcs	
	def button_down(self):
		super().button_down()
		
	def button_up(self):
		super().button_up()	
		
		self.game.event.show_intro()		
	
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		pass
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()