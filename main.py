import pygame
from config import *
from explosion import Explosion

pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")


explosion_group = pygame.sprite.Group()
 
run = True
while run:

  clock.tick(FPS)

    # update background
  screen.fill(CUSTOM_COLOR)

  explosion_group.draw(screen)
  explosion_group.update()

  
  

  
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      explosion = Explosion(pos[0], pos[1])
      explosion_group.add(explosion)

  pygame.display.update()

pygame.quit()
