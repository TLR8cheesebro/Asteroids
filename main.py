# import pygame library, dont forget the basics ya filthy animal
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from bullet import *


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
    asteroids = pygame.sprite.Group()
    bullet = pygame.sprite.Group()
    bullet.radius = SHOT_RADIUS
    
    Bullet.containers = (bullet, updatable, drawable)


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    

#game loop
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        #frame rate 60 secs, set delta time
        dt = (in_game_clock.tick(60)) / 1000

        for shot in bullet:
            for asteroid in asteroids:
                if asteroid.collision(shot) == True:
                    shot.kill()
                    asteroid.split()
                    print("BLLAAOOOOWWWW")

        for obj in asteroids:
            if obj.collision(player1) == True:
                print("Game Over !!!!!")
                print("womp womp :'(")
                Running = False   

        #rotate ship
        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))

        #screen goes here
        for obj in drawable:
            obj.draw(screen)


        # is this my update step?
        pygame.display.flip()
    
    
    pygame.quit()

if __name__ == "__main__":
    main()