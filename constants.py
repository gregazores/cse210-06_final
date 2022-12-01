# constants regarding game play
#import some sort of file path converting library
from space_invaders.game.casting.color import Color #import the Color class from the color file which creates a color object to be used when drawing/displaying the game objects in the video service

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Invaders" #the name of the game for reference and display purposes
FRAME_RATE = 60 #the rate of screen refresh: how fast the game will go based on how often the screen is redrawn to show the movement/animation of the objects. This will determine how smooth the animation is and how responsive the game controls are

# SCREEN - the game window
SCREEN_WIDTH = 1040 #the decided width of the game window in pixels
SCREEN_HEIGHT = 680 #the chosen height of the game window in pixels
CENTER_X = SCREEN_WIDTH / 2 #the graphical half way point in the width, the x component of the center point of the game window
CENTER_Y = SCREEN_HEIGHT / 2 #the graphical half way point in the height, the y component of the center point of the game window

# FIELD 
FIELD_TOP = 60 
FIELD_BOTTOM = SCREEN_HEIGHT 
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT - the font used for the game
FONT_FILE = os.path.dirname(os.path.abspath(__file__)) + "batter/assets/fonts/zorque.otf" #file that contains the font for the printed items on the screen
FONT_SMALL = 32 #size of small font
FONT_LARGE = 48 #size of large font

# SOUND - game play sounds
BOUNCE_SOUND = os.path.dirname(os.path.abspath(__file__)) + "batter/assets/sounds/boing.wav" #sound of a bouncing ball - to be replaced with sound of bullet being fired
WELCOME_SOUND =os.path.dirname(os.path.abspath(__file__)) +  "batter/assets/sounds/start.wav" #sound of the opening screen - replace with sound of choice
OVER_SOUND = os.path.dirname(os.path.abspath(__file__)) + "batter/assets/sounds/over.wav" #sound of game over - replace with sound of choice
#ALIEN_SOUND - will be the sound made when the aliens are destroyed

# TEXT 
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS - basic colors used in the game
BLACK = Color(0, 0, 0) 
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS - the keys used during game play assigned to variable for easy use. 
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES - numbers assigned to the different screens in game play for easy use as a parameter in the director class method
NEW_GAME = 0 #the screen for a new game
TRY_AGAIN = 1 #the screen asking the player if they want to try again
NEXT_LEVEL = 2 #the screen for the next level of play
IN_PLAY = 3 
GAME_OVER = 4 #the screen for when the game ends

# LEVELS - the file directory to the level data
LEVEL_FILE = os.path.dirname(os.path.abspath(__file__)) + "batter/assets/data/level-{:03}.txt" #the file directory for the level foundation text
BASE_LEVELS = 5 

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES - the different game phases of play
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS - player stats
STATS_GROUP = "stats" #the group that the stats are held in in the cast class
DEFAULT_LIVES = 3 #starting lives
MAXIMUM_LIVES = 5 #the max number of live the player can have

# HUD - the heads up display to display the stats of the player screen/scene
HUD_MARGIN = 15 #the space around the HUD to differentiate it from the rest o9f the screen and prevent overlap
LEVEL_GROUP = "level" #the cast group for the level being played
LIVES_GROUP = "lives" #the cast group for the lives of the player
SCORE_GROUP = "score" #the cast group for the player's score
LEVEL_FORMAT = "LEVEL: {}" #the displaying of the level being played
LIVES_FORMAT = "LIVES: {}" #the displaying of the number of live the player has
SCORE_FORMAT = "SCORE: {}" #the displaying of the player's score

# BALL - The constants for the ball class which will be converted to the bullet class
BALL_GROUP = "balls" #the cast group for the ball - converted to bullet
BALL_IMAGE = os.path.dirname(os.path.abspath(__file__)) + "batter/assets/images/000.png" #file for ball image - convert to bullet
BALL_WIDTH = 28 #width of ball image - convert to bullet
BALL_HEIGHT = 28 #height of ball image - convert to bullet
BALL_VELOCITY = 6 #speed of the ball in frames - convert to bullet -- bullets only move up or down based on who fired them (positive or negative y dimension) 

# RACKET - the constants for the racket class - convert to ship class
RACKET_GROUP = "rackets" #the cast group for rackets - convert to ship
RACKET_IMAGES = [f"batter/assets/images/{n:03}.png" for n in range(100, 103)] #the file path for the racket image - convert to ship
RACKET_WIDTH = 106 #the width of the racket image - convert to ship
RACKET_HEIGHT = 28 #the height of the racket image - convert to ship
RACKET_RATE = 6 
RACKET_VELOCITY = 7 #the speed the racket moves - conver to ship

# BRICK - the constants for the bricks class - convert to aliens
BRICK_GROUP = "bricks" #the cast group for bricks - convert to aliens
BRICK_IMAGES = {
    "b": [f"batter/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"batter/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"batter/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"batter/assets/images/{i:03}.png" for i in range(40,49)]
} #the brick images - convert to alien
BRICK_WIDTH = 80 #the width of a brick image - convert to alien
BRICK_HEIGHT = 28 #the height of a brick image - convert to alien
BRICK_DELAY = 0.5 
BRICK_RATE = 4
BRICK_POINTS = 50 #the number of points breaking a brick is worth - convert to aliens -- each alien image is worth different amounts of points

# DIALOG - the messages printed on the the screen for the player to read and to give direction
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"