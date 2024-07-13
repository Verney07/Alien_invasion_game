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
        self.screen.blit(self.score_image, self.score_rect)

