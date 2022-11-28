""" Text Card Managers """

from scripts.screen_objects.text_card import *

from scripts.bases.timed_rect_bases.timed_image_text_rect import TimedImageTextRect
from scripts.bases.timed_rect_bases.text_typing_card import TextTypingCard
from scripts.bases.applied_bases.text_frame import TextFrame
from scripts.bases.applied_bases.typing_text_frame import TypingTextFrame

class TextCardManager:
	def __init__(self, game):
		self.game = game
		self.game.tc_mngr = self
		self.window = self.game.window
		self.current_card = None
		
	def re_init(self):
		pass
		
	def update(self, dt):
		if self.current_card:
			self.current_card.update(dt)
		
	#<---- Inventory Management
	def remove_current(self):
		if self.current_card:
			self.current_card.delete_card()
			self.current_card = None
		
	def show_message_card(self):
		if self.current_card:
			if not isinstance(self.current_card, MessageCard):
				self.current_card.delete_card()
				self.current_card = MessageCard(self.game)
		else:
			self.current_card = MessageCard(self.game)
			
	def show_score_card(self):
		if self.current_card:
			if not isinstance(self.current_card, ScoreCard):
				self.current_card.delete_card()
				self.current_card = ScoreCard(self.game)
		else:
			self.current_card = ScoreCard(self.game)
			
	def show_typing_card(self):
		Temp(self.game, None, hide=False)
		
		return
		if self.current_card:
			if not isinstance(self.current_card, TypingCard):
				self.current_card.delete_card()
				self.current_card = TypingCard(self.game, message=SAMPLE_TEXT)
		else:
			self.current_card = TypingCard(self.game, message=SAMPLE_TEXT)
			
	def show_ht_card(self, orientation='right'):
		#Temp(self.game, None, hide=False)
		
		self.current_card = TypingTextFrame(self.game, self.game.window)
		return
	
		if self.current_card:
			if not isinstance(self.current_card, HalfTypingCard):
				self.current_card.delete_card()
				self.current_card = HalfTypingCard(self.game, message=SAMPLE_TEXT, orientation=orientation)
		else:
			self.current_card = HalfTypingCard(self.game, message=SAMPLE_TEXT, orientation=orientation)

	def on_touch_down(self, touch):
		card = self.current_card
		if card.in_cnvs and self.game.has_finished_loading:
			if card.proceed_button and card.proceed_button_in_cnvs and card.proceed_button.collide_point(*touch.pos):
				card.proceed_button.state = 'down'
				return True
	
			elif card.skip_button and card.skip_button_in_cnvs and card.skip_button.collide_point(*touch.pos):
				card.skip_button.state = 'down'
				return True

	def on_touch_move(self, touch):
		return True
		
	def on_touch_up(self, touch):
		return True
	
		card = self.current_card
		if card.in_cnvs and self.game.has_finished_loading:
			if card.proceed_button and card.proceed_button_in_cnvs and card.proceed_button.collide_point(*touch.pos):
				card.proceed_button.state = 'normal'
				return True
	
			elif card.skip_button and card.skip_button_in_cnvs and card.skip_button.collide_point(*touch.pos):
				card.skip_button.state = 'normal'
				return True


