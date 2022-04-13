import pygame


black = pygame.Color('black')
white = pygame.Color('white')
red = pygame.Color('red')
blue = pygame.Color('blue')
print(white, black)
pygame.init()

# screen = pygame.display.set_mode([500, 500])

image = pygame.image.load(r'C:\Users\marc\Downloads\tic_tac_toe_X.jpg')

display_surface = pygame.display.set_mode((380, 380))

#image = pygame.transform.scale(image, (100, 100))
# image.set_colorkey((255, 255, 255))
# image(255, 255, 255).convert_alpha()

running = True
display_surface.fill(white)
#draw tictactoe board
def drawtictacboard():
	pygame.draw.line(display_surface, black, [125,0], [125, 380], 20)
	pygame.draw.line(display_surface, black, [255,0], [255, 400], 20)
	pygame.draw.line(display_surface, black, [0, 125], [400, 125], 20)
	pygame.draw.line(display_surface, black, [0, 255], [400, 255], 20)

drawtictacboard()

def draw_circle(row, column):
	pygame.draw.circle(display_surface, red, (200,200), 55)
	
# draw_circle(0,0)

while running:
	# display_surface.blit(image, (0, 0))

	#Check if user closed window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		pygame.display.update()
	
	# screen.fill((225, 225, 225))
	#screen,

	# pygame.draw.circle(screen, (0, 0, 225), (250, 250), 75)
	pygame.display.flip()


pygame.quit()
quit()