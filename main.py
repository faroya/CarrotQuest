# -- import (pygame) models
import pygame

from models import *

# initialization pygame to start  ---->
pygame.init()
pygame.mixer.init()
# ----->

clock = pygame.time.Clock() # Fps -->
eat = pygame.mixer.Sound("eat.wav") #Loading sound 
clock = pygame.time.Clock() # Fps -->

# Game Score ------------->
score = 1
font = pygame.font.SysFont('Arial',50,True)


# varbules ---->
Fps = 30
screen_w = 580 # screen highet
screen_h = 620 # screen width

# set window ---->
win = pygame.display.set_mode((screen_w,screen_h)) 
pygame.display.set_caption("Rabbit") # Title -->

# background add and scaling
bg = pygame.image.load("art/bg.png").convert_alpha()
bg = pygame.transform.scale(bg,(screen_w, screen_h))

# Rabbit ----->
rect1,rabbit = Rabbit(300,screen_h - 135)
# Rabbit --------------->

carrots = [] # insert carrtos & and amont of carrot
for carrot in range(4):
    carrots.append(Carrot(random.randint(20,screen_w-20),random.randint(-50,-10)))

def draw_carrot(carrots,surface): 
    # carrot list // surface --> like window
    for rect,carr in carrots:
        win.blit(carr,(rect.x,rect.y))
        # move carrot downward
        rect.y += 4
run = True
# Main Loop --->
while run:
    clock.tick(Fps)
    
    # Chack The Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if quit then close the game
            run = False

    # Resetting Pos
    for rect,carrot in carrots:
        if rect.y > screen_h:
            # rest carrot pos 
            restpos(rect)

        # Collidetion Chack ---------->
        if rect.colliderect(rect1): # rect1 => Rabbit Rect 
            print("Collide !!")
            # add to score
            score +=1
            # rest carrot pos --->
            restpos(rect)
            # play eat sound -->
            eat.play()


    # move rabbit // keyborad controle
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]: # move left with " <-- "arrow
        rect1.x -= 8
    if key[pygame.K_RIGHT]:# move right with " --> " arrow 
        rect1.x += 8
    
    # Drawing Part & Update screen ------>
    draw_carrot(carrots,win)
    win.blit(rabbit,(rect1.x,rect1.y))

    # Font and score drawing  ------>
    text = font.render(str(score),1,(255,255,255))
    win.blit(text,(screen_w/2.1, 20))

    pygame.display.update()
    win.blit(bg,(0,0)) # background
    
pygame.quit()



