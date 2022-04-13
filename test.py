import pygame


black = pygame.Color('black')
white = pygame.Color('white')
red = pygame.Color('red')
blue = pygame.Color('blue')
print(white, black)
pygame.init()

LINEWIDTH = 10

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
	pygame.draw.line(display_surface, black, [125,0], [125, 380], LINEWIDTH)
	pygame.draw.line(display_surface, black, [255,0], [255, 400], LINEWIDTH)
	pygame.draw.line(display_surface, black, [0, 125], [400, 125], LINEWIDTH)
	pygame.draw.line(display_surface, black, [0, 255], [400, 255], LINEWIDTH)

drawtictacboard()

def draw_circle(row, column):
	pygame.draw.circle(display_surface, red, (60 + row*(LINEWIDTH + 120), 60 + column*(LINEWIDTH + 120)), 55)
	
draw_circle(1,1)

def draw_x(row, column):
	#first draw an x on the first block
	offset_x = row * (120 + LINEWIDTH)
	offset_y = column * (120 + LINEWIDTH)
	pygame.draw.line(display_surface, blue, [5 + offset_x, 5 + offset_y], [115+ offset_x, 115 + offset_y], 5)
	pygame.draw.line(display_surface, blue, [5 + offset_x, 115 + offset_y], [115 + offset_x , 5 + offset_y], 5)

draw_x(1,2)

while running:
	# display_surface.blit(image, (0, 0))

	#Check if user closed window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		pygame.display.update()
	# print(pygame.mouse.get_pos())
	pygame.display.flip()


pygame.quit()
quit()