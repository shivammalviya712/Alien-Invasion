# Author - Shivam Malviya
# Date - 31st May 2019


class GameStats:

    def __init__(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()

        # Start alien invasion in an active state
        self.game_active = False

        self.highscore = 0

    def reset_stats(self):

        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1