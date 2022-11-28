
from settings import *
from scripts.game.audio import Audio
from scripts.game.player import Player
from scripts.scene_objects.sky import Sky
from scripts.scene_objects.floor import Floor
from scripts.game.graph_manager import GameGraph
from scripts.screen_objects.minimaps import DefaultMinimap


""" Sky """	
class UserSky(Sky):
	def __init__(self, game, sky_path, hide, **kwargs):
		super().__init__(game, image_name=str(sky_path), hide=hide)

""" Floor """		
class UserFloor(Floor):
	def __init__(self, game, hide, **kwargs):
		super().__init__(game, hide=hide)


""" Audio """
class UserAudio(Audio):
	def __init__(self, game, player_atk, player_hit, npc_atk, npc_hit, notification, beep, pause_start, theme, **kwargs):
		super().__init__(game, player_atk=str(player_atk), player_hit=str(player_hit), npc_atk=str(npc_atk), npc_hit=str(npc_hit), notification=str(notification), beep=str(beep), pause_start=str(pause_start), theme=str(theme))	


""" Map """		
class UserMap(DefaultMinimap):
	def __init__(self, game, hide=False):
		super().__init__(game,hide=hide)


""" Player """
class UserPlayer(Player):
	def __init__(self, game, player_pos_x, player_pos_y, player_angle, player_radius, player_health, player_regen, **kwargs):		
		super().__init__(game, pos_x=float(player_pos_x), pos_y=float(player_pos_y), angle=float(player_angle),  radius=float(player_radius), health=float(player_health), regen=float(player_regen))


""" Graph Manager """
class UserGraphManager(GameGraph):					
	def __init__(self, game, map_path, **kwargs):
		super().__init__(game, world_path=str(map_path))












	
	