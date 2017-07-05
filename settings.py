#copied this from part 8

#Creating Pygame Window
TITLE = "Flip!"
WIDTH = 600
HEIGHT = 800
FPS = 60
#FPS stands for frames per second and is how fast your game runs
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 22

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (212,175,55)
PURPLE = (113, 113, 198)
HOT_PINK = (255,105,180)
LIME_GREEN = (50,205,50)
TURQUOISE = (64,224,208)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
MIDNIGHT_BLUE = (25, 25, 112)



