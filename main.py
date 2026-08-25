import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    clock = pygame.time.Clock()
    dt = 0.0
    asteroidf = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for entry in drawable:
            entry.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        for entry in asteroids:
            for sh in shots:
                if sh.collides_with(entry):
                    log_event("asteroid_shot")
                    sh.kill()
                    entry.split()
        for entry in asteroids:
            if entry.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
