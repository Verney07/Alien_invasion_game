"""Main program to 'Alien Invasion' game."""
import sys

import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # ---------------------------------------------------------------------
        # Define window size and background color with instance-attribute:
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        # # FULLSCREEN mode:-------------------------------------------------
        # # Create the screen surface:
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # Update the settings after the creation of the screen:
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # ---------------------------------------------------------------------
        pygame.display.set_caption("Alien Invasion")

        # Make an instance-attribute of 'Ship' class.
        self.ship = Ship(self)

        # Create the group that holds the bullets:
        self.bullets = pygame.sprite.Group()

        #Create the group that holds the aliens:
        self.aliens=pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        # Control the game

        while True:
            # Helper method:
            self._check_events()
            # Call the ship's update() method on each pass through the loop:
            self.ship.update()
            # Update the position of the bullets on each pass through:
            self._update_bullets()

            self._update_screen()
            # Create an instance of class Clock:
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # event
                # exit the game:
                sys.exit()

            # Pygame detects a KEYDOWN event:
            elif event.type == pygame.KEYDOWN:  # press the key
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:  # release the key
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # Verify if the player presses the right arrow key:
        if event.key == pygame.K_RIGHT:
            # Change the flag 'moving_right' to True:
            self.ship.moving_right = True

        # Verify if the player presses the left arrow key:
        elif event.key == pygame.K_LEFT:
            # Change the flag 'moving_left' to True:
            self.ship.moving_left = True

        # Pressing Q to quit the game:
        elif event.key == pygame.K_q:
            sys.exit()

        # Call _fire_bullet() when spacebar is pressed.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to releases."""

        # Verify if the player releases the right arrow key:
        if event.key == pygame.K_RIGHT:
            # Change the flag 'moving_right' to False:
            self.ship.moving_right = False

        # Verify if the player releases the left arrow key:
        elif event.key == pygame.K_LEFT:
            # Change the flag 'moving_left' to False:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""

        # Limit group o 3 fired bullets. News bullet will appear, when the old
        # pass through the screen's top.
        if len(self.bullets) < self.settings.bullets_allowed:
            # Make the 'new_bullet' instance of 'Bullet' class:
            new_bullet = Bullet(self)

            # Ad to the group 'bullets' using the add() method:
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update the position of the bullets on each pass through:
        self.bullets.update()

        # Get rid of bullets that have disappeared:-----------
        # Use the copy() method to set up the for loop:
        for bullet in self.bullets.copy():
            # Verify if the bullet it has disappeared off the screen's top:
            if bullet.rect.bottom <= 0:
                # Remove the bullet.
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Make an alien.
        alien=Alien(self)
        self.aliens.add(alien)
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen during each pass through the loop:
        # (Using the instance-attribute)
        self.screen.fill(self.settings.bg_color)

        # Draw all fired bullets to the screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the ship on bottom of the background:
        self.ship.blitme()

        #Draw the alien on upper-left area of the screen:
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen vsible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
