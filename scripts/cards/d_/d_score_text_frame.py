
from scripts.cards.text_frame import TextFrame
from settings import *


class ScoreTextFrame(TextFrame):
	def __init__(self, game, hide=False):
		super().__init__(game=game, window=False, hide=hide, bg_color=(0.1,0.5,0.3,1), image_name="py.png", image_category="game", text=SAMPLE_TEXT, font_name="Modenine", halign='center', valign='middle', font_size=100, text_color=(0.5,0.3,0.1,1), padding_x=100, padding_y=100, button_bg=(0.5,0.3,0.1,1), button_text='Skip', button_font_name='AdventureRequest', button_font_size=40, button_t_color=(1,1,1,1), button_size=(250,100), button_pos=(0, 0))
		
		self.accum_time = 0
		self.flip_time = 1
		
		self.background.remove()
		self.frame_image.remove()
		self.frame_button.remove()
	
		
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
	def update(self, dt):
		#super().update(dt)
		



	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		pass

	def show(self):
		super().show()
			
	def hide(self):
		super().hide()
					
	def remove(self):
		super().remove()

