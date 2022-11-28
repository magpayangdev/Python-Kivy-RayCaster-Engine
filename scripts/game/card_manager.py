
from settings import *
from scripts.cards.menu_card import MenuCard
from scripts.cards.typing_card import TypingCard
from scripts.cards.score_card import ScoreCard
from scripts.bases.touch_objects.touch_object import TouchObject


class CardManager(TouchObject):
	def __init__(self, game):
		super().__init__(game=game)

		self.current_card = None
	
		self.intro_kwargs = {'game':self.game, 'window':self.game.window, 'hide':False, 'flip_time':0.1, 'pause_speed':1, 'start_iter':True, 'bg_color':(0.5,0.3,0.1,1), 'image_name':"py.png", 'image_category':"game", 'text':SAMPLE_TEXT, 'font_name':"Modenine", 'font_size':100, 'text_color':(0,0,0,1), 'padding_x':100, 'padding_y':100}
		
		self.menu_kwargs=None
		
	#<----Card Events
	def remove_current_card(self):
		if self.current_card:
			self.current_card.remove()
			
		self.current_card=None
		
	def show_intro_card(self):
		if self.current_card:
			self.remove_current_card()
			
		self.current_card = TypingCard(game=game, window=game.window, hide=False)
		
	def show_menu_card(self):
		if self.current_card:
			self.remove_current_card()
			
		self.current_card = MenuCard(game=game, window=game.window, hide=False)
		
	def show_score_card(self):
		if self.current_card:
			self.remove_current_card()
			
		self.current_card = ScoreCard(game=game, window=game.window, hide=False)

	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		super().update(dt)
				
		if self.current_card:
			self.current_card.update(dt)

	#<----TouchFunctions: on_touch_down, on_touch_move, on_touch_up
	def on_touch_down(self, touch):
		super().on_touch_down(touch)

		if self.current_card and self.current_card.button_comp.does_collide(touch):
			self.current_card.button_state = 'down'
	
	def on_touch_move(self, touch):
		super().on_touch_move(touch)
		
	def on_touch_up(self, touch):
		super().on_touch_up(touch)
		
		if self.current_card and self.current_card.button_comp.does_collide(touch):
			self.current_card.button_state = 'normal'
		
		
		
		
		
		
		
		
		