# Author - Shivam Malviya
# Date - 24th May 2019


import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ship, screen, ai_settings, bullets, stats, play_button, aliens, scoreboard):
    """Take cares of keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, ai_settings, bullets, aliens, stats, scoreboard)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, ai_settings, screen, ship, bullets, scoreboard)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship, screen, ai_settings, bullets, aliens, stats, scoreboard):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)

    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_p:
        start_game(aliens, bullets, ai_settings, ship, stats, screen, scoreboard)


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, ai_settings, screen, ship, bullets, scoreboard):

    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active :

        start_game(aliens, bullets, ai_settings, ship, stats, screen, scoreboard)


def start_game(aliens, bullets, ai_settings, ship, stats, screen, scoreboard ):

    ai_settings.initialise_dynamic_settings()
    # Hide cursor
    pygame.mouse.set_visible(False)

    stats.reset_stats()
    stats.game_active = True
    scoreboard.prep_level()
    scoreboard.prep_highscore()
    scoreboard.prep_score()
    scoreboard.prep_ships()

    aliens.empty()
    bullets.empty()

    create_fleet(aliens, ai_settings, screen, ship)
    ship.center_ship()


def update_screen(screen, ship, ai_settings, bullets, aliens, play_button, stats, scoreboard):
    # Add colour and ship to the screen
    screen.fill(ai_settings.screen_colour)

    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Draw aliens on the screen
    for alien in aliens.sprites():
        alien.blitme()

    # Drawing Scoreboard
    scoreboard.display_score()

    # Draw play button when game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, scoreboard):

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for collisions and takes appropriate actions
    check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, scoreboard)


def fire_bullet(bullets, ai_settings, screen, ship):

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)


def create_fleet(aliens, ai_settings, screen, ship):

    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship, alien)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_aliens(screen, ai_settings, alien_width, aliens, alien_number, row_number)


def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_aliens(screen, ai_settings, alien_width, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = 2 * alien.rect.height * row_number + alien.rect.height + 40
    aliens.add(alien)


def get_number_rows(ai_settings, ship, alien):

    available_space = ai_settings.screen_height - 3 * alien.rect.height - ship.rect.height
    number_rows = available_space//(2 * alien.rect.height)
    return number_rows


def update_aliens(aliens, ai_settings, ship, bullets, screen, stats, scoreboard):

    check_fleet_edges(aliens, ai_settings)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, aliens, bullets, ship, stats, screen, scoreboard)

    check_aliens_bottom(aliens, ship, ai_settings, bullets, stats, screen, scoreboard)


def check_fleet_edges(aliens, ai_settings):

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, scoreboard):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    for aliens in collisions.values():
        stats.score += ai_settings.alien_points * len(aliens)
    scoreboard.prep_score()
    check_highscore(stats, scoreboard)

    # Create new fleet
    if len(aliens) == 0:

        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(aliens, ai_settings, screen, ship)
        stats.level += 1
        scoreboard.prep_level()


def ship_hit(ai_settings, aliens, bullets, ship, stats, screen, scoreboard):

    if stats.ship_left > 0:

        stats.ship_left -= 1
        scoreboard.prep_ships()

        aliens.empty()
        bullets.empty()

        ship.center_ship()
        create_fleet(aliens, ai_settings, screen, ship)

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(aliens, ship, ai_settings, bullets, stats, screen, scoreboard):

    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.screen_rect.bottom:
            ship_hit(ai_settings,aliens, bullets, ship, stats, screen, scoreboard)
            break


def check_highscore(stats, scoreboard):

    if stats.score > stats.highscore:
        stats.highscore = stats.score

    scoreboard.prep_highscore()