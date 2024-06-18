"""Main program to 'Alien Invasion' game."""
import sys

import pygame

from settings import Settings


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

        # Set the background color: mix of red, green and blue.
        # (red, green, blue)
        self.bg_color = (230, 230, 230)  # ligth gray color

    def run_game(self):
        """Start the main loop for the game."""
        # Control the game

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event
                    # exit the game:
                    sys.exit()

            # Redraw the screen during each pass through the loop:
            # (Using the instance-attribute)
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen vsible.
            pygame.display.flip()

            # Create an instance of class Clock:
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
