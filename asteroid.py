import math
import random
from constants import *
from circleshape import *
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)
	def update(self, dt):
		self.position += (self.velocity * dt)
	def split(self):
		old_radius = self.radius
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		asteroid_one_velocity = self.velocity.rotate(random_angle)
		asteroid_two_velocity = self.velocity.rotate(-random_angle)
		new_radius = old_radius - ASTEROID_MIN_RADIUS
		asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_one.velocity = asteroid_one_velocity * 1.2
		asteroid_two.velocity = asteroid_two_velocity * 1.2
