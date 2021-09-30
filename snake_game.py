import pygame
import time
import random

WIDTH=800
HEIGH=600
pygame.init()
surface= pygame.display.set_mode((WIDTH,HEIGH))
pygame.display.set_caption("Snake")
background_colour=(255,255,255)
#surface.fill(background_colour)
#pygame.display.flip()

game_running = True
snake_pos_x = 200 # Snake snake_pos_x coordinate position
snake_pos_y = 200 # Snake snake_pos_y coordinate position
width = 20 #Width of initial snake
height = 20 #Length of initial snake
vel =1 # Speed of the snake
fps = pygame.time.Clock()
snake_moving = "RIGHT"

def quit_game():
    print("Quitting the game")
    quit()
def game_over():
    print("You lost the game")
    quit()

while game_running:

    pygame.time.delay(10) #Delay the time in the game by 10 seconds(Convinient to use because the game is too fast)
    
        # Moving the snake
    if snake_moving == 'Up':
        snake_pos_y -= vel

    if snake_moving == 'Down':
        snake_pos_y += vel

    if snake_moving == 'Left':
        snake_pos_x -= vel

    if snake_moving == 'Right':
        snake_pos_x += vel

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_moving = 'Left'
        if event.key == pygame.K_RIGHT:
            snake_moving = 'Right'
        if event.key == pygame.K_UP:
            snake_moving = 'Up'
        if event.key == pygame.K_DOWN:
            snake_moving = 'Down'
            
        if event.key == pygame.K_ESCAPE:
            quit_game()




    if snake_pos_x<0 or snake_pos_x>800-width:
        game_over()
    if snake_pos_y<0 or snake_pos_y>600-height:
        game_over()


    surface.fill(background_colour)
    pygame.draw.rect(surface, (255,0,0),(snake_pos_x,snake_pos_y,width,height))

    pygame.display.update()
    #fps.tick(vel)
pygame.quit()