import pygame
pygame.init()

clock = pygame.time.Clock()
dt = 0.0
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH, PLAYER_COLOR
from logger import log_state
from player import Player


def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        dt = clock.tick(60) / 1000
        # print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # player.update(dt)
        # player.draw(screen)

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        




if __name__ == "__main__":
    main()
