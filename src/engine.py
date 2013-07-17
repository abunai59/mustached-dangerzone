# Engine for the game
# By:  abunai59

import pygame
import os

# Define colors
green = (   0,  255,    0)
black = (   0,  0,      0)

# Initialize the pygame library
pygame.init()

# Define path to executable
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Define path to resources
__resources__ = __location__ + "\\..\\resources"

# Define the window size
size = [700,500]
# Create a screen from the screen size
screen=pygame.display.set_mode(size)
# Set the window title
pygame.display.set_caption("Shashin Adventure")

# Create a background surface to draw to
background = pygame.Surface(screen.get_size())
# Fill the background with black initially
background.fill(black)
# Define position of background image
background_pos = [0,0]
# Define initial background image
background_img = pygame.image.load(__resources__ +"\default.png").convert()

# Check for user quitting
done = False

# Create a clock to use for screen update
clock = pygame.time.Clock()
# Decide the framerate of the screen update
framerate = 20

# Begin program loop
while done == False:
    #--Event processing
    for event in pygame.event.get():
        # Handle quit input
        if event.type == pygame.QUIT:   
            done = True
        # Handle other input

    #--Game logic

    #--Draw code
    screen.blit(background_img, background_pos)

    #--Update screen
    pygame.display.flip()

    #--Clock the output
    clock.tick(framerate)

#Upon Quit
pygame.quit()
