import pygame as py
import random as rand
import gates
py.init()
#vars below
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
lock = pygame.time.Clock()
myfont = pygame.font.SysFont("Comic Sans MS",15)
running=True 

while running == True:
    lock.tick(100)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            running=False
