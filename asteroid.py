import pygame
from circleshape import CircleShape
from logger import log_event
from constants import ASTEROID_COLOR, ASTEROID_LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from particle import Particle
import random
from image_loader import load_image, random_asteroid_path


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, image_path=None) -> None:
        super().__init__(x, y, radius)
        self.image_path = image_path or random_asteroid_path()
        size = (int(radius * 2), int(radius * 2))
        self.image = load_image(self.image_path, size)

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        color = ASTEROID_COLOR
        line_width = ASTEROID_LINE_WIDTH
        radius = self.radius
        position = (int(self.position.x), int(self.position.y))
        rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, rect)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.wrap(margin=ASTEROID_MAX_RADIUS)

    def explode(self):
        count = int(self.radius / 2)  # bigger asteroids = bigger explosions
        for _ in range(count):
            Particle(self.position.x, self.position.y)

    def split(self):
        self.explode()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        new_movement_one = self.velocity.rotate(new_angle)
        new_movement_two = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_one.velocity = new_movement_one * 1.2
        asteroid_two.velocity = new_movement_two * 1.2
