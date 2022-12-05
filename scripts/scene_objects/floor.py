
from scripts.bases.base_floor import BaseFloor

_HIDE = True


class DefaultFloor(BaseFloor):
	def __init__(self, game, floor_color='white', **kwargs):
		super().__init__(game=game, floor_color=floor_color, hide=_HIDE)
		
	def re_init(self, floor_color='white', **kwargs):
		super().re_init(floor_color=floor_color, hide=_HIDE)
