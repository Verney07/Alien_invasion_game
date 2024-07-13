"""Module that manage the most behavior of the player's ship."""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        # Call 'super()'.
        super().__init__()
        
        # Assign the screen to an attribute of Ship:
        self.screen = ai_game.screen

        # Access to 'rect' (rectangle) attribute of screen and assing to 'self.screen_rect'
        self.screen_rect = ai_game.screen.get_rect()

        # Create 'settings' attribute for ship:
        self.settings = ai_game.settings

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        # Access the ship surface's 'rect' attribute:
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        # (The rect only keep the integer portion of value.)
        self.x = float(self.rect.x)

        # Movement flag; start whit a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position base on the movement flag."""
        # Update the ship's x value, not the rect.
        # Check the position of the ship before changing the value of self.x.

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        #Reset the 'self.x' attribute, wich allows us to track the ship's
        # exact position.
        self.x = float(self.rect.x)
