import pygame as py
import random as rand
import gates
import eztext
py.init()
#vars below
class Images:
    image=[]
    x=0
    y=0
    img_count=0
    img_selected=False
screen_width = 1000
screen_height = 700
screen = py.display.set_mode((screen_width,screen_height))
lock = py.time.Clock()
myfont = py.font.SysFont("Comic Sans MS",11)
yfont = py.font.SysFont("Comic Sans MS",20)
running=True 
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
prevclickedRes=0
prevclickedPlay=0
WhiteBox=py.image.load("gray.jpg")
WhiteBox=py.transform.scale(WhiteBox,(50,50))
prevclickedResImg=0
#vars above
def screenMsg(screen,x,y,font,text,color):
    xv=font.render(text,1,color)
    screen.blit(xv,(x,y))    
def rectbutton(screen,x,y,w,h,color,events,text,font,fcolor):
    xv=font.render(text,1,fcolor)
    py.draw.rect(screen,color,(x,y,w,h))
    name=py.Rect(x,y,w,h)
    screen.blit(xv,(x+w/2-py.Surface.get_width(xv)/2,y+h/2-py.Surface.get_height(xv)/2))    
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
    return(False)
            
def Selectlevel():
    lock.tick(10)
    events=py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
            py.display.quit()
    screen.fill((50,50,50))
    cou=0
    for j in range(3):
        for i in range(5):  
            cou=cou+1
            click=rectbutton(screen,175+160*i,300+100*j,50,50,BLACK,events,str(cou),myfont,WHITE)
            if click == True:
                return(cou)            
    py.display.flip()
    return(16)
    
def gamescreen(levelnum,LevImageRes,LevImagePlay):
    lock.tick(100)
    global prevclickedResImg
    events = py.event.get()
    for event in events:
        if event.type == py.QUIT: 
            running=False
    screen.fill((50,50,50))
    Playcount=0
    tog1=False
    for j in range(5):
        for i in range(5):
            if LevImagePlay[Playcount].img_selected == False:
                tog1=imgbutton(screen,LevImagePlay[Playcount].image[LevImagePlay[Playcount].img_count],LevImagePlay[Playcount].x,LevImagePlay[Playcount].y,events)
            elif LevImagePlay[Playcount].img_selected == True:
                tog1=imgbutton(screen,WhiteBox,LevImagePlay[Playcount].x,LevImagePlay[Playcount].y,events)
            if tog1 == True:
                if LevImagePlay[Playcount].img_count == prevclickedResImg:
                    LevImagePlay[Playcount].img_selected = False
            Playcount+=1
    coun=0
    tog=False
    global prevclickedRes
    for j in range(5):
        for i in range(5):
            if LevImageRes[coun].img_selected == False:
                tog=imgbutton(screen,LevImageRes[coun].image[LevImageRes[coun].img_count],LevImageRes[coun].x,LevImageRes[coun].y,events)
            if LevImageRes[coun].img_selected == True:
                screen.blit(WhiteBox,(LevImageRes[coun].x,LevImageRes[coun].y))
            if tog == True:
                LevImageRes[prevclickedRes].img_selected = False
                prevclickedRes=coun
                prevclickedResImg=LevImageRes[coun].img_count
                LevImageRes[coun].img_selected = True
            coun+=1
    screenMsg(screen,400,100,yfont,"LOGIC PUZZLER",ORANGE)
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
    txtbx.update(events)
    #blit txtbx on the sceen
    txtbx.set_pos(100,10)
    txtbx.draw(screen)
    while select and levnum == 16:
        for event in py.event.get():
            if event.type == py.QUIT: 
                running=False
                
        levnum=Selectlevel()
    if levnum != 16:
        imcount=[]
        for g in range(25):
            imcount.append(g)
        rand.shuffle(imcount)
        count=0
        LevFilesLoc="Levels/"+str(levnum)+"/" 
        LevImageRes=[]
        for j in range(5):
            for i in range(5):
                LevImagesTemp=Images()
                img=py.image.load(LevFilesLoc +str(count+1) +".jpg")
                img=py.transform.scale(img,(50,50))                
                LevImagesTemp.img_count=imcount[count]
                LevImagesTemp.image.append(img)
                LevImagesTemp.x=i*51
                LevImagesTemp.y=j*51+440
                LevImagesTemp.img_selected=False
                LevImageRes.append(LevImagesTemp)
                count+=1
        count=0
        LevImagesPlay=[]
        for j in range(5):
            for i in range(5):
                LevImagesTemp=Images()
                img=py.image.load(LevFilesLoc +str(count+1) +".jpg")
                img=py.transform.scale(img,(50,50))                
                LevImagesTemp.img_count=count
                LevImagesTemp.image.append(img)
                LevImagesTemp.x=i*51+400
                LevImagesTemp.y=j*51+440
                LevImagesTemp.img_selected=True
                LevImagesPlay.append(LevImagesTemp)
                count+=1
        
        lvnum = True
    while lvnum:
        gamescreen(levnum,LevImageRes,LevImagesPlay)
    py.display.flip()
while running:
    lock.tick(100)
    events=py.event.get(py.QUIT)
    for event in events:
        if event.type == py.QUIT: 
            running=False
    main()
print(locals())
#xkcc
