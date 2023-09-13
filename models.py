import random
import pygame

def Rabbit(x,y):# load image ---->
    # scaling them
    width = 50
    height = 82
    stand = pygame.image.load('art/bunny1_stand.png').convert_alpha() # standing image when no moving --->
    stand = pygame.transform.scale(stand,(width,height)) # scaleing the image to new size ---->
    
    rect = pygame.Rect(x,y, width, height)

    return rect,stand # return rect and stand image


def Carrot(x,y): # load image ---->
    # scaling them
    width = 24
    height = 27
    carrot = pygame.image.load('art/carrots.png')
    carrot = pygame.transform.scale(carrot,(width,height)) # scaleing the image to new size ---->
    # Get Rect , collidetion 
    rect = pygame.Rect(x,y,width,height)

    return rect,carrot # return rect and stand image


def restpos(rect): # rest the postions of carrot

    rect.x = random.randint(0, 530)
    rect.y = random.randint(-50,0)