
#kwargs = {'game':game, 'window':window, 'text':'Label Text', 'font_name':'Modenine', 'halign':'center', 'valign':'middle', 'font_size':100,  'text_color':(0.5,0.3,0.1,1), 'text_size':(100,100), 'padding_x':100, 'padding_y':100, 'hide':False}

from kivy.uix.label import Label
from scripts.bases.window_objects.window_object import WindowObject

class TextBase(WindowObject):
	def __init__(self, game, window, text='Label Text', font_name='Modenine', halign='center', valign='middle', font_size=100,  text_color=(0.5,0.3,0.1,1), text_size=(100,100), padding_x=100, padding_y=100, hide=False):
		super().__init__(game=game, window=window)

		# base_direction: None, “ltr”, “rtl”, “weak_ltr”, and “weak_rtl”.
		# halign: auto, left, center, right and justify
		# valign:  ‘bottom’, ‘middle’ (or ‘center’) and ‘top’.
		
		self.label=None
		try:
			self.label = Label(text=text, font_name=font_name, halign=halign, valign=valign, font_size=font_size, text_size=text_size, color=text_color, markup=True)
			
		except IOError:
			self.label = Label(text=text) 

		self.label.padding_x = padding_x
		self.label.padding_y = padding_y
		
		if hide:
			self.hide()
		else:
			self.show()
			
	#<----Getters			
	@property
	def size(self):
		return self.label.text_size
				
	@property
	def text(self):
		return self.label.text

	#<----Setters
	@size.setter
	def size(self, value):
		self.label.text_size = value
				
	@text.setter
	def text(self, value):
		self.label.text = value


	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
				
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
		