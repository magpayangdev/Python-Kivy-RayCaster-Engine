
from scripts.cards.card import Card
from settings import *

_bgkwargs = {'color':(0.1,0.1,0.1,1), 'size':(100,100), 'pos':(0,0)}
_ikwargs = {'image_name':'py.png','image_category':'game','color':(0.5,0.5,0.5,1),'size':(100,100),'pos':(0,0)}
_tkwargs = {'text':'', 'font_name':'Modenine', 'halign':'right', 'valign':'bottom', 'font_size':100,  'text_color':(0,1,0,1), 'text_size':(100,100), 'padding_x':100, 'padding_y':100}
_bkwargs = {'text':'SKIP', 'background_color':(1,1,1,1), 'font_name':'AdventureRequest', 'font_size':75, 'text_color':(1,1,1,1), 'size':(275,100), 'pos':(0,0), 'callback':None}


class TypingCard(Card):
	def __init__(self, game, window, hide=False, message=SAMPLE_TEXT, pause_speed=0.5, typing_speed=0.1, bgkwargs=_bgkwargs, ikwargs=_ikwargs, tkwargs=_tkwargs, bkwargs=_bkwargs):
		super().__init__(game=game,  window=window, hide=hide, bgkwargs=bgkwargs, ikwargs=ikwargs, tkwargs=tkwargs, bkwargs=bkwargs)
		
		if self.window.width > self.window.height:
			self.image_size = self.window.height - 100, self.window.height - 100
			self.text_size = self.window.height, self.window.height
			
		else:
			self.image_size = self.window.width - 100, self.window.width - 100
			self.text_size = self.window.width, self.window.width
			
		f = lambda : (self.window.width/2-self.image_size[0]/2,self.window.height/2-self.image_size[1]/2)
		self.image_pos = f()
		
		g = lambda : (self.window.width - self.button_size[0] - 10 , self.button_size[1] + 10)
		self.button_pos = g()
		
		self.message = message
		self.pause_speed = pause_speed
		self.typing_speed = typing_speed
		self.proceed_button_size = (365, 100)
		self.idle_tick = 2.1
		
		self.accum_time = 0
		self.flip_time = self.typing_speed
		
	#<----Button Funcs				
	def button_down(self):
		super().button_down()
		
	def button_up(self):
		super().button_up()
		
		self.game.event.skip()
	
	#<----Base Functions: re_init, update	
	def re_init(self):
		super().re_init()
		
	def update(self,dt):	
		self.accum_time += dt
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0
			
			try:
				self.try_func()
			
			except IndexError:
				self.index_error_func()
			
	def try_func(self):
		self.type_next_letter()
		self.game.audio.notify('beep')
	
	def index_error_func(self):
		self.game.audio.notify('beep')
		self.flip_time = self.idle_tick

		self.button_size = self.proceed_button_size
		self.button_pos = self.window.width / 2, 10 + self.button_size[1]
		self.button_text = 'Proceed'			
				
	#<----Window Functions: re_size, show, hide, remove		
	def re_size(self):
		pass
		
	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
			
	def remove(self):
		super().remove()
		
	def type_next_letter(self):
		len_1 = len(self.message)
		len_2 = len(self.text)

		char = self.message[len_2]
		if char == ' ':
			self.flip_time = self.pause_speed

		elif char == '#':
			self.flip_time = self.pause_speed
			char = '\n'
						
		else:
			self.flip_time = self.typing_speed
			
		self.text = self.text + char
		
		if len_1 == len_2 + 1:
			self.flip_time = 1.5
