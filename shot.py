import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_COLOR, SHOT_LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
            self.screen = screen
            color = SHOT_COLOR
            line_width = SHOT_LINE_WIDTH
            radius = SHOT_RADIUS
            position = (int(self.position.x), int(self.position.y))
            pygame.draw.circle(screen, color, position, radius, line_width)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt