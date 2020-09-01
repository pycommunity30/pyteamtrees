#teamtrees
import pygame
import random
import time
x = 100
y = 100
treex = random.randint(20, 580)
treey = random.randint(40, 380)
window = pygame.display.set_mode((600, 400), 0, 32)
green = (0, 150, 0)
brown = (50, 40, 0)
white = (255, 255, 255)
mission = "Collect the saplings!!!"
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
time.sleep(1)
move = "right"
while True:
    tile = pygame.draw.rect(window, green, (x, y, 30, 30))
    if pygame.KEYDOWN:
        if pygame.K_a:
            move = "left"
        elif pygame.K_d:
            move = "right"
        elif pygame.K_w:
            move = "up"
        elif pygame.K_s:
            move = "down"
    if move == "up":
        y -= 30
    elif move == "down":
        y += 30
    elif move == "left":
        x -= 30
    elif move == "right":
        x += 30

    window.fill(white)
    textsurface = myfont.render("Mission: " + mission, False, (0, 0, 0))
    window.blit(textsurface, (0, 0))
    pygame.draw.rect(window, brown, ((treex + 9), (treey + 30), 15, 30))
    pygame.draw.rect(window, green, (treex, treey, 30, 30))
    pygame.display.update()
