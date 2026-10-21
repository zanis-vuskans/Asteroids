import sys
import random
from highscore import load_high_score, save_high_score
import pygame
pygame.init()

clock = pygame.time.Clock()
dt = 0.0
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import Particle


def main():

    lives = PLAYER_LIVES

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    score = 0
    high_score = load_high_score()
    font = pygame.font.Font(None, 36)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    Particle.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    stars = [
        [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
        random.uniform(10, 80), random.choice([1, 1, 2, 3])]
        for _ in range(150)
    ]

    while True:
        log_state()
        dt = clock.tick(60) / 1000
        # print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if score > high_score:
                    save_high_score(score)
                return
        screen.fill((0, 0, 0))

        for star in stars:
            star[1] += star[2] * dt            # move down
            if star[1] > SCREEN_HEIGHT:        # wrap to top
                star[1] = 0
                star[0] = random.randint(0, SCREEN_WIDTH)
            brightness = int(star[2] / 80 * 155) + 100
            pygame.draw.circle(screen, (brightness,) * 3, (int(star[0]), int(star[1])), star[3])

        # player.update(dt)
        # player.draw(screen)

        updatable.update(dt)
        for asteroid in asteroids:
            if not player.is_invulnerable and player.collides_with(asteroid):
                player.explode()
                lives -= 1
                log_event("player_hit")

                if lives <= 0:
                    print(f"Game over! Final score: {score}")
                    if score > high_score:
                        save_high_score(score)

                    text = font.render(f"Game over! Final score: {score}", True, "white")
                    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

                    screen.fill("black")          # optional: clear the playfield
                    screen.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(3000)        # show it for 3 seconds

                    sys.exit()
                player.respawn()
                break
                
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += 1
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        high_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))      
        high_rect = high_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(high_surface, high_rect)
        screen.blit(font.render(f"Lives: {lives}", True, "white"), (10, 40))
        pygame.display.flip()
        




if __name__ == "__main__":
    main()
