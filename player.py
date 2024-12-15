from constants import *
from circleshape import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            (248, 200, 220),
             self.triangle(),
             2
        )

    def rotate(self, dt):
        movement = PLAYER_TURN_SPEED * dt
        self.rotation = movement + self.rotation
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
                
        #left
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        #right
        if keys[pygame.K_d]:
            self.rotate(dt)
        #forward
        if keys[pygame.K_w]:
            self.move(dt)
        #backward
        if keys[pygame.K_s]:
            self.move(dt * -1)
        #pew pew 
        if keys[pygame.K_SPACE]:
            self.shoot()
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        bullet = Bullet(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        print("pew")
        