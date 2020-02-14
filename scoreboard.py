# Author - Shivam Malviya
# Date - 1st June 2019


import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scoreboard():

    def __init__(self, screen, game_stats, ai_settings):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = game_stats
        self.ai_settings = ai_settings

        self.font = pygame.font.SysFont(None, 48)
        self.text_colour = (0, 0, 0)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.ai_settings.screen_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def prep_highscore(self):

        self.highscore_rounded = round(self.stats.highscore, -1)
        self.highscore_str = "{:,}".format(self.highscore_rounded)
        self.highscore_image = self.font.render(self.highscore_str, True, self.text_colour, self.ai_settings.screen_colour)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = 20

    def prep_level(self):

        self.level_str = str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True, self.text_colour, self.ai_settings.screen_colour)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):

        self.ships = Group()
        for ship_no in range(self.stats.ship_left):

            ship = Ship(self.screen, self.ai_settings)
            ship.rect.y = 10
            ship.rect.x = 10 + ship_no * (ship.rect.width + 10)
            self.ships.add(ship)

    def display_score(self):

        # Displaying scores, level and ships left
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
