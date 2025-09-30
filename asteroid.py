import random

from circleshape import *

from constants import ASTEROID_MIN_RADIUS, SPLIT_ASTEROID_SPEED_MULTIPLIER

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = velocity1 * SPLIT_ASTEROID_SPEED_MULTIPLIER
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = velocity2 * SPLIT_ASTEROID_SPEED_MULTIPLIER



    def update(self, dt):
        self.position += (self.velocity * dt)



