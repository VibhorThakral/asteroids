import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self,x,y,radius):
    super().__init__(x,y,radius)    

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return      
    random_angle = random.uniform(20,50)
    ast_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    ast_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    ast_one.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
    ast_two.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
