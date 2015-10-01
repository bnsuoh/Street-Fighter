#!/usr/bin/env python
#Hisar Tetris
#copyright: Bensu Sicim
#Hisar Schools
#import time
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
w,h,pWidth=1024,718,100
BLACK=(0,0,0)
WHITE=(255,255,255)
screen=pygame.display.set_mode((1024,718))
pygame.display.set_caption("Street Fighter!")
font=pygame.font.Font(None, 60)
text1=font.render("Player 1 Wins!", True, WHITE)
text2=font.render("Player 2 Wins!", True, WHITE)
class player:
    def __init__(self,a):
        self.x=a
        self.x2=self.x+pWidth
        self.xin=self.x
        self.speed=50
        self.health=100
        self.turbo=0
def attack(self,opp):
    opp.healthin=opp.health
    if self.turbo!=3:
        self.turbo+=1
        opp.health-=5
        opp.turbo=0
    elif self.turbo==3:
        opp.health-=30
        self.turbo=0
        opp.turbo=0
def moveRight(self):
    self.xin=self.x
    self.x+=self.speed
    self.x2+=self.speed
def moveLeft(self):
    self.xin=self.x
    self.x-=self.speed
    self.x2-=self.speed
p1=player(40)
p2=player((w-140))
def checkButtons():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and p1.x2<w:
                moveRight(p1)
            elif event.key == K_a and p1.x>0:
                moveLeft(p1)
            elif event.key == K_w and p2.health!=0 and (abs(p2.x2-p1.x)<=50 or abs(p2.x-p1.x2)<=50):
                attack(p1,p2)
            if event.key == K_LEFT and p2.x>0:
                moveLeft(p2)
            elif event.key == K_RIGHT and p2.x2<w:
                moveRight(p2)
            elif event.key == K_UP and p1.health!=0 and (abs(p2.x2-p1.x)<=50 or abs(p2.x-p1.x2)<=50):
                attack(p2,p1)
        if p1.health<=0:
            p1.health=0
        elif p2.health<=0:
            p2.health=0
while True:
    if p1.health!=0 and p2.health!=0:
         checkButtons()
         pygame.draw.rect(screen,BLACK,Rect((p1.xin, h-400),(100,400)))
         pygame.draw.rect(screen,BLACK,Rect((p2.xin, h-400),(100,400)))
         pygame.draw.rect(screen,(255,51,204),Rect((p1.x, h-400),(100,400)))
         pygame.draw.rect(screen,(51,102,255),Rect((p2.x,h-400),(100,400)))

         pygame.draw.rect(screen,BLACK,Rect((40,40),(944,50)))
         pygame.draw.rect(screen,WHITE,Rect((40,40),(p1.health*4,50)))
         pygame.draw.rect(screen,WHITE,Rect((w-440,40),(p2.health*4,50)))

         pygame.draw.rect(screen,BLACK,Rect((40,90),(944,50)))
         pygame.draw.rect(screen,WHITE,Rect((40,90),(p1.turbo*(400/3),50)))
         pygame.draw.rect(screen,WHITE,Rect((w-440,90),(p2.turbo*(400/3),50)))
    else:
        if p1.health==0:
            screen.blit(text2,(400,300))
        elif p2.health==0:
            screen.blit(text1,(400,300))
    pygame.display.update()
                    
    
    
