import plugin
from .screens.paint_screen import PaintScreen

class PaintPlugin(plugin.PluginObject):

	def get_main_screen():
		return PaintScreen()

	def get_screens():
		return [PaintScreen()]