import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
block_color = (134,43,63)

car_width = 73

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (100, 200))

def things_dodged(count, speed):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))
    text_speed = font.render("Speed: " + str(speed), True, black)
    gameDisplay.blit(text_speed, (0,20))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText, red)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    message_display("You Crashed")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.750)
    x_change = 0
    car_speed = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if x > display_width - car_width or x < 0:
                print('CRASH')
                crash()
                gameExit = True

        x += x_change 
        gameDisplay.fill(white)


        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged, thing_speed)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width-150)
            dodged += 1
            if dodged < 5:
                thing_speed += 0.7
                thing_width += (dodged * -0.8)
            elif dodged >= 5 and dodged < 10:
                thing_speed += 0.5
                thing_width += (dodged * -0.4)
                print(thing_speed)
            elif dodged >= 10 and dodged < 15:
                thing_speed += 0.3
                print(thing_speed)
            elif dodged >= 15:
                thing_speed = thing_speed


            

        # DASH: if double tap key right, teleport to right +50


        if y < thing_starty+thing_height:
            print('y crossover')
            #if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx+thing_width:
            if x+car_width > thing_startx and x < thing_startx + thing_width:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

