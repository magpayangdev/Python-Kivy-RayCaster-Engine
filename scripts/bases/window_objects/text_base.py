# base_direction: None, “ltr”, “rtl”, “weak_ltr”, and “weak_rtl”.
# halign: auto, left, center, right and justify
# valign:  ‘bottom’, ‘middle’ (or ‘center’) and ‘top’.

from kivy.uix.label import Label
from scripts.bases.window_objects.window_object import WindowObject


_PADDING_X, _PADDING_Y, _HIDE = 100, 100, False
_FONT_SIZE, _TEXT_COLOR, _TEXT_SIZE = 100, (1,1,1,1), (100,100)
_TEXT, _FONT_NAME, _HALIGN, _VALIGN = 'Label Text', 'Roboto', 'center', 'middle'


class TextBase(WindowObject):
	def __init__(self, game, window, text=_TEXT, font_name=_FONT_NAME, halign=_HALIGN, valign=_VALIGN, font_size=_FONT_SIZE,  text_color=_TEXT_COLOR, text_size=_TEXT_SIZE, padding_x=_PADDING_X, padding_y=_PADDING_Y, hide=_HIDE, **kwargs):
		super().__init__(game=game, window=window)
				
		self.label=None
		try:
			self.label = Label(text=text, font_name=font_name, halign=halign, valign=valign, font_size=font_size, text_size=text_size, color=text_color, markup=True)
			
		except IOError:
			self.label = Label(text=text) 

		self.label.padding_x = padding_x
		self.label.padding_y = padding_y
		
		if hide:
			if self.in_cnvs:
				self.window.remove_widget(self.label)
				self.in_cnvs=False
		else:
			if not self.in_cnvs:
				self.window.add_widget(self.label)
				self.in_cnvs=True
							
	#<----Getters
	@property
	def color(self):
		return self.label.color
	@color.setter
	def color(self, value):
		self.label.color = value
		
	@property
	def text_size(self):
		return self.label.text_size
	@text_size.setter
	def text_size(self, value):
		self.label.text_size = value
		
	@property
	def font_size(self):
		return self.label.font_size
	@font_size.setter
	def font_size(self, value):
		self.label.font_size = value
		
	@property
	def valign(self):
		return self.label.valign
	@valign.setter
	def valign(self, value):
		self.label.valign = value
		
	@property
	def halign(self):
		return self.label.halign
	@halign.setter
	def halign(self, value):
		self.label.halign = value
		
	@property
	def font_name(self):
		return self.label.font_name
	@font_name.setter
	def font_name(self, value):
		self.label.font_name = value
					
	@property
	def size(self):
		return self.label.text_size
				
	@property
	def text(self):
		return self.label.text

	@property
	def pad_x(self):
		return self.label.padding_x
		
	@property
	def pad_y(self):
		return self.label.padding_y

	#<----Setters
	@size.setter
	def size(self, value):
		self.label.text_size = value
				
	@text.setter
	def text(self, value):
		self.label.text = value
		
	@pad_x.setter
	def pad_x(self, value):
		self.label.padding_x = value
		
	@pad_y.setter
	def pad_y(self, value):
		self.label.padding_y = value


	#<----Base Functions: re_init, update		
	def re_init(self, text=_TEXT, font_name=_FONT_NAME, halign=_HALIGN, valign=_VALIGN, font_size=_FONT_SIZE,  text_color=_TEXT_COLOR, text_size=_TEXT_SIZE, padding_x=_PADDING_X, padding_y=_PADDING_Y, hide=_HIDE, **kwargs):
		super().re_init()
		
		try:
			self.text = text
			self.font_name = font_name
			self.halign = halign
			self.valign = valign
			self.font_size = font_size
			self.text_size = text_size
			self.color = text_color
			
		except Exception:
			self.text = text
		
		if hide:
			if self.in_cnvs:
				self.window.remove_widget(self.label)
				self.in_cnvs=False
		else:
			if not self.in_cnvs:
				self.window.add_widget(self.label)
				self.in_cnvs=True
			
	def update(self, dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()

	def show(self):
		super().show()
		
		if not self.in_cnvs:
			self.window.add_widget(self.label)
			self.in_cnvs=True
			
	def hide(self):
		super().hide()
		
		if self.in_cnvs:
			self.window.remove_widget(self.label)
			self.in_cnvs=False
			
	def remove(self):
		super().remove()
		
		self.hide()	
		
		del(self.label)
		