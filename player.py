import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from particle import Particle
import random
from image_loader import load_image

def point_segment_distance(p, a, b):
    #"""Shortest distance from point p to the line segment a-b."""
    ab = b - a
    t = (p - a).dot(ab) / ab.length_squared()
    t = max(0, min(1, t))
    closest = a + ab * t
    return p.distance_to(closest)

def point_in_triangle(p, a, b, c):
    #"""True if point p lies inside triangle abc."""
    def cross(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    d1 = cross(p, a, b)
    d2 = cross(p, b, c)
    d3 = cross(p, c, a)

    has_neg = d1 < 0 or d2 < 0 or d3 < 0
    has_pos = d1 > 0 or d2 > 0 or d3 > 0
    return not (has_neg and has_pos)

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.shot_cooldown = 0
        self.invulnerable_timer = 0
        self.base_image = load_image(
            "assets/Space_ship.png", (PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)
        )

    @property
    def is_invulnerable(self):
        return self.invulnerable_timer > 0

    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        self.shoot_timer = 0
        self.invulnerable_timer = PLAYER_RESPAWN_INVULNERABLE_SECONDS



    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        color = PLAYER_COLOR
        line_width = PLAYER_LINE_WIDTH
        points = self.triangle()
        if self.is_invulnerable and int(self.invulnerable_timer * 10) % 2 == 0:
            return
        #pygame.draw.polygon(screen, color, points, line_width)

        rotated = pygame.transform.rotate(self.base_image, 180 - self.rotation)
        rect = rotated.get_rect(center=self.position)
        screen.blit(rotated, rect)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED



    def explode(self):
        colors = [(255, 255, 255), (100, 180, 255), (255, 200, 80), (255, 120, 40)]
        for _ in range(40):
            Particle(
                self.position.x,
                self.position.y,
                color=random.choice(colors),
                speed_range=(80, 400),
            )
    def collides_with(self, other):
        a, b, c = self.triangle()

        # Case 1: other's center is inside the ship
        if point_in_triangle(other.position, a, b, c):
            return True

        # Case 2: other's circle touches any edge of the ship
        for p1, p2 in ((a, b), (b, c), (c, a)):
            if point_segment_distance(other.position, p1, p2) <= other.radius:
                return True

        return False

    def update(self, dt: float) -> None:
        self.invulnerable_timer = max(0, self.invulnerable_timer - dt)
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown < 0:
                self.shoot()
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS  

        self.wrap() 
                 
