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
black=(0,0,0)
white=(255,255,255)
#vars above  
def rectbutton(screen,x,y,w,h,color):
    py.draw.rect(screen,color,(x,y,w,h))
    butot=py.Rect(x,y,w,h)
    global even
    for event in even:
        if event.type == py.MOUSEBUTTONUP:
            if butot.collidepoint((py.mouse.get_pos())):
                return(True)
    
def imgbutton(screen,img,x,y,):
    screen.blit(img,(x,y))
    butt=py.Rect(x,y,img.get_width(),img.get_height())
    eve = py.event.get()
    for eve in events:
        if event.type == py.MOUSEBUTTONUP: 
            if butt.collidepoint((py.mouse.get_pos())):
                return(1)
def Selectlevel():
    lock.tick(10)
    #global events
    for event in events:
        if event.type == py.QUIT: 
            running=False
            py.display.quit()
    screen.fill((50,50,50))
    for i in range(5):
        even=py.event.get(py.MOUSEBUTTONUP)
        global even                
        if i < 5:
            click=rectbutton(screen,200+160*i,200,50,50,black)
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
    select=False
    levnum=16
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
                
        levnum=Selectlevel()
        print(levnum)
    while levnum != 16:
        gamescreen(levnum)
    py.display.flip()
while running:
    lock.tick(10)
    events=py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    main()
