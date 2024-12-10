from constants import *
from circleshape import *

class Bullet(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0, 128, 0),
             self.position,
            SHOT_RADIUS
        )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        #shoot
        if keys[pygame.K_SPACE]:
            print("pew")
            self.draw()
            
        
