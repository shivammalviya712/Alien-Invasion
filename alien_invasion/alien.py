# Author - Shivam Malviya
# Date - 26th May 2019


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, ai_settings):

        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images\\UFO.bmp")
        self.ai_settings = ai_settings

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.aliens_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):

        screen_rect = self.screen_rect
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True




