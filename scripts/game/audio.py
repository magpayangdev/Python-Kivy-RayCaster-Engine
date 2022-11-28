
from scripts.modules.loaders import audio_loader as al

class Audio:
	def __init__(self, game, player_atk='player_atk.wav', player_hit='player_hit.wav', npc_atk='npc_atk.wav', npc_hit='npc_hit.wav', notification='notification.wav', beep='beep.wav', pause_start='pause_start.wav', theme='theme.mp3'):
		self.game = game
		self.game.audio = self
		
		self.player_atk = al._audio_container.get(player_atk)
		self.player_atk.volume = 0.5
		self.player_hit = al._audio_container.get(player_hit)
		self.player_hit.volume = 0.5
		self.npc_atk = al._audio_container.get(npc_atk)
		self.npc_atk.volume = 0.1
		self.npc_hit = al._audio_container.get(npc_hit)
		self.npc_hit.volume = 0.4
		self.notification = al._audio_container.get(notification)
		self.notification.volume = 1.0
		self.beep = al._audio_container.get(beep)
		self.beep.volume = 1.0
		self.pause_start = al._audio_container.get(pause_start)
		self.pause_start.volume = 1.0
		self.theme = al._audio_container.get(theme)
		self.theme.volume = 0.1

	def re_init(self):
		pass
	
	def update(self, dt):
		pass

	def hit(self, id='npc'):
		if id == 'player':
			self.player_hit.play()
			
		elif id == 'npc':
			self.npc_hit.play()
		
	def attack(self, id='npc'):
		if id == 'player':
			self.player_atk.play()
			
		elif id == 'npc':
			self.npc_atk.play()
			
	def notify(self, id='notification'):
		if id == 'notification':
			self.notification.play()
		elif id == 'beep':
			self.beep.play()
			
	def pause_game(self):
		self.pause_start.play()
		
	def play_theme(self):
		self.theme.play()
		
	def stop_theme(self):
		self.theme.stop()