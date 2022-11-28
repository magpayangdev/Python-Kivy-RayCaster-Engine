
from scripts.cards.text_frame import TextFrame
from scripts.bases.timed_updates.timed_update import TimedUpdate


from settings import *

class TypingTextFrame(TimedUpdate):
	def __init__(self, game, window, hide=False, flip_time=0.1, pause_speed=1, start_iter=True, bg_color=(0.5,0.3,0.1,1), image_name="py.png", image_category="game", text=SAMPLE_TEXT, font_name="Modenine", halign='right', valign='bottom', font_size=100, text_color=(0,0,0,1), padding_x=100, padding_y=100):
		super().__init__(game, flip_time=flip_time, start_iter=start_iter)
		
		self.frame_comp = TextFrame(game=game, window=window, hide=hide, bg_color=bg_color, image_name=image_name, image_category=image_category, text="", font_name=font_name, halign=halign, valign=valign, font_size=font_size, text_color=text_color, padding_x=padding_x, padding_y=padding_y)
		
		self.message = text
		self.pause_speed = pause_speed
		self.typing_speed = self.flip_time
		
		self.button_pos = self.window.width - self.button_size[0] - 10 , self.button_size[1] + 10
		
	#<----Properties Window
	@property
	def window(self):
		return self.frame_comp.window
		
	@property
	def button_widget(self):
		return self.frame_comp.button_widget
		
	@property
	def button_comp(self):
		return self.frame_comp.button_comp
	
	#<----Properties Button	
	@property
	def button_text(self):
		return self.frame_comp.button_text

	@property
	def button_size(self):
		return self.frame_comp.button_size
		
	@property
	def button_pos(self):
		return self.frame_comp.button_pos

	#<----Setter Button		
	@button_text.setter
	def button_text(self, value):
		self.frame_comp.button_text = value

	@button_size.setter
	def button_size(self, value):
		self.frame_comp.button_size = value

	@button_pos.setter
	def button_pos(self, value):
		self.frame_comp.button_pos = value
		
	#<----Properties Text
	@property
	def text(self):
		return self.frame_comp.text
	
	@text.setter
	def text(self, value):
		self.frame_comp.text=value
		
	#<---- Touch Down
	def on_touch_down(self, touch):
		#super().on_touch_down(touch)
		pass
			
	#<---- Touch Move	
	def on_touch_move(self, touch):
		#super().on_touch_move(touch)
		pass
				
	#<---- Touch Up
	def on_touch_up(self, touch):
		#super().on_touch_up(touch)
		pass


		

	#<----Base Functions: re_init, update
	def re_init(self):
		super().re_init()
		
	def update(self, dt):
		super().update(dt)
		
		if not self.start_iter:
			return
		
		self.accum_time += dt
		self.fbf_update(dt)
		
		if self.accum_time > self.flip_time:
			self.accum_time = 0
			self.timed_update()

	#<----Update Functions: fbf_update, timed_update			
	def fbf_update(self, dt):
		pass
		
	def timed_update(self):
		if self.do_once:
			self.do_once = False
			self.do_once_func()

		try:
			self.try_func()
			
		except StopIteration:
			self.stop_iteration_func()
			
		except IndexError:
			self.index_error_func()
			
	def index_error_func(self):

		
	#<----Timed Update Functions: do_once_func, try_func, stop_iteration_func	
	def do_once_func(self):		
		pass
			
	def try_func(self):

		
	def stop_iteration_func(self):
		super().stop_iteration_func()
		
		
	#<----Loop Controls: start, resume, loop, stop	
	def start(self):
		super().start()
		
	def resume(self):		
		super().resume()
		
	def loop(self):
		super().loop()
		
	def stop(self):
		super().stop()

	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()
		
		self.frame_comp.re_size()

	def show(self):
		self.frame_comp.show()
			
	def hide(self):
		self.frame_comp.hide()
			
	def remove(self):
		self.hide()
		del(self.frame_comp)





















