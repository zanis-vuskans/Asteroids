import pygame
pygame.init()

clock = pygame.time.Clock()
dt = 0.0
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH, PLAYER_COLOR
from logger import log_state
from player import Player


def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
        
        player.draw(screen)
        pygame.display.flip()
        




if __name__ == "__main__":
    main()
