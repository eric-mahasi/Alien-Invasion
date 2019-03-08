import os

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that will represent a single alien."""

    def __init__(self, sett, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.sett = sett

        # Load the alien image and set its rect attributes.
        self.image = pygame.image.load(os.path.join('assets/', 'alien.bmp'))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"Update aliens to move."""
        self.x += (self.sett.alien_speed_factor * self.sett.fleet_direction)
        self.rect.x = self.x
