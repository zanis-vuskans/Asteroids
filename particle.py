import random
import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(255, 200, 80), speed_range=(50, 250)):
        if hasattr(self.__class__, "containers"):
            super().__init__(self.__class__.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        angle = random.uniform(0, 360)
        speed = random.uniform(*speed_range)
        self.velocity = pygame.Vector2(1, 0).rotate(angle) * speed

        self.lifetime = random.uniform(0.4, 0.9)
        self.age = 0
        self.start_radius = random.uniform(2, 4)
        self.color = color

    def update(self, dt):
        self.age += dt
        if self.age >= self.lifetime:
            self.kill()
            return
        self.position += self.velocity * dt
        self.velocity *= 0.98  # slight drag so they slow down

    def draw(self, screen):
        # Shrink over lifetime
        progress = self.age / self.lifetime
        radius = max(1, int(self.start_radius * (1 - progress)))
        pygame.draw.circle(screen, self.color, self.position, radius)