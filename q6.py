import random, pygame 
from pygame.locals import*

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('teste')

def pintarQuadrado():
  screen.fill(PRETO)
  pygame.draw.rect(screen,(AMARELO),(random.randint(0,600),random.randint(0,600),50,50))


while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
    elif event.type == pygame.KEYDOWN:   
      if event.key == pygame.K_SPACE: 
        pintarQuadrado()

    pygame.display.update()