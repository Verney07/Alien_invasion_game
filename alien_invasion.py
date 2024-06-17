"""Main program to 'Alien Invasion' game."""
import sys

import pygame


class AlienInvasion():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # Initialize the background:
        pygame.init()

        # window size:
        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        # Control the game

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event
                    # exit the game:
                    sys.exit()

            # Make the most recently drawn screen vsible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
