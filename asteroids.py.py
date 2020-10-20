import pygame
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('\t\t\t\t\tSPACE INVADERS')


spaceship=pygame.image.load('spaceship.png')
spaceshipx=370
spaceshipy=480
spaceshipx_change=0
spaceshipy_change=0

icon=pygame.image.load('title.png')
pygame.display.set_icon(icon)

 
offset=[0,0]

def space_ship(x,y):
   screen.blit(spaceship,(x,y))


Running =  True

while Running:

   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           Running= False

  
       if event.type==pygame.KEYDOWN:
          
          if event.key==pygame.K_LEFT:
            spaceshipx_change=-0.5
          if event.key==pygame.K_RIGHT:
            spaceshipx_change=0.5
          if event.key==pygame.K_UP:
             spaceshipy_change=0.5
          if event.key==pygame.K_DOWN:
             spaceshipy_change=-0.5
       if event.type==pygame.KEYUP:
          
          if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
      

                  spaceshipx_change=0
          if event.key==pygame.K_UP or  event.key==pygame.K_DOWN:


                  spaceshipy_change=0
                  
 

   spaceshipy+=spaceshipy_change       
   spaceshipx+=spaceshipx_change

   if spaceshipy<=540:
      spaceshipy=540
   elif spaceshipy>=0:
      spaceshipy=0

   if spaceshipx<=0:
      spaceshipx=0
   elif spaceshipx>=730:
      spaceshipx=730


   space_ship(spaceshipx,spaceshipy)
   pygame.display.update()
 
quit()

