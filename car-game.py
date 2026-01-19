import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255, 255, 255)

car_width = 73

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (100, 200))


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.750)
    x_change = 0
    car_speed = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            print(x)

            # How to just set a boundary though? 
            
            if x > display_width - car_width or x < 0:
                print('CRASH')
                gameExit = True

        x += x_change 

        gameDisplay.fill(white)
        car(x,y)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

