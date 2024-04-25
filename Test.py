import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window dimensions
window_width = 800
window_height = 600
window_size = (window_width, window_height)

# Create the window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('My Game')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the window with a color (e.g., white)
    window.fill((255, 255, 255))  # RGB value for white
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
