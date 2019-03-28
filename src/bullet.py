import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to handle bullets."""

    def __init__(self, sett, screen, ship):
        """Create  a bullet object at the ships current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at(0,0) and then set correctly.
        self.rect = pygame.Rect(0, 0, sett.bullet_width, sett.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Space bar fire flag.

        # Store the bullet's as a decimal.
        self.y = float(self.rect.y)

        self.color = sett.bullet_color
        self.speed = sett.bullet_speed_factor

    def update(self):
        """Move the bullet up."""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)
