
""" Ray Caster Engine """	

from kivy.app import App
from scripts.main_window import MainWindow	

class MainApp(App):
	def build(self):
		root = MainWindow()
		root.bind(size=root.re_init,pos=root.re_init)
		return root

if __name__ == "__main__":
	MainApp().run()

__version__="1.0.3"
