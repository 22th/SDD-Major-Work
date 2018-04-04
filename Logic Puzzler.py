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
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)                
#vars above  
def rectbutton(screen,x,y,w,h,color,events):
    py.draw.rect(screen,color,(x,y,w,h))
    name=py.Rect(x,y,w,h)
    for evet in events:
        if evet.type == py.MOUSEBUTTONUP:
            if name.collidepoint((py.mouse.get_pos())):
                return(True)   
def imgbutton(screen,img,x,y,events):
    screen.blit(img,(x,y))
    butt=py.Rect(x,y,img.get_width(),img.get_height())
    for event in events:
        if event.type == py.MOUSEBUTTONUP: 
            if butt.collidepoint((py.mouse.get_pos())):
                return(True)
            
def Selectlevel():
    lock.tick(10)
    events=py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
            py.display.quit()
    screen.fill((50,50,50))
    i=0
    for i in range(5):              
        if i < 5:
            click=rectbutton(screen,200+160*i,200,50,50,BLACK,events)
            if click == True:
                 return(i)
    py.display.flip()
    return(16)
def gamescreen(levelnum):
    lock.tick(10)
    events = py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    print("y")
    screen.fill((50,50,255))
    py.display.flip()
def main():
    events=py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    
    select=False
    lvnum=False
    levnum=16
    screen.fill((50,50,50))
    start=imgbutton(screen,startbutt,350,100,events)
    if start == True:
        select=True
    #txtbx.update()
    #blit txtbx on the sceen
    #txtbx.set_pos(100,10)
    #txtbx.draw(screen)
    while select:
        for event in py.event.get():
            if event.type == py.QUIT: 
                running=False
                
        levnum=Selectlevel()
    if levnum != 16:
        lvnum = True
        print("test")
    while lvnum:
        gamescreen(levnum)
    py.display.flip()
while running:
    lock.tick(100)
    events=py.event.get(py.QUIT)
    for event in events:
        if event.type == py.QUIT: 
            running=False
    main()
