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
txtbx = eztext.Input(maxlength=45, color=(255,255,255), prompt='Name: ')
startbutt=py.image.load("startbutton.png")
start=0
SL=0
py.display.set_caption("Logic Puzzler")
#vars above    
def imgbutton(screen,img,x,y,):
    screen.blit(img,(x,y))
    butt=py.Rect(x,y,img.get_width(),img.get_height())
    ev = py.event.get()
    for ev in events:
        if event.type == py.MOUSEBUTTONDOWN: 
            mousepos=py.mouse.get_pos()
            if butt.collidepoint((mousepos)):
                return(1)
def Selectlevel():
    lock.tick(10)
    global events
    for event in events:
        if event.type == py.QUIT: 
            running=False
            py.display.quit()
    print("y")
    screen.fill((59,50,255))
    py.display.flip()
def gamescreen(levelnum):
    lock.tick(10)
    events = py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    print("y")
    screen.fill((50,50,50))
    py.display.flip()
def main():
    select=False
    screen.fill((50,50,50))
    start=imgbutton(screen,startbutt,350,100)
    print(start)
    if start == 1:
        select=True
    #txtbx.update()
    #blit txtbx on the sceen
    #txtbx.set_pos(100,10)
    #txtbx.draw(screen)
    while select:
        for event in py.event.get():
            if event.type == py.QUIT: 
                running=False
        
        Selectlevel()
    py.display.flip()
while running:
    lock.tick(10)
    events=py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    main()
