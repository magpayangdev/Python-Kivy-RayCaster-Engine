
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

def basic_rect(window, color=(1,1,1,1), size=(100,100), pos=(0,0), **kwargs):
	with window.canvas:
		colour_ref = Color(rgb=color)
		rect_ref = Rectangle(size=size, pos=pos)
		
				
		return True, colour_ref, rect_ref
	return False, colour_ref, rect_ref
	
def basic_rect_rgba(window, color=(1,1,1,1), size=(100,100), pos=(0,0), **kwargs):
	with window.canvas:
		colour_ref = Color(rgba=color)
		rect_ref = Rectangle(size=size, pos=pos)
		
				
		return True, colour_ref, rect_ref
	return False, colour_ref, rect_ref

def textured_rect(window, color=(1,1,1,1), size=(100,100), pos=(0,0), texture=None, **kwargs):
	with window.canvas:
		colour_ref = Color(*color)
		rect_ref = Rectangle(size=size, pos=pos, texture=texture)
		return True, colour_ref, rect_ref
	return False, colour_ref, rect_ref	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	