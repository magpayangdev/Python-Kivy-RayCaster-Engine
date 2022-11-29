
# kwargs = {'game':self.game, 'window':self.window, 'hide':True, 'text':'EXIT', 'background_color':(0,0,0,1), 'font_name':'AdventureRequest', 'font_size':50, 'text_color':(1,1,1,1), 'size':self.button_size, 'pos':f(*self.button_size), 'callback':None}

from kivy.uix.button import Button
from scripts.bases.window_objects.window_object import WindowObject

class ButtonBase(WindowObject):
	def __init__(self, game, window, hide=False, text='BUTTON', background_color=(0,0,0,1), font_name='AdventureRequest', font_size=100, text_color=(1,1,1,1), size=(100,100), pos=(0,0), callback=None):
		super().__init__(game=game,window=window)
		
		#self.on_press_cb = None
		#self.on_release_cb = None
		
		self.init_text = text
		self.init_text_color = text_color

		self.init_size = (size[0] / self.window.width, size[1] / self.window.height)
		self.init_pos = (pos[0] - size[0] / 2, pos[1] - size[1] / 2)
			
		self.button = Button(text=text, background_color=background_color, font_name=font_name, font_size=font_size, color=text_color, size_hint=self.init_size, pos=self.init_pos)
		
		if callback:
			self.button.bind(state=callback)
		
		if hide:
			self.window.remove_widget(self.button)
			self.in_cnvs=False
		else:
			self.window.add_widget(self.button)
			self.in_cnvs=True
				
	#<----Properties Button		
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
		
	#<----Button Funcs
	def does_collide(self, touch):
		return self.button.collide_point(*touch.pos)
					
	#<----Base Functions: re_init, update			
	def re_init(self):
		super().re_init()
		
		self.button.text = self.init_text
		self.button.text_color = self.init_text_color
		self.button.size_hint = self.init_size
		self.button.pos = self.init_pos
		
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
