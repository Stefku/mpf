"""Flasher config player."""
from mpf.core.config_player import ConfigPlayer


class FlasherPlayer(ConfigPlayer):

    """Triggers flashers based on config."""

    config_file_section = 'flasher_player'
    show_section = 'flashers'

    def play(self, settings, context, priority=0, **kwargs):
        """Flash flashers."""
        del kwargs

        if 'flashers' in settings:
            settings = settings['flashers']

        for flasher, s in settings.items():
            try:
                flasher.flash(**s)
            except AttributeError:
                self.machine.flashers[flasher].flash(**s)

    def get_express_config(self, value):
        """Parse express config."""
        return dict(ms=None)

player_cls = FlasherPlayer
