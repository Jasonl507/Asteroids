import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

version = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill("black")
        
        for things in drawable:
            things.draw(screen)
        
        for objects in asteroids:
            if objects.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for objects in asteroids:
            for shot in shots:
                if objects.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    objects.split()
                    shot.kill()


        pygame.display.flip()

        log_state()

        dt = clock.tick(60) / 1000
       

    



if __name__ == "__main__":
    main()
