import pygame
import circleshape as cs
from shot import Shot
from constants import (
                        PLAYER_RADIUS,
                        LINE_WIDTH,
                        PLAYER_TURN_SPEED,
                        PLAYER_SPEED,
                        PLAYER_SHOOT_SPEED,
                        PLAYER_SHOOT_COOLDOWN_SECONDS
                        )

class Player(cs.CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cool_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):        
        color = "white"
        points_list = self.triangle()
        pygame.draw.polygon(screen, color, points_list, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
      

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cool_timer > 0:
                return
            self.shot_cool_timer = PLAYER_SHOOT_COOLDOWN_SECONDS 
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED





