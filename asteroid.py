from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    # random spawn point variables ????
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            2
        )

    def update(self, dt):
        flight_path = self.position + (self.velocity * dt)
