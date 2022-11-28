
from kivy.uix.layout import Layout
from scripts.bases.window_objects.window_object import WindowObject

class LayoutBase(WindowObject):
	def __init__(self, game, window, hide=False):
		super().__init__(game=game, window=window)

		self.layout=None

		self.layout = Layout()
		self.window.add_widget(self.layout)
		self.in_cnvs = True
		
		if hide:
			self.hide()
		else:
			self.show()
	
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
			self.window.add_widget(self.layout)
			self.in_cnvs = True
		
	def hide(self):
		super().hide()
		
		if self.in_cnvs:
			self.window.remove_widget(self.layout)
			self.in_cnvs = False
		
	def remove(self):
		super().remove()
		
		self.hide()
