import os

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, sett, screen):
        # Load the ship image and get its rect.
        super(Ship, self).__init__()
        self.screen = screen

        self.image = pygame.image.load(os.path.join('assets/', 'ship.bmp'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.sett = sett
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Start each new ship at the bottom center of the screen.

        self.y = self.screen_rect.bottom
        self.center_ship()
        self.ship_speed_factor = 1.5

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        self.y = self.screen_rect.bottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.sett.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.sett.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.sett.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.sett.ship_speed_factor

        # Update rect object center value.
        self.rect.centery = self.y
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at the current position."""
        self.screen.blit(self.image, self.rect)
