from circleshape import *
from constants import *
import random
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    # use the position from the parent bro 
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0), self.position, self.radius,
            2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(new_angle)
            velocity2 = self.velocity.rotate(-new_angle)
            new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
            meteorite1 = Asteroid(self.position.x, self.position.y, new_ast_radius)
            meteorite2 = Asteroid(self.position.x, self.position.y,  new_ast_radius)
            
            meteorite1.velocity = velocity1 * 1.2
            meteorite2.velocity = velocity2 * 1.2

            