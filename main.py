import math
import pygame, sys

pygame.init()

bild = pygame.display.set_mode((800,800))
fps = pygame.time.Clock()

def zweige(startX, startY, laenge, startWinkel, rotationsWinkel):
    r = math.pow(startX + laenge - startX, 2) + math.pow(startY + laenge - startY, 2)
    r = math.sqrt(r)

    newX = r * math.cos(math.radians(startWinkel + rotationsWinkel)) + startX
    newY = r * math.sin(math.radians(startWinkel + rotationsWinkel)) + startY

    pygame.draw.line(bild, (255, 255, 255), (startX, startY), (newX, newY))
    if(laenge > 1):

        #rechts
        zweige(newX,newY, laenge * 0.67, startWinkel + rotationsWinkel, rotationsWinkel)

        #links
        zweige(newX, newY, laenge * 0.67, startWinkel - rotationsWinkel, rotationsWinkel)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


   # pygame.draw.line(bild, (255,255,255), (400,800), (400,700))

    r = math.pow (400 + 60 - 400, 2) + math.pow(700 + 60 - 700, 2)
    r = math.sqrt(r)

    newX = r * math.cos(math.radians(330)) + 400
    newY = r * math.sin(math.radians(330)) + 700

   # pygame.draw.line(bild, (255,255,255), (400,700), (newX, newY))

    zweige(400, 800, 100, 240, 30)

    pygame.display.update()
    fps.tick(120)