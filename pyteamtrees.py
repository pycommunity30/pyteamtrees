#teamtrees
import pygame
import random
import time
x = 0
y = 0
treex = random.randint(20,580)
treey = random.randint(40,380)
window = pygame.display.set_mode((600,400),0,32)
green = (0,150,0)
brown = (50,40,0)
white = (255,255,255)
mission = "Collect the saplings!!!"
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
time.sleep(1)
tile = pygame.draw.rect(window, green,(x,y,30,30))
while True:
    if pyg
    window.fill(white)
    textsurface = myfont.render("Mission: " + mission, False, (0, 0, 0))
    window.blit(textsurface, (0, 0))
    pygame.draw.rect(window, brown,((treex + 9),(treey + 30),15,30))
    pygame.draw.rect(window, green,(treex,treey,30,30))
    pygame.display.update()
