
""" More than just a loading screen! 
	Also manages the creation of all textures and audio dictionaries.
	Textures dicts are the {<key.png>: <Texture Object>} and the {<sprite id>:((<TObjIdle>), (<TObjWalk>)...)}"""

from scripts.bases.window_objects.labelled_rect import LabelledRect

class LoadingScreen(LabelledRect):
	def __init__(self, game, window=None, text='Loading Screen', font_name='Modenine', font_size=100, color=(1,1,1,1), size=(100,100), pos=(0,0), hide=False):
		super().__init__(game=game, window=window, text=text, font_name=font_name, font_size=font_size, color=color, size=size, pos=pos, hide=hide)
		
		self.rect.size = self.window.size
		self.rect.pos = self.window.pos

	#<----Base Functions: re_init, update			
	def re_init(self):
		self.rect.size = self.window.size
		self.rect.pos = self.window.pos
		
		super().re_init()
		
	def update(self,dt):
		super().update(dt)
		
	#<----Rectangle Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()

	def show(self):
		super().show()
					
	def hide(self):
		super().hide()
				
	def remove(self):
		super().remove()
		
		del(self.game.l_screen)

