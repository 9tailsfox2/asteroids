import math
from circleshape import *
from constants import *
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.radius = PLAYER_RADIUS
		self.rotation = 0
		width = height = int(math.ceil(PLAYER_RADIUS * math.sqrt(2) * 2))
		self.image = pygame.Surface((width, height), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=(x, y))
	# in the player class
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]
	def draw(self, screen):
		self.image.fill((0, 0, 0, 0))
		local_points = [point - self.rect.center + pygame.Vector2(self.rect.width // 2, self.rect.height // 2) for point in self.triangle()]
		pygame.draw.polygon(self.image, "white", local_points, 2)
		top_left = self.position - pygame.Vector2(self.rect.width // 2, self.rect.height // 2)
		screen.blit(self.image, top_left)
	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)
	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.rect.center = self.position
		if keys[pygame.K_a]:
            		self.rotate(-dt)
		if keys[pygame.K_d]:
            		self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
