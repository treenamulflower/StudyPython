import pygame
from sys import exit

#Basics

pygame.init() #necessary
screen = pygame.display.set_mode((800, 400))  #width, height
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

while True:
    #Closes game once you press X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  #opposite of pygame.init()
            exit()
    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60) #Maximum framerate


#Display image

