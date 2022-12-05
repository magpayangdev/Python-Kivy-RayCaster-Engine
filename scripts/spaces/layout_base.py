
from kivy.uix.layout import Layout

_HIDE = False

class LayoutBase(Layout):
	def __init__(self, game, hide=_HIDE, **kwargs):
		super(LayoutBase, self).__init__()
		
		self.game=game
		self.in_cnvs=False
		
		if not hide:
			self.game.window.add_widget(self)
			self.in_cnvs=True
		
	#<----Base Functions: re_init, update		
	def re_init(self, hide=_HIDE):
		if hide:
			self.hide()
		else:
			self.show()
				
	def update(self, dt):
		pass

	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		pass
		
	def show(self):
		if not self.in_cnvs:
			self.game.window.add_widget(self)
			self.in_cnvs = True
		
	def hide(self):
		if self.in_cnvs:
			self.game.window.remove_widget(self)
			self.in_cnvs = False
		
	def remove(self):
		self.hide()
	