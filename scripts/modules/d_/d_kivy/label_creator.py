
from kivy.uix.label import Label

def basic_label(window, label_ref, text='Label Creator', font_name='Modenine', font_size=100):
		if label_ref:
			window.remove_widget(label_ref)
	
		try:
			label = Label(text=text, font_name=font_name, font_size=font_size)
			
		except IOError:
			label = Label(text=text, font_size=font_size)
			
		window.add_widget(label)
		
		return label
		
def positioned_label(window, label_ref, text, color, size_hint, pos_hint):
	if  label_ref:
		window.remove_widget(label_ref)

	label = Label(text = text, color = color, size_hint = size_hint, pos_hint = pos_hint)

	window.add_widget(label)
	
	return label		