import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def update_aliens(sett, stats, sb, screen, ship, aliens, bullets):
    """Check edges and Update the positions."""
    check_fleet_edges(sett, aliens)
    aliens.update()
    check_aliens_bottom(sett, stats, sb, screen, ship, aliens, bullets)
    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(sett, stats, sb, screen, ship, aliens, bullets)


def update_bullets(sett, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    # Get rid of bullets over screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collisions(sett, screen, stats, sb, ship, aliens, bullets)


def check_bullet_collisions(sett, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet alien collision."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += sett.alien_points * len(aliens)
            sb.prep_score()
        check_highscore(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        sett.increase_speed()

        # Increase Level.
        stats.level += 1
        sb.prep_level()

        create_fleet(sett, screen, ship, aliens)


def ship_hit(sett, stats, sb, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens,bullets.
        reset_game(sett, screen, ship, aliens, bullets)
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(sett, stats, sb, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(sett, stats, sb, screen, ship, aliens, bullets)
            break


def fire_bullet(sett, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < sett.bullets_allowed:
        new_bullet = Bullet(sett, screen, ship)
        bullets.add(new_bullet)


def check_fleet_edges(sett, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(sett, aliens)
            break


def change_fleet_direction(sett, aliens):
    for alien in aliens.sprites():
        alien.rect.y += sett.alien_drop_factor
    sett.fleet_direction *= -1


def get_no_aliens(sett, alien_width):
    """Determine the number of aliens that fit in a row.
     Spacing between each alien is equal to half alien width"""

    available_space_x = sett.screen_width - 1.5 * alien_width
    no_of_aliens = int(available_space_x / (1.5 * alien_width))
    return no_of_aliens


def create_alien(sett, screen, aliens, alien_number, row_no):
    """Create an alien, and place it in row."""
    alien = Alien(sett, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.5 * alien_width * alien_number
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.rect.y = alien_height + 1.5 * alien_height * row_no
    aliens.add(alien)


def create_fleet(sett, screen, ship, aliens):
    """Create a full fleet/row of aliens."""
    alien = Alien(sett, screen)
    no_aliens = get_no_aliens(sett, alien.rect.width)
    no_rows = get_no_rows(sett, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.

    for row in range(no_rows):
        for alien_number in range(no_aliens):
            create_alien(sett, screen, aliens, alien_number, row)


def get_no_rows(sett, ship_height, alien_height):
    """Get how many rows that fit on the screen."""
    available_space_y = (sett.screen_height - (2 * alien_height) - ship_height)
    no_rows = int(available_space_y / (1.5 * alien_height))
    return no_rows


def reset_game(sett, screen, ship, aliens, bullets):
    """Empty aliens and bullets, create new fleet and center ship."""
    # Empty the list of aliens and Bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship.
    create_fleet(sett, screen, ship, aliens)
    ship.center_ship()


"""Event Listeners"""


def check_b_play(sett, screen, stats, sb, b_play, ship, aliens, bullets,
                 mouse_x, mouse_y):
    """Start New Game when the player clicks play."""
    button_clicked = b_play.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # Reset dynamic settings.
        sett.initialize_dynamic_sett()

        # Hide mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game stats.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_highscore()
        sb.prep_level()
        sb.prep_ships()

        # Reset Game.
        reset_game(sett, screen, ship, aliens, bullets)


def check_highscore(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.highscore:
        stats.highscore = stats.score
        sb.prep_highscore()


def check_keydown_events(event, sett, screen, ship, bullets):
    """Keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.

        new_bullet = Bullet(sett, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """KeyUp Event """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(sett, screen, stats, sb, b_play, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sett, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_b_play(sett, screen, stats, sb, b_play, ship, aliens,
                         bullets, mouse_x, mouse_y)


def update_screen(sett, screen, stats, sb, ship, aliens, bullets, b_play):
    """Update images on the screen and flip to the new screen.
    Redraw the screen during each pass through the loop."""

    screen.fill(sett.bg_color)
    # Redraw all bullets behind ship and aliens.

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the score info.
    sb.show_score()
    # Draw Play button if game not active and display high score to
    # beat.
    if not stats.game_active:
        b_play.draw_button()
        sb.show_score()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
