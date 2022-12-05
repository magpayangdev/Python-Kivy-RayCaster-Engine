
from scripts.bases.base_audio import BaseAudio


_D_ATK,_D_HIT,_D_NPC_ATK,_D_NPC_HIT,_D_N,_D_B,_D_PS,_D_THEME= 'player_atk.wav','player_hit.wav','npc_atk.wav','npc_hit.wav','notification.wav','beep.wav','pause_start.wav','theme.mp3'


class DefaultAudio(BaseAudio):
	def __init__(self, game, player_atk=_D_ATK, player_hit=_D_HIT, npc_atk=_D_NPC_ATK, npc_hit=_D_NPC_HIT, notification=_D_N, beep=_D_B, pause_start=_D_PS, theme=_D_THEME, **kwargs):
		super().__init__(game=game, player_atk=player_atk, player_hit=player_hit, npc_atk=npc_atk, npc_hit=npc_hit, notification=notification, beep=beep, pause_start=pause_start, theme=theme)
		
	def re_init(self, player_atk=_D_ATK, player_hit=_D_HIT, npc_atk=_D_NPC_ATK, npc_hit=_D_NPC_HIT, notification=_D_N, beep=_D_B, pause_start=_D_PS, theme=_D_THEME, **kwargs):
		super().re_init(player_atk=player_atk, player_hit=player_hit, npc_atk=npc_atk, npc_hit=npc_hit, notification=notification, beep=beep, pause_start=pause_start, theme=theme)
