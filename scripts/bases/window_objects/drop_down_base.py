
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from scripts.bases.window_objects.button_base import ButtonBase


_TEXT, _FONT_NAME, _FONT_SIZE = 'BUTTON', 'AdventureRequest', (100,100) 
_BG_COLOR, _TEXT_COLOR, _SIZE, _POS = (1,1,1,1), (1,1,1,1), (100,100), (0,0)
_CALLBACK, _HIDE, _DD_LIST = None, False, [None,]


class DropDownBase(ButtonBase):
	def __init__(self, game, window=None, dd_list=_DD_LIST, callback=_CALLBACK, on_select=None, text=_TEXT, bg_color=_BG_COLOR, font_name=_FONT_NAME, font_size=_FONT_SIZE, text_color=_TEXT_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().__init__(game=game, window=window, callback=callback, text=text, bg_color=bg_color, font_name=font_name, font_size=font_size, text_color=text_color, size=size, pos=pos, hide=hide)
		
		self.dropdown = DropDown()
		self.drop_down_list = dd_list
		
		for idx in range(len(self.drop_down_list)):
			btn = Button(text=str(self.drop_down_list[idx]), size_hint_y=None, height=44)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)
			
		self.button.text = str(self.drop_down_list[0])
		
		self.dropdown.bind(on_select=self.on_select)
		self.dropdown.bind(on_dismiss=self.on_dismiss)
		
		self.callback = on_select
		
	#<----Drop Down Funcs
	def on_dismiss(self, *args):
		self.state = 'normal'
		
	def on_select(self, instance, button_text):
		self.text = button_text
		self.state = 'normal'
		
		if self.callback:
			self.callback()

	#<----Button Funcs
	def button_down(self, instance):
		super().button_down(instance)
		self.dropdown.open(instance)
		
	def button_normal(self, instance):
		super().button_normal(instance)
		
	def re_init(self, dd_list=_DD_LIST, callback=_CALLBACK, text=_TEXT, bg_color=_BG_COLOR, font_name=_FONT_NAME, font_size=_FONT_SIZE, text_color=_TEXT_COLOR, size=_SIZE, pos=_POS, hide=_HIDE, **kwargs):
		super().re_init(callback=callback, text=text, bg_color=bg_color, font_name=font_name, font_size=font_size, text_color=text_color, size=size, pos=pos, hide=hide)
		
		self.button.text = str(self.drop_down_list[0])
		self.state = 'normal'
	
	def update(self,dt):
		super().update(dt)
		
	#<----Window Functions: re_size, show, hide, remove
	def re_size(self):
		super().re_size()

	def show(self):
		super().show()
		
					
	def hide(self):
		super().hide()
					
	def remove(self):
		super().hide()

		self.window.remove_widget(self.dropdown)
		self.dropdown=None