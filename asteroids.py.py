 import pygame
import random,math
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('\t\t\t\t\tSPACE INVADERS')
bg=pygame.image.load('backgroung.jpg')


#player
spaceship=pygame.image.load('spaceship.png')
spaceshipx=370
spaceshipy=480
spaceshipx_change=0
spaceshipy_change=0
spaceship_rect=spaceship.get_rect(center=(spaceshipx,spaceshipy))
angle=0

#asteroids
asteroid1=pygame.image.load('asteroid1.png')
asteroid1x=random.randint(0,730)
asteroid1y=random.randint(50,100)
asteroid1x_change=1
asteroid1y_change=1

#bullet
bullet=pygame.image.load('bulletG.png')
bulletx=0
bullety=540
bulletx_change=0
bullety_change=8
bullet_state='ready'


#icon
icon=pygame.image.load('title.png')
pygame.display.set_icon(icon)

 
 
#defining player
def space_ship(x,y):
   screen.blit(spaceship,(x,y))

def asteroid_1(x,y):
   screen.blit(asteroid1,(x,y))

def rotate(surface,angle):
   rotated_surface=pygame.transform.rotozoom(surface,angle,1)
   rotated_rect=rotated_surface.get_rect(center=(spaceshipx,spaceshipy))
   
   return rotated_surface ,rotated_rect

def fireBullet(x,y):
   global bullet_state
   bullet_state='fire'
   screen.blit(bullet,(x+18,y+40))
def iscollision(asteroid1x,asteroid1y,bulletx,bullety):
   distance=math.sqrt(math.pow((asteroid1x-bulletx),2)+math.pow((asteroid1y-bullety),2))
   if distance <5:
      True
   else:
         False

Running =  True

score=0

while Running:

   screen.fill((0,0,0))
   screen.blit(bg,[0,0])
                                               

   for event in pygame.event.get():
        if event.type==pygame.QUIT:
           Running=False

  
        if event.type==pygame.KEYDOWN:
           
           
          if event.key==pygame.K_LEFT:
            spaceshipx_change=-1.5
          if event.key==pygame.K_RIGHT:
            spaceshipx_change=1.5
          if event.key==pygame.K_UP:
             spaceshipy_change=-1.5
          if event.key==pygame.K_DOWN:
             spaceshipy_change=1.5
           
          if event.key==pygame.K_SPACE:
             if bullet_state=='ready':
                 bullety=spaceshipy-20
                 bulletx=spaceshipx
                 fireBullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
          
              if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                 spaceshipx_change=0
              if event.key==pygame.K_UP or  event.key==pygame.K_DOWN:
                   spaceshipy_change=0
              
 
   spaceshipy+=spaceshipy_change       
   spaceshipx+=spaceshipx_change

   if spaceshipy>=540:
      spaceshipy=540
   elif spaceshipy<=0:
      spaceshipy=0

   if spaceshipx<=0:
      spaceshipx=0
   elif spaceshipx>=730:
      spaceshipx=730
   asteroid1x+=asteroid1x_change

   if asteroid1x<=0:
      asteroid1x_change=1
   elif asteroid1x>=736:
      asteroid1x_change=-1


   asteroid1y+=asteroid1y_change
 
   if asteroid1y<=0:
      asteroid1y_change=1
   elif asteroid1y>=540:
      asteroid1y_change=-1


   #bullet movement

   if bullety<=0:
      bullety=540
      bullet_state='ready'
   if bullet_state == 'fire':
       fireBullet(bulletx
                  ,bullety)
       bullety-=bullety_change
 #collision
       collision=iscollision(asteroid1x,asteroid1y,bulletx,bullety)
       if collision:
             bullety=540
             bullet_state='ready'
             score+=5
             print(score)
        
       asteroid1x=random.randint(0,730)
       asteroid1y=random.randint(50,100)     

   asteroid_1( asteroid1x,asteroid1y)
   space_ship(spaceshipx,spaceshipy)
   pygame.display.update()
 
quit()
