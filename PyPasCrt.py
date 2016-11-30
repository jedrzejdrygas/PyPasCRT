import pygame, sys, gc
from pygame.locals import *
from collections import OrderedDict
gc.enable()
pygame.init()
rozmiar_x=900
rozmiar_y=600
tablica=pygame.display.set_mode((rozmiar_x,rozmiar_y))
#rozmiar piksela
x_switch=(rozmiar_x-100)/80
y_switch=rozmiar_y/24
#kolory
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BROWN = (170,85,0)
CYAN=(0,170,170)
GRAY=(170,170,170)
MAGENTA=(170,0,170)
kolor=[BLACK,WHITE,RED,GREEN,BLUE,BROWN,CYAN,GRAY,MAGENTA]

kolory=[]

piksele=[]
wartosc_y=[]
for y in range(rozmiar_y):
    if y%25==0:
        wartosc_y.append(y)
print wartosc_y
przycisk=0
for y in wartosc_y:
        x=90
        while x<(rozmiar_x-x_switch):
            x=x+x_switch
            piksele.append(pygame.Rect(x, y, x_switch, y_switch))
x=0
y=0
pygame.draw.rect(tablica, BLACK,(0,0, 50,50))
pygame.draw.rect(tablica, RED,(50,0, 50,50))
pygame.draw.rect(tablica, GREEN,(0,50, 50,50))
pygame.draw.rect(tablica, BLUE,(50,50, 50,50))
pygame.draw.rect(tablica, BROWN,(0,100, 50,50))
pygame.draw.rect(tablica, CYAN,(50,100, 50,50))
pygame.draw.rect(tablica, GRAY,(0,150,50,50))
pygame.draw.rect(tablica, MAGENTA,(50,150, 50,50))
pygame.draw.rect(tablica, WHITE,(0,200, 100,50))
a=pygame.font.get_default_font()
myfont = pygame.font.SysFont(a, 30)
label = myfont.render("Paleta", 1, BLACK)
tablica.blit(label, (0, 225))
pygame.display.flip()
czarny=pygame.Rect(0,0, 50,50)
czerwony=pygame.Rect(50,0, 50,50)
zielony=pygame.Rect(0,50, 50,50)
niebieski=pygame.Rect(50,50, 50,50)
brazowy=pygame.Rect(0,100, 50,50)
turkusowy=pygame.Rect(50,100, 50,50)
szary=pygame.Rect(0,150,50,50)
fiolet=pygame.Rect(50,150, 50,50)
kolor=BLACK
file=open("./Program.pas", 'w+')
plik=[]
plik2=[]
file.writelines('uses crt;')
file.writelines('\n')
file.writelines('Begin ')
file.writelines('\n')
file.writelines('ClrScr;')
file.writelines('\n')
while True:
    
    for event in pygame.event.get():
        if event.type==QUIT:        
            plik2=list(OrderedDict.fromkeys(plik))
            print plik2
            for x in range(len(plik2)):
                file.write(plik2[x])
            file.writelines('GotoXY(80,24);')
            file.writelines('TextBackground(Black);')
            file.writelines('Readln()')
            file.writelines('end.')
            file.close()
            pygame.quit()
            sys.exit    
        elif event.type == MOUSEBUTTONUP:
            przycisk=0
        elif event.type == MOUSEBUTTONDOWN:
            przycisk=1
            for r in piksele:
                    if r.collidepoint(event.pos):
                        print r
                        x=r[0]/10 -9
                        y=r[1]/25 +1
                        print x, y
                        pygame.draw.rect(tablica, (kolor),((r)))
                        if kolor ==BLACK:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(0)+');'+ "write(' ');\n ")
                        elif kolor==BLUE:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(1)+');'+ "write(' ');\n") 
                        elif kolor==GREEN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(2)+');'+ "write(' ');\n") 
                        elif kolor==CYAN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(3)+');'+ "write(' ');\n") 
                        elif kolor == RED:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(4)+');'+ "write(' ');\n") 
                        elif kolor==MAGENTA:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(5)+');'+ "write(' ');\n") 
                        elif kolor==BROWN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(6)+');'+ "write(' ');\n") 
                        elif kolor==GRAY:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(7)+');'+ "write(' ');\n") 
            if czarny.collidepoint(event.pos):
                kolor=BLACK
            if czerwony.collidepoint(event.pos):
                kolor=RED
            if zielony.collidepoint(event.pos):
                kolor=GREEN
            if niebieski.collidepoint(event.pos):
                kolor=BLUE
            if brazowy.collidepoint(event.pos):
                kolor=BROWN
            if szary.collidepoint(event.pos):
                kolor=GRAY
            if turkusowy.collidepoint(event.pos):
                kolor=CYAN
            if fiolet.collidepoint(event.pos):
                kolor=MAGENTA
            
        elif przycisk==1 and event.type==MOUSEMOTION:
                for r in piksele:
                    if r.collidepoint(event.pos):
                        x=event.pos[0]
                        y=event.pos[1]
                        pygame.draw.rect(tablica, (kolor),((r)))
                        x=r[0]/10 - 9
                        y=r[1]/25 +1
                        print x,y
                        pygame.draw.rect(tablica, (kolor),((r)))
                        if kolor ==BLACK:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(0)+');'+ "write(' ');\n ")
                        elif kolor==BLUE:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(1)+');'+ "write(' ');\n") 
                        elif kolor==GREEN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(2)+');'+ "write(' ');\n") 
                        elif kolor==CYAN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(3)+');'+ "write(' ');\n") 
                        elif kolor == RED:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(4)+');'+ "write(' ');\n") 
                        elif kolor==MAGENTA:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(5)+');'+ "write(' ');\n") 
                        elif kolor==BROWN:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(6)+');'+ "write(' ');\n") 
                        elif kolor==GRAY:

                            plik.append('GotoXY('+str(x)+ ',' +str(y) + '); TextBackground('+str(7)+');'+ "write(' ');\n") 
                        
   
    pygame.display.update()

pygame.quit()
