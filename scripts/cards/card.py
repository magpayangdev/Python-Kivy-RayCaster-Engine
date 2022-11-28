
from scripts.bases.window_objects.text_base import TextBase
from scripts.bases.window_objects.rect_base import RectBase
from scripts.bases.window_objects.textured_rect import TexturedRect
from scripts.bases.window_objects.button_base import ButtonBase

_bgkwargs = {'color':(0.1,0.1,0.1,1), 'size':(100,100), 'pos':(0,0)}
_ikwargs = {'image_name':'py.png', 'image_category':'game', 'color':(1,1,1,1), 'size':(100,100), 'pos':(0,0)}
_tkwargs = {'text':'Label Text', 'font_name':'Modenine', 'halign':'center', 'valign':'middle', 'font_size':100,  'text_color':(0.5,0.3,0.1,1), 'text_size':(100,100), 'padding_x':100, 'padding_y':100}
_bkwargs = {'text':'BUTTON', 'background_color':(0,0,0,1), 'font_name':'AdventureRequest', 'font_size':100, 'text_color':(1,1,1,1), 'size':(100,100), 'pos':(0,0), 'callback':None}

class Card(RectBase):
	def __init__(self, game,  window, hide=False, bgkwargs=_bgkwargs, ikwargs=_ikwargs, tkwargs=_tkwargs, bkwargs=_bkwargs):
		super().__init__(game=game, window=window, hide=hide, **bgkwargs)
		
		self.size = self.window.size
		self.pos = self.window.pos
		
		bkwargs.update({'callback':self.button_callback})
		
		self.image_comp = TexturedRect(game=game, window=window, hide=hide, **ikwargs)
		self.text_comp = TextBase(game=game, window=window, hide=hide, **tkwargs)
		self.button_comp = ButtonBase(game=game, window=window, hide=hide, **bkwargs)

	#<----Image Properties
	@property
	def image_texture(self):
		return self.image_comp.texture
		
	@property
	def image_color(self):
		return self.image_comp.color
		
	@property
	def image_size(self):
		return self.image_comp.size
		
	@property
	def image_pos(self):
		return self.image_comp.pos
	
	#<----Image Setter	
	@image_texture.setter
	def image_texture(self, value):
		self.image_comp.texture = value
		
	@image_color.setter
	def image_color(self, value):
		self.image_comp.color = value
		
	@image_size.setter
	def image_size(self, value):
		self.image_comp.size = value
		
	@image_pos.setter
	def image_pos(self, value):
		self.image_comp.pos = value

	#<----Button Properties	
	@property
	def button_state(self):
		return self.button_comp.state
		
	@property
	def button_widget(self):
		return self.button_comp.widget
	
	@property
	def button_text(self):
		return self.button_comp.text
			
	@property
	def button_size(self):
		return self.button_comp.size
			
	@property
	def button_pos(self):
		return self.button_comp.pos
		
	#<----Button Setter
	@button_state.setter
	def button_state(self, value):
		self.button_comp.state = value
		
	@button_text.setter
	def button_text(self, value):
		self.button_comp.text = value
		
	@button_size.setter
	def button_size(self, value):
		self.button_comp.size = value
		
	@button_pos.setter
	def button_pos(self, value):
		self.button_comp.pos = value
		
	#<----Text Properties		
	@property
	def text(self):
		return self.text_comp.text
		
	@property
	def text_size(self):
		return self.text_comp.size
		
	#<----Text Setter
	@text.setter
	def text(self, value):
		self.text_comp.text = value
		
	@text_size.setter
	def text_size(self, value):
		self.text_comp.size = value
		
	#<----Button Funcs	
	def button_callback(self, instance, state):
		if state == 'down':
			self.button_down()
			
		elif state == 'normal':
			self.button_up()
			
		else:
			raise Exception('Invalid button state: {}'.format(state))
			
	def button_down(self):
		pass
		
	def button_up(self):
		pass
	
	#<----Base Functions: re_init, update			
	def re_init(self):
		pass
				
	def update(self,dt):
		pass
				
	#<----Window Functions: re_size, show, hide, remove		
	def re_size(self):
		pass
		
	def show(self):
		super().show()
		
		self.image_comp.show()
		self.text_comp.show()
		self.button_comp.show()
			
	def hide(self):
		super().hide()
		
		self.image_comp.hide()
		self.text_comp.hide()
		self.button_comp.hide()
			
	def remove(self):
		super().remove()
		
		self.hide()
		
		del(self.image_comp)
		del(self.text_comp)
		del(self.button_comp)
			
	