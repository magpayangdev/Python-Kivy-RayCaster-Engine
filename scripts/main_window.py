
""" The Main Window.
	Creates the loading screen object. 
	Handles touch inputs exit game signals. 
	Provides the canvas for most of the game objects. """

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from scripts.game.game_mode import GameMode

from kivy.clock import Clock
class MainWindow(FloatLayout):
	def __init__(self, **kwargs):
		super(MainWindow, self).__init__(**kwargs)				

		self.bind(size=self.re_init, pos=self.re_init)
		self.game_mode = GameMode(window=self, mode='mode 1')

	def re_init(self, instance, *args): 
		self.game_mode.re_init()
					
	def quit_game(self):
		App.get_running_app().stop()
						
	def on_touch_down(self, touch):
		self.game_mode.event.on_touch_down(touch)
						
	def on_touch_move(self, touch):
		self.game_mode.event.on_touch_move(touch)
							
	def on_touch_up(self, touch):
		self.game_mode.event.on_touch_up(touch)
