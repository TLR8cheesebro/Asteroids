import pygame
from constants import *
from circleshape import CircleShape
from player import *

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0, 128, 0),
             self.position,
            SHOT_RADIUS
        )

    def update(self, dt):
        self.position += (self.velocity * dt)