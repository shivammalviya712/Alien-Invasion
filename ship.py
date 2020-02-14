# Author - Shivam Malviya
# Date - 24th May 2019


import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):

        super().__init__()
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\\spaceship-y.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Decimal x co-ordinate
        self.center = self.rect.centerx

        # Flags for checking its motion
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"This updates ship's x co-ordinate."""

        # Updates the center's x co-ordinate but not rect's.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updates rect
        self.rect.centerx = self.center

    def center_ship(self):

        self.center = self.screen_rect.centerx
