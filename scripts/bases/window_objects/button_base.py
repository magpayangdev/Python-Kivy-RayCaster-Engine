
from kivy.uix.button import Button
from scripts.bases.window_objects.window_object import WindowObject

_TEXT, _FONT_NAME, _FONT_SIZE = 'BUTTON', 'Modenine', (100,100) 
_BG_COLOR, _TEXT_COLOR, _SIZE, _POS = (1,1,1,0), (1,1,1,1), (100,100), (0,0)
_EXTERNAL_CALLBACK, _HIDE = None, False


class ButtonBase(WindowObject):
	def __init__(self, game, window, callback= _EXTERNAL_CALLBACK, text=_TEXT, bg_color=_BG_COLOR, font_name=_FONT_NAME, font_size=_FONT_SIZE, text_color=_TEXT_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().__init__(game=game, window=window)
			
		self.button = Button()

		self.text = text
		self.font_name = font_name
		self.font_size = font_size
		self.text_color = text_color
		self.background_color = bg_color
		self.size = size
		self.pos = pos

		if callback:		
			self.button.bind(state=callback)
		else:
			self.button.bind(state=self.button_callback)
			
		if hide:
			if self.in_cnvs:
				self.window.remove_widget(self.button)
				self.in_cnvs=False
		else:
			if not self.in_cnvs:
				self.window.add_widget(self.button)
				self.in_cnvs=True

	#<----Button Funcs
	def button_callback(self, instance, state):
		if state == 'down':
			self.button_down(instance)
			
		elif state == 'normal':
			self.button_normal(instance)
			
		else:
			raise Exception('Invalid button state: {}'.format(state))
			
	def button_down(self, instance):
		pass
		
	def button_normal(self, instance):
		pass

	def does_collide(self, touch):
		return self.button.collide_point(*touch.pos)
				
	#<----Properties Button
	#property
	@property
	def background_color(self):
		return self.button.background_color
		
	@background_color.setter
	def background_color(self, value):
		self.button.background_color = value
		
	@property
	def font_name(self):
		return self.button.font_name
		
	@property
	def font_size(self):
		return self.button.font_size

	@property
	def text_color(self):
		return self.button.color
				
	@property
	def callback(self):
		return None
		
	@property
	def state(self):
		return self.button.state
			
	@property
	def widget(self):
		return self.button
	
	@property
	def text(self):
		return self.button.text
			
	@property
	def size(self):
		f = lambda x,y: (x * self.window.width, y * self.window.height)
		return f(*self.button.size_hint)
			
	@property
	def pos(self):
		return self.button.pos
		
	#<----Setters
	@font_name.setter
	def font_name(self, value):
		self.button.font_name = value

	@font_size.setter
	def font_size(self, value):
		self.button.font_size = value

	@text_color.setter
	def text_color(self, value):
		self.button.color = value
		
	@callback.setter
	def callback(self, value):
		self.button.bind(state=value)
		
	@state.setter
	def state(self, value):
		if value in ('normal','down'):
			self.button.state = value
		else:
			raise Exception('Invalid button state {}'.format(value))
			
	@text.setter
	def text(self, value):
		self.button.text = value

	@size.setter
	def size(self, value):
		f = lambda x,y: (x / self.window.width, y / self.window.height)
		self.button.size_hint = f(*value)
		
	@pos.setter
	def pos(self, value):
		f = lambda x,y: (x - self.size[0] / 2, y - self.size[1] / 2)
		self.button.pos = f(*value)
					
	#<----Base Functions: re_init, update			
	def re_init(self, callback=_EXTERNAL_CALLBACK, text=_TEXT, bg_color=_BG_COLOR, font_name=_FONT_NAME, font_size=_FONT_SIZE, text_color=_TEXT_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().re_init()
		
		self.text = text
		self.font_name = font_name
		self.font_size = font_size
		self.text_color = text_color
		self.background_color = bg_color
		self.size = size
		self.pos = pos

		if callback:		
			self.button.bind(state=callback)
		else:
			self.button.bind(state=self.button_callback)
			
		if hide:
			if self.in_cnvs:
				self.window.remove_widget(self.button)
				self.in_cnvs=False
		else:
			if not self.in_cnvs:
				self.window.add_widget(self.button)
				self.in_cnvs=True
				
		
	def update(self,dt):
		super().update(dt)
		
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()

	def show(self):
		super().show()
		
		if not self.in_cnvs:
			self.window.add_widget(self.button)
			self.in_cnvs=True
					
	def hide(self):
		super().hide()
		
		if self.in_cnvs:
			self.window.remove_widget(self.button)
			self.in_cnvs=False
					
	def remove(self):
		super().hide()
		
		self.hide()
	
		del(self.button)
