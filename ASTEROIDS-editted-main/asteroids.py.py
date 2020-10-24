import pygame
import random,math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((1500,800))
pygame.display.set_caption('\t\t\t\t\tASTEROIDS')
bg=pygame.image.load('backgroung.jpg')

#sounds
mixer.music.load('beat1.wav')
mixer.music.play(-1)
laser=mixer.Sound('E:/OTHERS/python/pygame learning project/ASTEROIDS-editted-main/ASTEROIDS-editted-main/fire.wav')
boom=mixer.Sound('bangMedium.wav')
#player
spaceship=pygame.image.load('spaceship.png')
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
asteroidcount=6
for i in range(asteroidcount):
    asteroid.append(pygame.image.load('rock.png'))
    asteroidx.append(random.randint(0,1600))
    asteroidy.append(random.randint(150,200))
    asteroidx_change.append(3)
    asteroidy_change.append(3)

#bullet
bullet=pygame.image.load('jing.fm-blast-clipart-1178204.png')
bulletx=0
bullety=540
bulletx_change=0
bullety_change=8
bullet_state='ready'

#score
global score_val
score_val=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=20
texty=20

#game over
 
font=pygame.font.Font('freesansbold.ttf',64)



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
   screen.blit(bullet,(x+47,y+40))
   
   
def iscollision(asteroidx,asteroidy,bulletx,bullety):
   distance=math.sqrt(math.pow((asteroidx-bulletx),2)+(math.pow((asteroidy-bullety),2)))
   if distance <40:
         return True
   else:
         return False
 

Running =  True

def score_show(x,y,):
    score=font.render('SCORE :'+str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))
def gameover():
    Text=font.render('GAME OVER !',True,(0,255,0))
    screen.blit(Text,(700,350))
while Running:

   screen.fill((0,0,0))
   screen.blit(bg,[0,0])
                                               

   for event in pygame.event.get():
        if event.type==pygame.QUIT:
           Running=False

  
        if event.type==pygame.KEYDOWN:
           
           
          if event.key==pygame.K_LEFT:
            spaceshipx_change=-5
          if event.key==pygame.K_RIGHT:
            spaceshipx_change=5
          if event.key==pygame.K_UP:
             spaceshipy_change=-5
          if event.key==pygame.K_DOWN:
             spaceshipy_change=5
           
          if event.key==pygame.K_SPACE:
             if bullet_state=='ready':
                 bullety=spaceshipy-20
                 bulletx=spaceshipx
                 laser.play()
                 fireBullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
          
              if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                 spaceshipx_change=0
              if event.key==pygame.K_UP or  event.key==pygame.K_DOWN:
                   spaceshipy_change=0
              
 
   spaceshipy+=spaceshipy_change       
   spaceshipx+=spaceshipx_change
   
#adding borders
   if spaceshipy>=710:
      spaceshipy=710
   elif spaceshipy<=0:
      spaceshipy=0

   if spaceshipx<=0:
      spaceshipx=0
   elif spaceshipx>=1500:
      spaceshipx=1500
   for i in range(asteroidcount):
       asteroidx[i]+=asteroidx_change[i]

       if asteroidx[i]<=0:
          asteroidx_change[i]=3
       elif asteroidx[i]>=1550:
          asteroidx_change[i]=-3


       asteroidy[i]+=asteroidy_change[i]
 
       if asteroidy[i]<=0:
          asteroidy_change[i]=3
       elif asteroidy[i]>=740:
          asteroidy_change[i]=-3
       #collision effects
       collision=iscollision(asteroidx[i],asteroidy[i],bulletx,bullety)
       if collision == True:
           boom.play()
           bullet_state = "ready"
           score_val+=10
           bullety=540
           asteroidy[i] = random.randint(50,100)
           asteroidx[i] = random.randint(0,730)
       asteroid_1( asteroidx[i],asteroidy[i],i)
       #space ship explosion
        
       dis=math.sqrt(math.pow((spaceshipx-asteroidx[i]),2)+(math.pow((spaceshipy-asteroidy[i]),2)))
        
       if dis<=40:
           for i in range(asteroidcount):
               for j in range(asteroidcount):
                   asteroidy[j]=2000
                   gameover()
                   break
           
                
 
           
           
   #bullet movement

   if bullety<=0:
      bullety=540
      bullet_state='ready'
   if bullet_state == 'fire':
       fireBullet(bulletx,bullety)
       bullety-=bullety_change
  
       
   score_show(textx,texty)
   space_ship(spaceshipx,spaceshipy)
   pygame.display.update()
 
quit()
