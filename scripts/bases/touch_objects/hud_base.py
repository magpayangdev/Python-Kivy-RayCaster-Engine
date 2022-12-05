
from scripts.screen_objects.health_indicators import DefaultHealthIndicator as HealthIndicator
from scripts.bases.touch_objects.quadrant_touch_object import QuadrantTouchObject
from scripts.screen_objects.controllers import LeftController, RightController
from scripts.screen_objects.player_sprites import DefaultPlayerSprite
from scripts.bases.window_objects.button_base import ButtonBase
from scripts.bases.window_objects.text_base import TextBase
from scripts.screen_objects.hit_rect import HitRect
from scripts.modules.textures import *
from settings import *
import math


class HudBase(QuadrantTouchObject):
	def __init__(self, game, window):
		super().__init__(game=game, window=window)
		
		self.reset_hit_rect=False
		
		self.button_size = 250, 100
		f = lambda x,y: (self.window.width - x / 2, self.window.height - y / 2)
		
		self.eb_kwargs = {'game':self.game, 'window':self.window, 'callback':self.exit_game, 'text':'EXIT', 'bg_color':(1,1,1,1), 'font_name':'AdventureRequest', 'font_size':75, 'text_color':(1,1,1,1), 'size':self.button_size, 'pos':f(*self.button_size), 'hide':True}
	
		self.debug_label_kwargs = {'game':self.game, 'window':self.window, 'text':'Label Text', 'font_name':'AdventureRequest', 'halign':'center', 'valign':'top', 'font_size':75,  'text_color':(1,0,0,1), 'text_size':self.window.size, 'padding_x':0, 'padding_y':0, 'hide':True}
		
		self.left_xypad_active = False
		self.right_xypad_active = False

		self.player_sprite = DefaultPlayerSprite(self.game)
		self.left_controller = LeftController(self.game)
		self.right_controller = RightController(self.game)
		self.player_health = HealthIndicator(self.game)
		self.hud_text = TextBase(**self.debug_label_kwargs)		
		self.exit_button = ButtonBase(**self.eb_kwargs)	
		self.hit_rect = HitRect(self.game)
		
		
	@property
	def text(self):
		self.hud_text.text
		
	@text.setter
	def text(self, value):
		self.hud_text.text = value
		
	#<----Window Functions
	def re_size(self):
		pass
		
	def show(self):
		self.player_sprite.show()
		self.left_controller.show()
		self.right_controller.show()
		self.player_health.show()
		self.exit_button.show()
		self.hud_text.show()		
		self.hit_rect.show()
		
	def hide(self):
		self.player_sprite.hide()
		self.left_controller.hide()
		self.right_controller.hide()
		self.player_health.hide()
		self.hud_text.hide()
		self.exit_button.hide()
		self.hit_rect.hide()
	
	def remove(self):
		self.hide()
		
		self.player_sprite.remove()
		self.left_controller.remove()
		self.right_controller.remove()
		self.player_health.remove()
		self.exit_button.remove()
		self.hud_text.remove()
		self.hit_rect.remove()
		
		del(self.player_sprite)
		del(self.left_controller)
		del(self.right_controller)
		del(self.player_health)
		del(self.hud_text)		
		del(self.exit_button)
		del(self.hit_rect)	
		
	#<----Base Functions: re_init, update		
	def re_init(self):
		super().re_init()
		
		self.player_sprite.re_init()
		self.left_controller.re_init()
		self.right_controller.re_init()
		self.player_health.re_init()
		self.hud_text.re_init(**self.debug_label_kwargs)		
		self.exit_button.re_init(**self.eb_kwargs)
		self.hit_rect.re_init()
						
	def update(self, dt):
		pass
	
	#<----Hud Functions
	def exit_game(self, *args):
		self.game.event.exit_game()
		
	def reset_hud(self):
		self.hit_rect.color = 1,1,1,0
		
	def game_over(self):
		self.hit_rect.color = 1,1,1,1
		self.hit_rect.texture = get_menu_texture('game_over.png')
		
	def victory(self):
		self.hit_rect.color = 1,1,1,1
		self.hit_rect.texture = get_menu_texture('victory.png')

	def player_is_hit(self):			
		self.accum_time = 0.0
		self.reset_hit_rect = True
		self.hit_rect.color = 1,0,0,0.5 
		self.player_health.flip(self.game.player.health)

	#<----TouchFunctions: on_touch_down, on_touch_move, on_touch_up
	def on_touch_down(self, touch):
		super().on_touch_down(touch)
		
		if self.exit_button.does_collide(touch):
			self.exit_button.state = 'down'
	
	def on_touch_move(self, touch):
		super().on_touch_move(touch)
		
	def on_touch_up(self, touch):
		super().on_touch_up(touch)
			
	#<---- Touch Down Funcs
	def touch_down_q1(self, touch):
		super().touch_down_q1(touch)
		
		if math.dist(touch.pos, controller_center_left()) < 250:		
			self.left_xypad_active = True	
			self.left_controller.start_counting()
		else:
			self.left_xypad_active = False

	def touch_down_q2(self, touch):
		super().touch_down_q1(touch)
		
	def touch_down_q3(self, touch):
		super().touch_down_q3(touch)	
		
		if math.dist(touch.pos, controller_center_right()) < 250:
			self.right_xypad_active = True
			self.right_controller.start_counting()
		else:
			self.right_xypad_active = False
		
	def touch_down_q4(self, touch):
		super().touch_down_q4(touch)
		
	#<---- Touch Move Funcs
	def touch_move_q1(self, touch):
		super().touch_move_q1(touch)
		
		if self.left_xypad_active:		
			self.left_controller.move_stick(*touch.pos)
			self.game.player.right_dir = max(-1, min(1, (touch.x - controller_center_left()[0]) / 250))
			self.game.player.forward_dir = max(-1, min(1, (touch.y - controller_center_left()[1]) / 250))	
			self.left_controller.stop_counting()
		else:
			self.left_controller.reset_stick()
			self.game.player.forward_dir = 0
			self.game.player.right_dir = 0
		
	def touch_move_q2(self, touch):
		super().touch_move_q2(touch)
		
	def touch_move_q3(self, touch):
		super().touch_move_q3(touch)
		
		if self.right_xypad_active: #<----
			self.right_controller.move_stick(*touch.pos)
			self.game.player.yaw = max(-1, min(1, (touch.x - controller_center_right()[0]) / 250))
			self.right_controller.stop_counting()
		else:
			self.right_controller.reset_stick()
			self.game.player.yaw = 0
		
	def touch_move_q4(self, touch):
		super().touch_move_q4(touch)
		
	#<---- Touch Up Funcs
	def touch_up_q1(self, touch):
		super().touch_up_q1(touch)
		
		self.left_controller.reset_stick()
		self.game.player.forward_dir = 0
		self.game.player.right_dir = 0
		self.left_controller.flip()
		
	def touch_up_q2(self, touch):
		super().touch_up_q2(touch)
		
		self.left_controller.reset_stick()
		self.game.player.forward_dir = 0
		self.game.player.right_dir = 0
		
	def touch_up_q3(self, touch):
		super().touch_up_q3(touch)
		
		self.right_controller.reset_stick()
		self.game.player.yaw = 0
		self.right_controller.flip()
		
	def touch_up_q4(self, touch):
		super().touch_up_q4(touch)
		
		self.right_controller.reset_stick()
		self.game.player.yaw = 0
