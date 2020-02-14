# Author - Shivam Malviya
# Date - 24th May 2019


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Initialise static game settings
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.screen_colour = (245, 230, 230)

        # Ship setting
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (0, 0, 0)
        self.bullets_allowed = 8

        # Aliens settings
        self.fleet_drop_speed = 10

        # Increment in speed with each level
        self.speedup_scale = 1.1

        # Rate of increase of alien points
        self.score_scale = 1.5

        # Initialise dynamic settings
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.aliens_speed_factor = 1

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.aliens_speed_factor *= self.speedup_scale

        # Increase points for each alien shot down after each level
        self.alien_points = int(self.alien_points * self.score_scale)