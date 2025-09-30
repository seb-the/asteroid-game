# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import sys

from constants import *

from circleshape import *

from player import *

from asteroidfield import *

from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # setting groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # setting containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # instantization
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0
        updatable.update(dt)
        for thing in asteroids:
            if thing.collide(player):
                print("Game over!")
                sys.exit()
        pygame.Surface.fill(screen,(0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
