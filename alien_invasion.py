# Author - Shivam Malviya
# Date - 24th May 2019


import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from play_button import PlayButton
from scoreboard import Scoreboard


def run_game():

    # Initialise game, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make play button
    play_button = PlayButton(screen, "PLAY")

    # Make a ship
    ship = Ship(screen, ai_settings)

    # Creating fleet of aliens
    aliens = Group()
    gf.create_fleet(aliens, ai_settings, screen, ship)

    # Make a group of bullets
    bullets = Group()

    # Creating GameStats
    game_stats = GameStats(ai_settings)

    # Creating Score Board Instance
    scoreboard = Scoreboard(screen, game_stats, ai_settings)

    # Start the main loop for the game
    while True:

        gf.check_events(ship, screen, ai_settings, bullets, game_stats, play_button, aliens, scoreboard)
        if game_stats.game_active:

            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, game_stats, scoreboard)
            gf.update_aliens(aliens, ai_settings, ship, bullets, screen, game_stats, scoreboard)

        gf.update_screen(screen, ship, ai_settings, bullets, aliens, play_button, game_stats, scoreboard)


run_game()
