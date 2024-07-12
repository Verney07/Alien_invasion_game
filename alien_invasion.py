"""Main program to 'Alien Invasion' game"""
import sys
#We can pause the game for a moment when the ship is hit.
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize the background:
        pygame.init()
        # Define 'clock' for controlling the frame rate:
        self.clock = pygame.time.Clock()
        # Make an instance-attribue of 'Settings' class (settings module):
        self.settings = Settings()
        
        #---------------------------------------------------------------
        # Define window size and background color with instance-attribute:
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # # FULLSCREEN mode:-------------------------------------------------
        # # Create the screen surface:
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # Update the settings after the creation of the screen:
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        #---------------------------------------------------------------

        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game statistics and create a 
        # scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Make an instance-attribute of 'Ship' class.
        self.ship = Ship(self)
         # Create the group that holds the bullets:
        self.bullets = pygame.sprite.Group()
        #Create the group that holds the aliens:
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Create an instance of 'Button' class (it doesn't draw the button)
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        # Control the game
        while True:
            # Helper method:
            self._check_events()

            if self.game_active:
                # Call the ship's update() method on each pass through the loop:
                self.ship.update()
                # Update the position of the bullets on each pass through:
                self._update_bullets()
                #Update the position of each alien:
                self._update_aliens()
           
            self._update_screen()
            # Create an instance of class Clock:
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #event
                # exit the game:
                sys.exit()
            
            # Pygame detects a KEYDOWN event:
            elif event.type == pygame.KEYDOWN: # press the key
                self._check_keydown_events(event)
           
            elif event.type == pygame.KEYUP:    # release the key
                self._check_keyup_events(event)

            # Pygame detects a 'MOUSEBUTTONDOWN' event when player clicks
            # anywhere on the screen.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Returns a tuple containing the mouse cursor's coordinates.
                mouse_pos = pygame.mouse.get_pos()
                # Send the 'x' and 'y' values to the method to verify if the player
                # clicks on the 'Play' botton:
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks 'Play'."""
        # Check whether the point of the mouse click overlaps the region 
        # defined by the 'Play' button's rect: collidepoint
        
        # Store the boolean's value 'True' or 'False'
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        # The game will restart onley if 'Play' is clicked and
        # the game_active is False.
        if button_clicked and not self.game_active:

            # Reset the game settings: return any changed settings to their
            # initial values each time the player starts a new game.
            self.settings.initialize_dynamic_settings()       

            # Reset the game statistics and gives the player three new ships.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)


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
        """Respond to key releases."""

        # Verify if the player releases the right arrow key:
        if event.key == pygame.K_RIGHT:
            # Change the flag 'moving_right' to False:
            self.ship.moving_right = False
       
       # Verify if the player releases the left arrow key:
        elif event.key == pygame.K_LEFT:
            # Change the flag 'moving_left' to False:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

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
        
        self._check_bullet_alien_collisions()
         
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #Remove any bullets and aliens that have collided.
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien. 
        collisions  = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #Check whether the aliens group is empty.
        if not self.aliens:
            #Destoy existing bullets.
            self.bullets.empty()
            #Fills the screen with aliens again
            self._create_fleet()

            #Increase the game's tempo when the last alien has been shot down:
            self.settings.increase_speed()
    
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        #Check if the fleet is at an edge, then update positions.
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #Call '_ship_hit()' method when an alien hits the ship.
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ships_lef.
            self.stats.ships_left -= 1

            #Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            #Create new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            #Pauses program execution for half second.
            sleep(0.5)
        
        # Set 'game_active' to 'False' when the player has used up
        # all their ships:
        else:
            self.game_active = False

            # Set the mouse cursor visible once the game ends.
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        #Grab the alien's width and heigh using the 'size' attribute.
        alien_width, alien_height = alien.rect.size

        #Set the initial 'x' and 'y' values for the placement of the first
        #alient in the fleet.
        current_x, current_y = alien_width, alien_height

        #While loop that controls how many rows are placed onto the screen.
        while current_y < (self.settings.screen_height - 3 * alien_height):
            
            #Keep adding aliens 'while' there's enough room to place one.
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # As long as there's at least two aliens width's worth of
                # space at the right edge of the screen, enter the loop and add
                # another alien to the fleet
                
                #Call the helper '_create_alien' method and pass it the 'y' value
                # and 'x' position.
                self._create_alien(current_x, current_y)

                #Increment the value in two alien widths to the horizontal
                #position to move past the alien just added.
                current_x += 2 * alien_width

            #Finished a row; rest 'x' value and increment 'y' value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""

        #Create an alien in the correct position whenever there's enough 
        # horizontal and vertical space 
        new_alien = Alien(self)
        #Set the precise horizontal position on the current value        
        new_alien.x = x_position
        #Position the alien's rect at this same x-value.
        new_alien.rect.x = x_position
        #Position the alien's rect at this same y-value.
        new_alien.rect.y = y_position

        #Add the new alien to the group.
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""

        #Loop through the fleet and call 'check_edges()' on each alien
        for alien in self.aliens.sprites():
            # When 'if' block returns 'True' we know an alilen is at an edge
            # and the whole fleet needs to change direction.
            if alien.check_edges():
                self._change_fleet_direction()
                # Break out of the loop
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""

        # Loop through all the aliens and drop each one using the setting
        # 'fleet_drop_speed'
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of te screen."""
        for alien in self.aliens.sprites():
            # Alien reaches the bottom when its 'rect.bottom' value is 
            # greather than or equal to the screen's height. 
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same as if the ship got hit.
                # If one alien hits the bottom, there's no need check the rest.
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
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

        # Draw the score information: draw before 'Play' button.
        self.sb.show_score()

        # Make the button visible to draw it after the other elements
        # have been drawn. The button appears when the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        
        # Make the most recently drawn screen vsible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()