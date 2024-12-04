# import pygame library, dont forget the basics ya filthy animal
import pygame
from constants import *
from circleshape import *
from player import *


player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


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
    Running = True

    in_game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player1.containers = (updatable, drawable)
    

#Refresh screen black until quit
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        #frame rate 60 secs, set delta time
        dt = (in_game_clock.tick(60)) / 1000     
        
        screen.fill((0, 0, 0))
        
        #rotate ship
        for obj in updatable:
            obj.update(dt)
        #player draw goes here
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
           
    
    pygame.quit()

if __name__ == "__main__":
    main()