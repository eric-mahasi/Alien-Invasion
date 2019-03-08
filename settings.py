class Settings(object):
    """A class for settings."""

    def __init__(self):
        # Screen Settings.
        self.screen_width = 1024
        self.screen_height = 684
        self.bg_color = (230, 230, 230)

        # Ship Settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien Settings.
        self.alien_drop_factor = 10
        self.fleet_direction = 1

        # Leveling up setting.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_sett()

    def initialize_dynamic_sett(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
