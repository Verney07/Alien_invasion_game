"""Module that manage the most behavior of the player's ship."""
import pygame


class Ship():
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""

        # Assign the screen to an attribute of Ship:
        self.screen = ai_game.screen

        # Access to 'rect' (rectangle) attribute of screen and assing to 'self.screen_rect'
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        # Access the ship surface's 'rect' attribute:
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start whit a ship that's not moving.
        self.moving_right = False

    def update(self):
        """Update the ship's position base on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
