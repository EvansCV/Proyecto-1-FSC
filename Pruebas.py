import pygame
pygame.init()
blanco = (255, 255, 255)
negro = (20, 20, 20)
pantalla = pygame.display.set_mode((800, 600))


running = True

while running:
	pygame.draw.rect(pantalla, blanco, (0, 0, 400, 200))
	#pygame.draw.rect(pantalla, negro, (0 + 2, 0 + 2, 120, 150 - 4))

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			running = False
	
