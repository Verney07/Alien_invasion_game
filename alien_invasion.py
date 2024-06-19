"""Main program to 'Alien Invasion' game."""
import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # Initialize the background:
        pygame.init()

        # Define 'clock' for controlling the frame rate:
        self.clock = pygame.time.Clock()

        # Make an instance-attribue of 'Settings' class (settings module):
        self.settings = Settings()

        # Define window size and background color with instance-attribute:
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # Make an instance-attribute of 'Ship' class.
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        # Control the game

        while True:
            # Helper method:
            self._check_events()
            self._update_screen()
            # Create an instance of class Clock:
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # event
                # exit the game:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pass through the loop:
        # (Using the instance-attribute)
        self.screen.fill(self.settings.bg_color)

        # Draw the ship on bottom of the background:
        self.ship.blitme()

        # Make the most recently drawn screen vsible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
