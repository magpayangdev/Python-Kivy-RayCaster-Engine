"""
"""
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from settings import *
from scripts.modules.textures import *

import scripts.modules.kivy.button_creator as BC
import scripts.modules.kwargs.text_card_kwargs as b_kwargs




class MessageCard:
	def __init__(self, game, color=BLACK_a, message=SAMPLE_TEXT, font_size='50sp', text_size=(1000,1000)):
		self.game = game
		self.window = self.game.window
		self.accum_time = 0
		self.text_refresh_rate = 0.1
		self.enable_tick = True
		
		self.font_size = font_size
		self.text_size = text_size
		self.message = message

		self.card_colour = color
		self.bg_colour = None
		self.bg_rect = None
		self.card_label = None
		self.in_cnvs = False		
		with self.window.canvas:
			self.bg_colour = Color(rgba=self.card_colour)
			self.bg_rect = Rectangle(size=self.window.size)
			
		self.card_label = Label(text = self.message, 
								font_name = FONT_1, 
								base_direction = 'rtl',
								#halign = 'auto',
								font_size = self.font_size, 
								text_size = self.text_size, 
								color = RED, 
								markup = True)
								
		self.window.add_widget(self.card_label)
		self.in_cnvs=True
		
		self.bg_image_colour = None
		self.bg_image_rect = None
		self.proceed_button = None
		self.skip_button = None
		self.skip_button_in_cnvs = False
		self.proceed_button_in_cnvs= False
			
	def re_init(self):
		pass
		
	def update(self, dt):
		if self.enable_tick:
			self.accum_time += dt
			self.fbf_update(dt)
			
			if self.accum_time > self.text_refresh_rate:
				self.accum_time = 0
				
				self.timed_update()
	
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		pass
		
	def show_card(self):
		pass
		
	def hide_card(self):
		self.window.canvas.remove(self.bg_colour)
		self.window.canvas.remove(self.bg_rect)
		self.window.remove_widget(self.card_label)
		
	def delete_card(self):
		self.hide_card()

class ScoreCard(MessageCard):
	def __init__(self, game, color=BLACK_a, font_size='50sp', text_size=(1000,1000)):
		
								
		super().__init__(game, (0,0,0,0), '', font_size, text_size)
		
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):


class TypingCard(MessageCard):
	def __init__(self,game,color=BLACK_a,message=SAMPLE_TEXT,font_size='50sp',text_size=(1000,1000), bg_image='py.png'):
		super().__init__(game, color, message, font_size, text_size)
		b_kwargs.init(self)
		
		self.pause_speed = 0.5
		self.typing_speed = 0.1

		self.bg_image = bg_image
		self.BG_TEXTURE = get_game_texture(self.bg_image)
		self.BG_TEXTURE_SIZE = half_scr_w(), half_scr_w()
		self.BG_TEXTURE_POS = (half_scr_w()-self.BG_TEXTURE_SIZE[0]/2,half_scr_h()-self.BG_TEXTURE_SIZE[1]/2)
		with self.window.canvas:
			self.bg_image_colour = Color(1,1,1)
			self.bg_image_rect = Rectangle(texture=self.BG_TEXTURE, size=self.BG_TEXTURE_SIZE, 
											pos=self.BG_TEXTURE_POS)

		self.window.remove_widget(self.card_label)
		self.window.add_widget(self.card_label)
		self.card_label.text = ''
		self.card_label.text_size = self.BG_TEXTURE_SIZE
		self.card_label.padding_x = 100
		self.card_label.padding_y = 100
		self.in_cnvs=True

		self.show_skip_button()
								
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		
		try:
			self.game.audio.notify('beep')
			self.type_next_letter()
			
		except Exception as a:
			#raise Exception(a)
			self.hide_skip_button()
			self.show_proceed_button()
			
	def hide_card(self):
		self.window.canvas.remove(self.bg_image_colour)
		self.window.canvas.remove(self.bg_image_rect)
		
		self.hide_skip_button()
		self.hide_proceed_button()
		
		super().hide_card()
			
	def show_skip_button(self):
		self.skip_button = BC.create_font_button(self.window, self.skip_button, **b_kwargs._skip_button)
		self.skip_button_in_cnvs = True
			
	def show_proceed_button(self):	
		self.proceed_button = BC.create_font_button(self.window, self.proceed_button, **b_kwargs._proceed_button)
		self.proceed_button_in_cnvs = True
		
	def hide_skip_button(self):
		if self.skip_button_in_cnvs:
			self.window.remove_widget(self.skip_button)
			self.skip_button = None
			self.skip_button_in_cnvs = False
			
	def hide_proceed_button(self):
		if self.proceed_button_in_cnvs:
			self.window.remove_widget(self.proceed_button)
			self.proceed_button = None
			self.proceed_button_in_cnvs = False

	def skip(self, *args):
		self.card_label.text = ''
		self.game.event.skip()

	def proceed(self, *args):
		self.card_label.text = ''
		self.game.event.proceed()
		
	def type_next_letter(self):
		len_1 = len(self.message)
		len_2 = len(self.card_label.text)

		char = self.message[len_2]
		if char == ' ':
			self.text_refresh_rate = self.pause_speed

		elif char == '#':
			self.text_refresh_rate = self.pause_speed
			char = '\n'
						
		else:
			self.text_refresh_rate = self.typing_speed
			
		self.card_label.text = self.card_label.text + char
		
		if len_1 == len_2 + 1:
			self.text_refresh_rate = 1.5
		
class HalfTypingCard(TypingCard):
	def __init__(self, game, color=BLACK_a,
				message=SAMPLE_TEXT, font_size='50sp', text_size=(1000,1000), bg_image='py.png', orientation='left'):
		super().__init__(game, color, message, font_size, text_size, bg_image)

		self.img_orientation = orientation
						
		if self.img_orientation == 'left':
			self.BG_TEXTURE_POS = scr_width() / 4 - self.BG_TEXTURE_SIZE[0] / 2, half_scr_h() - self.BG_TEXTURE_SIZE[1] / 2
			self.bg_image_rect.pos = self.BG_TEXTURE_POS	
			self.card_label.pos = scr_width()/4, 0
			
		elif self.img_orientation == 'right':
			self.BG_TEXTURE_POS = 3*scr_width() / 4 - self.BG_TEXTURE_SIZE[0] / 2, half_scr_h() - self.BG_TEXTURE_SIZE[1] / 2
			self.bg_image_rect.pos = self.BG_TEXTURE_POS
			self.card_label.pos = -scr_width() / 4, 0	
			
		else:
			raise Exception('Invalid img_orientation {}'.format(self.img_orientation))
			
			
			
			
			
			
			
			
			
			
			