"""Scoring system to track the game's score in real time."""
import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    #Scoreboard writes text to the screen, import 'pygame.font' module.
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
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
        """Draw score to the screen."""
        # Draw the current score at the top right of the screen:
        self.screen.blit(self.score_image, self.score_rect)

        # Draw the current high score at the top center of the screen:
        self.screen.blit(self.high_score_image, self.high_score_rect)

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