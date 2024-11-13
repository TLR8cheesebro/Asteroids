# import pygame library, dont forget the basics ya filthy animal
import pygame
from constants import *

class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    On = True

#Refresh screen black until quit
    while On == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(Color(255,255,255))
        pygame.display.flip()

if __name__ == "__main__":
    main()