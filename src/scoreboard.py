import pygame.font
from pygame.sprite import Group

from src.ship import Ship


class ScoreBoard(object):
    """A class to report your score"""

    def __init__(self, sett, screen, stats):
        """Initialize score-keeping attributes"""
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.sett = sett

        # Font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.sett.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score onto the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_highscore(self):
        """Turn the highscore into a rendered image"""
        high_score = int(round(self.stats.highscore, -1))
        highscore_str = "{:,}".format(high_score)

        self.highscore_image = self.font.render(highscore_str, True,
                                                self.text_color,
                                                self.sett.bg_color)

        # Center highscore at the top of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top + 10

    def prep_level(self):
        """Turn the level into rendered image"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color,
                                            self.sett.bg_color)

        # Positon the level a top left
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = self.screen_rect.top + 10

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_no in range(self.stats.ships_left):
            ship = Ship(self.sett, self.screen)
            ship.rect.x = 10 + ship_no * ship.rect.width
            ship.rect.y = self.screen_rect.bottom - 10
            self.ships.add(ship)
