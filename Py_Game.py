import pygame
import random

import time

pygame.init()

crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("NFS.wav")

display_width = 800
display_height = 600
car_width = 66
things_count = 1
thing_startx = (0,0,0,0,0,0,0)

pause = False

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)
block_color = (53,115,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car-2.jpg')

#pygame.display.set_icon(carImg)

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg,(x, y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        
        button("Play Again", 150, 450, 100,50, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100,50, red, bright_red, quitgame)
        
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15) 

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:            
        pygame.draw.rect(gameDisplay, ac, (x, y, w,h))
        if click[0] == 1 and action != None:
            action()            
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w,h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2) ) 
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
    

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        
        button("Continue", 150, 450, 100,50, green, bright_green, unpause)
        button("QUIT", 550, 450, 100,50, red, bright_red, quitgame)
        
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15)    
    
	
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
				
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!", 150, 450, 100,50, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100,50, red, bright_red, quitgame)
        
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15)
	

def win():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Win!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        
        button("Play Again", 150, 450, 100,50, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100,50, red, bright_red, quitgame)
        
        mouse = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(15) 

def game_loop():
    pygame.mixer.music.play(-1)
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    dodged = 0
    global things_count
    global thing_startx
    thing_startx = list(thing_startx)
    for i in range(0,things_count):        
        thing_startx[i] = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    thing_width = 100
    thing_height = 100
 
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0



        x += x_change

        gameDisplay.fill(white)

        if dodged < 10:
            things_count = 1
        if dodged > 10 and things_count == 1:
            things_count = 2
        if dodged > 20 and things_count == 2:
            things_count = 3
        if dodged > 30 and things_count == 3:
            things_count = 4
        if dodged > 40 and things_count == 4:
            things_count = 5
        if dodged > 50 and things_count == 5:
            things_count = 6
        if dodged > 60 and things_count == 6:
            things_count = 7
        if dodged > 100:
            win()    
            
        for i in range(0,things_count):
            things(thing_startx[i], thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            for i in range(0,things_count):
                thing_startx[i] = random.randrange(0, display_width)
            dodged += 1
            #thing_speed +=0.01
            #thing_width+= (dodged * 1.01)

        if y < thing_starty + thing_height:
            for i in range(0,things_count):
                if x > thing_startx[i] and x < thing_startx[i] + thing_width or x+car_width > thing_startx[i] and x+car_width < thing_startx[i]+thing_width:
                    crash()

        pygame.display.update()
        clock.tick(60)
		
game_intro()
game_loop()
pygame.quit()
quit()




