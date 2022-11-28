
from scripts.cards.card import Card
from settings import *

_bgkwargs = {'color':(0.1,0.1,0.1,0), 'size':(100,100), 'pos':(0,0)}
_ikwargs = {'image_name':'py.png', 'image_category':'game', 'color':(1,1,1,0), 'size':(100,100), 'pos':(0,0)}
_tkwargs = {'text':'', 'font_name':'Modenine', 'halign':'center', 'valign':'middle', 'font_size':100,  'text_color':(1,0.3,0.1,1), 'text_size':(100,100), 'padding_x':100, 'padding_y':100}
_bkwargs = {'text':'BUTTON', 'background_color':(0,0,0,0), 'font_name':'AdventureRequest', 'font_size':100, 'text_color':(1,1,1,0), 'size':(100,100), 'pos':(0,0), 'callback':None}


class ScoreCard(Card):
	def __init__(self, game, window, hide=False, bgkwargs=_bgkwargs, ikwargs=_ikwargs, tkwargs=_tkwargs, bkwargs=_bkwargs):
		super().__init__(game=game,  window=window, hide=False, bgkwargs=bgkwargs, ikwargs=ikwargs, tkwargs=tkwargs, bkwargs=bkwargs)
		
		if self.window.width > self.window.height:
			self.text_size = self.window.height, self.window.height
		else:
			self.text_size = self.window.width, self.window.width
		
		self.all_kills = self.game.player.count_all_kills()
		self.lamda_generator = None
		self.counting_string_generator = None
		self.row_list = []
		self.line_tracker = ''
		
		if not self.all_kills:
			self.all_kills = {'Zero Kills' : 3}
			f = lambda key: ('{} \" \t {}'.format(key, '0' * i) for i in range(self.all_kills[key]))
		else:
			f = lambda key: ('{} \" \t {}'.format(key, i + 1) for i in range(self.all_kills[key]))

		self.lamda_generator = (f(key) for key in self.all_kills)
		self.counting_string_generator = next(self.lamda_generator)
		
		self.accum_time = 0
		self.flip_time = 0.2

	#<----Base Functions: re_init, update			
	def re_init(self):
		pass
				
	def update(self,dt):
	
		self.accum_time += dt
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0

			try:
				render_line = ''
				for row in self.row_list:
					render_line += row +'\n'

				self.line_tracker = next(self.counting_string_generator)
				self.text = render_line + self.line_tracker
			
				self.game.audio.notify('beep')
			
			except StopIteration:
				self.row_list.append(self.line_tracker)
			
				try:
					self.counting_string_generator = next(self.lamda_generator)

				except StopIteration:
					self.game.event.score_card_finished()
					self.enable_tick = False
				
	#<----Window Functions: re_size, show, hide, remove		
	def re_size(self):
		pass
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()