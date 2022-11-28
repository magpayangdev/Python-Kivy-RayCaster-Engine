""" Clocked Componenent of the loading screen """

from kivy.clock import Clock

_accum_time=0
_do_once=True
_loading_screen = None

def init(loading_screen):
	global _do_once, _accum_time, _loading_screen
	
	_do_once = True
	_accum_time = 0
	_loading_screen = loading_screen
	
def get_tick():
	return Clock.schedule_interval(loop, 0)

def loop(dt):
	global _do_once, _accum_time, _loading_screen
	
	if _do_once:
		_do_once = False	
		return
			
	_accum_time += dt
	_loading_screen.label.text = "{0:0.2f}".format(_accum_time)
		
	if _accum_time > 1:
		_accum_time = 0
		
		pass

	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		