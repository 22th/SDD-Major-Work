import pygame as py
import random as rand
import gates
import eztext
py.init()
#vars below
screen_width = 1000
screen_height = 700
screen = py.display.set_mode((screen_width,screen_height))
lock = py.time.Clock()
myfont = py.font.SysFont("Comic Sans MS",15)
running=True 
gate=gates.LogicGates()
txtbx = eztext.Input(maxlength=45, color=(255,255,255), prompt='type here: ')
#vars above
def imgbutton(screen,img,x,y,):
    screen.blit(img,(x,y))
    imgw=img.get_Width()
    imgh=img.get_Height()
    events = py.event.get()
    for event in events:
        if event.type == py.MOUSEBUTTONUP: 
            mousepos=py.mouse.get_pos()
            if x+imgw > mousepos[0] > x and y+imgh > mousepos[1] > y:
                return(1)

while running == True:
    lock.tick(100)
    events = py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    
