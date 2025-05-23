import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
all_shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, all_shots)
AsteroidField = AsteroidField()
def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 1/60
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, all_shots)
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in  pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for every_asteroid in asteroids:
			if player.collision(every_asteroid):
				print("Game over!")
				sys.exit()
		for sprite in drawable:
			sprite.draw(screen)
		dt = clock.tick(60) / 1000
		pygame.display.flip()
if __name__ == "__main__":
	main()
