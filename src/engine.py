# Engine for the game
# By:  abunai59

import pygame

# Define colors
green = (   0,  255,    0)

# Initialize the pygame library
pygame.init()

# Define the window size
size = [700,500]
# Create a screen from the screen size
screen=pygame.display.set_mode(size)
# Set the window title
pygame.display.set_caption("Shashin Adventure")

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
    screen.fill(green)

    #--Update screen
    pygame.display.flip()

    #--Clock the output
    clock.tick(framerate)

#Upon Quit
pygame.quit()
