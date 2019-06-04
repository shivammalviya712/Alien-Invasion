# Author - Shivam Malviya
# Date - 25th May 2019


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, screen, ai_settings, ship):

        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = self.rect.top

        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):

        self.y -= self.speed_factor
        self.rect.top = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
