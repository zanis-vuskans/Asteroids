import pygame
from circleshape import CircleShape

from constants import ASTEROID_COLOR, ASTEROID_LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        color = ASTEROID_COLOR
        line_width = ASTEROID_LINE_WIDTH
        radius = self.radius
        position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, color, position, radius, line_width)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt