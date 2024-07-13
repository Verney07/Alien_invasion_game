"""Scoring system to track the game's score in real time."""
import pygame.font
# Make a group of ships:
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""
    
    #Scoreboard writes text to the screen, import 'pygame.font' module.
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        # Assign the game instance to an attribute. Need it to create
        # some ships.
        self.ai_game = ai_game
        # Set the 'ai_game' parameters will report the value's tracking.
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information:
        self.text_color = (30, 30, 30)
        # Instantiate a font object:
        self.font = pygame.font.SysFont(None, 48)
        #Prepare the initial score image: turn the text into an image:
        self.prep_score()
        #Display the high score with a separate method:
        self.prep_high_score()
        # Display the current level to call 'self.prep_level()'.
        self.prep_level()
        # Display the current ships left to call 'self.prep_ships()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Format the score as multiples of 10 and include comma separators.
        rounded_score = round(self.stats.score, -1)
        # Turn the numerical value 'rounded_score' into a string.
        score_str = f"{rounded_score:,}"
        # Pass the string to 'render()' and then creates the image.
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the upper-right corner of the screen.
        # .score_rect: allows always line up with the screen's rigth side.
        self.score_rect = self.score_image.get_rect()
        # Set right edge 20 pixels down form the screen's top.
        self.score_rect.right = self.screen_rect.right - 20
        # Place the top edge 20 pixels down from the screen's top.
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        # Draw the current score at the top right of the screen:
        self.screen.blit(self.score_image, self.score_rect)
        # Draw the current high score at the top center of the screen:
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Draw the level image to the screen.
        self.screen.blit(self.level_image, self.level_rect)
        # Draw the ships image group to the screen:
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # Round the high score to the nearest 10 and format it with commas.
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        # Generate an image from the high score.
        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color,
            self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()

        # Center the high score 'rect' horizontally.
        self.high_score_rect.centerx = self.screen_rect.centerx

        # Set the high score's 'top' attribute to match the 'top' of the
        # score image.
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        # Check the current score against the high score.
        if self.stats.score > self.stats.high_score:
            # Update the value of 'high_score'. 
            self.stats.high_score = self.stats.score
            # Call 'prep_high_score()' to update the high score's image.
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        # 'game_stats.py' module, 'self.level' attribute = 1. 
        level_str = str(self.stats.level)
        
        # Create an image from the value stored in 'stats.level'.
        self.level_image = self.font.render(
            level_str,
            True,
            self.text_color, 
            self.settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        # Set the image's 'rect' attribute to match the score's 'right' attribute.
        self.level_rect.right = self.score_rect.right
        # Set the 'top' attribute 10 pixels beneath the bottom of the score
        # image.
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show hor many ships are left."""
        # Create an empty group 'self.ships' to hold the ship instances.
        self.ships = Group()
        # Fill this group: a loop runs once for every ship the player has left.
        for ship_number in range(self.stats.ships_left):
            # Create a new ship.
            ship = Ship(self.ai_game)
            # Set each ship's 'x'-coordinate value so the ships appear next
            # to each other with a 10-pixels margin on the left side.
            ship.rect.x = 10 + ship_number * ship.rect.width
            # Set the 'y'-coordinate value 10-pixels down from the top of
            # the screen. Ships appear in the upper-left corner.
            ship.rect.y = 10
            # Add new ship to the group ships.
            self.ships.add(ship)

