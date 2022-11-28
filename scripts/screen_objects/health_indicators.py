
from scripts.bases.multi_rect_bases.health_indicator import HealthIndicator


class DefautlHealthIndicator(HealthIndicator):
	def __init__(self, game, hide=True):
		super().__init__(game=game, hide=hide)