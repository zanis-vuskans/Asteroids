import pygame
pygame.init()

clock = pygame.time.Clock()
dt = 0.0
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        dt = clock.tick(60) / 1000
        # print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
