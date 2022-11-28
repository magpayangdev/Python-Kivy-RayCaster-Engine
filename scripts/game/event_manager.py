""" event manager - defines what happens when an event is called, sometimes depending on the game mode"""

from kivy.clock import Clock
from settings import *


class EventManager:
	def __init__(self, game):
		self.game = game	
		self.game.event = self 
		
	def re_init(self):
		pass
		
	def update(self, dt):
		pass
		
	def invalid_func(self):
		9/0
		
	#<----- Pre Primary Loop Events
	def score_card_finished(self):
		self.game.secondary_loop._accum_time = 18
		
		#<----Menu
	def show_intro(self):
		self.game.tc_mngr.show_intro_card()
	
	def skip(self):	
		self.game.tc_mngr.remove_current_card()
		self.game.audio.theme.stop()
		self.game.audio.theme.play()
		self.game.sky.show()
		self.game.floor.show()
		self.game.world.show()
		self.game.sprite_space.reload_sprites()
		self.game.sprite_space.show()
		self.game.hud.show()
		
		Clock.unschedule(self.game.tick)		
		self.game.tick = Clock.schedule_interval(self.game.primary_loop.update, 0)
		self.game.loop_num = 1
		
	def proceed(self):	
		self.skip()
		
	#<---- Primary Loop Events
	def start_loading(self):
		lsa.re_init(self)
		lsa.create_loading_screen(self.game)
		self.game.tick = Clock.schedule_interval(lsa.update, 0)

	def finished_loading(self):
		self.game.has_finished_loading = True
		Clock.unschedule(self.game.tick)
		self.game.tick = Clock.schedule_interval(self.game.pre_primary_loop.update, 0)
		self.game.loop_num = 0
		
		self.game.l_screen.remove()
	
		self.game.tc_mngr.show_menu_card()	
		self.game.audio.play_theme()

	def pauseself(self):
		self.game.paused = True
		self.game.hud.debug_text = 'Paused!'
		self.game.hud.debug_label.color = RED
		self.game.audio.pauseself()
		self.game.audio.stop_theme()
				
	def unpauseself(self):
		self.game.paused = False
		self.game.hud.debug_label.color = GREEN
		self.game.audio.play_theme()
		
	def exit_game(self):
		self.game.window.quit_game()
		
	#<---- Secondary Loop Events
	def level_clean_up(self):
		self.game.sprite_space.remove_all_sprites()
		
	def show_score(self):
		self.game.audio.theme.stop()
		self.game.hud.reset_hud()
		self.game.tc_mngr.show_score_card()	
		
	def next_level(self):
		self.game.secondary_loop._accum_time = 0
		self.game.tc_mngr.remove_current_card()
		self.game.player.re_init()
		
		Clock.unschedule(self.game.tick)
		self.game.tick = Clock.schedule_interval(self.game.primary_loop.update, 0)
		self.game.loop_num = 1

		self.game.audio.theme.play()
		self.game.sprite_space.reload_sprites()
		#self.game.sprite_space.show()

		
	#<---- Player Events
	def player_attack(self):
		self.game.sprite_space.player_attack()
		self.game.audio.attack('player')
		
	def player_hit(self, damage_amount=7):
		self.game.player.hit(damage_amount)
		if PLAYER_CAN_DIE and self.game.player.health == 0:
			self.player_has_died()
		else:
			self.game.hud.player_is_hit()

	def player_has_died(self):
		self.game.audio.theme.stop()
		self.game.hud.game_over()
		loop.start_secondary_loop()
		
	def player_health_updated(self):
		self.game.hud.player_health.flip(self.game.player.health)
		
	#<---- Sprite Events
	def sprite_attack(self, sprt):
		self.game.audio.attack('npc')
		self.player_hit(sprt.influence_amount)
	
	def sprite_hit(self, damage_amount=1):
		self.game.audio.hit()
		
	def sprite_has_died(self, sprt):
		self.game.player.add_to_kill_list(sprt.init_img_seq_id)

		if self.game.sprite_space.remaining_sprites() == 0:
			self.game.hud.victory()
			
			Clock.unschedule(self.game.tick)
			self.game.tick = Clock.schedule_interval(self.game.secondary_loop.update, 0)
			self.game.loop_num = 2			
		
	def sprite_for_delete(self, sprt):
		self.game.sprite_space.remove_sprite(sprt)
	
	#<---- Touch Events
	def on_touch_down(self, touch):		
		if self.game.loop_num == -1:
			pass
	
		elif self.game.loop_num == 0:
			self.game.tc_mngr.on_touch_down(touch)
						
		elif self.game.loop_num == 1:					
			self.game.hud.on_touch_down(touch)
			
		elif self.game.loop_num == 2:
			self.game.hud.on_touch_down(touch)
		
						
	def on_touch_move(self, touch):		
		if self.game.loop_num == -1:
			pass
			
		elif self.game.loop_num == 0:
			pass
			
		elif self.game.loop_num == 1:			
			self.game.hud.on_touch_move(touch)
			
		elif self.game.loop_num == 2:
			self.game.hud.on_touch_move(touch)
		
							
	def on_touch_up(self, touch):	
		if self.game.loop_num == -1:
			pass
			
		elif self.game.loop_num == 0:
			self.game.tc_mngr.on_touch_up(touch)
			
		elif self.game.loop_num == 1:
			self.game.hud.on_touch_up(touch)
			
		elif self.game.loop_num == 2:
			self.game.hud.on_touch_up(touch)
		