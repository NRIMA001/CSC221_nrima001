import pygame
import sys

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blue Background")

BLUE = (135, 206, 250)  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill(BLUE)

    pygame.display.update()

pygame.quit()
sys.exit()
