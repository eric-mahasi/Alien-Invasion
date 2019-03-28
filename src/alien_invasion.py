import pygame
from pygame.sprite import Group

from src import game_functions as gf
from src.alien import Alien
from src.button import Button
from src.game_stats import GameStats
from src.scoreboard import ScoreBoard
from src.settings import Settings
from src.ship import Ship


def rungame():
    # Initialize game,settings and create screen object.
    pygame.init()
    sett = Settings()
    screen = pygame.display.set_mode((sett.screen_width, sett.screen_height))
    pygame.display.set_caption("Alien Invasion")

    """"Instance initialization"""
    # Make instance of game stats.
    stats = GameStats(sett)
    # Make instance of scoreboard.
    sb = ScoreBoard(sett, screen, stats)
    # Make the play button.
    b_play = Button(sett, screen, "PLAY")

    # Make instance of ship.
    ship = Ship(sett, screen)
    # Make a group to store bullets and aliens.
    aliens = Group()
    bullets = Group()
    # Make instance of alien.
    alien = Alien(sett, screen)
    gf.create_fleet(sett, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(sett, screen, stats, sb, b_play, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(sett, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(sett, stats, sb, screen, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop.
        gf.update_screen(sett, screen, stats, sb, ship, aliens, bullets,
                         b_play)


rungame()
