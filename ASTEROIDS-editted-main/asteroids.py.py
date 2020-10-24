import pygame
import random,math
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('\t\t\t\t\tASTEROIDS')
bg=pygame.image.load('backgroung.jpg')


#player
spaceship=pygame.image.load('ufo.png')
spaceshipx=370
spaceshipy=480
spaceshipx_change=0
spaceshipy_change=0
spaceship_rect=spaceship.get_rect(center=(spaceshipx,spaceshipy))
angle=0

#asteroids
asteroid=[]
asteroidx=[]
asteroidy=[]
asteroidx_change=[]
asteroidy_change=[]
asteroidcount=4
for i in range(asteroidcount):
    asteroid.append(pygame.image.load('rock.png'))
    asteroidx.append(random.randint(0,730))
    asteroidy.append(random.randint(50,100))
    asteroidx_change.append(1)
    asteroidy_change.append(1)

#bullet
bullet=pygame.image.load('jing.fm-blast-clipart-1178204.png')
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

def asteroid_1(x,y,i):
   screen.blit(asteroid[i],(x,y))


def fireBullet(x,y):
   global bullet_state
   bullet_state='fire'
   screen.blit(bullet,(x+18,y+40))
   
def iscollision(asteroidx,asteroidy,bulletx,bullety):
   distance=math.sqrt(math.pow((asteroidx-bulletx),2)+(math.pow((asteroidy-bullety),2)))
   if distance <40:
         return True
   else:
         return False

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
            spaceshipx_change=-2
          if event.key==pygame.K_RIGHT:
            spaceshipx_change=2
          if event.key==pygame.K_UP:
             spaceshipy_change=-2
          if event.key==pygame.K_DOWN:
             spaceshipy_change=2
           
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
   
#adding borders
   if spaceshipy>=540:
      spaceshipy=540
   elif spaceshipy<=0:
      spaceshipy=0

   if spaceshipx<=0:
      spaceshipx=0
   elif spaceshipx>=730:
      spaceshipx=730
   for i in range(asteroidcount):
       asteroidx[i]+=asteroidx_change[i]

       if asteroidx[i]<=0:
          asteroidx_change[i]=1
       elif asteroidx[i]>=736:
          asteroidx_change[i]=-1


       asteroidy[i]+=asteroidy_change[i]
 
       if asteroidy[i]<=0:
          asteroidy_change[i]=1
       elif asteroidy[i]>=540:
          asteroidy_change[i]=-1
       #collision effects
       collision=iscollision(asteroidx[i],asteroidy[i],bulletx,bullety)
       if collision == True:
           bullet_state = "ready"
           bullety=540
           asteroidy[i] = random.randint(50,100)
           asteroidx[i] = random.randint(0,730)
       asteroid_1( asteroidx[i],asteroidy[i],i)

   #bullet movement

   if bullety<=0:
      bullety=540
      bullet_state='ready'
   if bullet_state == 'fire':
       fireBullet(bulletx,bullety)
       bullety-=bullety_change
  
       
   
   space_ship(spaceshipx,spaceshipy)
   pygame.display.update()
 
quit()
