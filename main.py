import os.path

import pygame
import sys
import random
import subprocess
pygame.init()

screen_width = 720
screen_height = 480

FPS = 30

WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")

line_color = (179, 134, 255)
x = 50
y = 250
width = 68
length =  250

asteroid_height = 1
asteroid_width = 1
asteroid_x = 400
asteroid_y = 400

asteroid_image = pygame.image.load(os.path.join('Assets', 'asteroid.png'))

a = 0
b = (screen_width / 1.5) - 40
a2 = 0
b2 = (screen_height / 1.5) - 40

def ship_window():
    global asteroid_width
    global asteroid_height
    global asteroid_x
    global asteroid_y


    WIN.fill((0,0,0))

    WIN.blit(pygame.transform.scale(asteroid_image, (asteroid_width, asteroid_height)), (asteroid_x, asteroid_y))

    pygame.draw.line(WIN, line_color, start_pos=(0, 0), end_pos=(screen_width / 3, screen_height / 3), width=2)
    pygame.draw.line(WIN, line_color, start_pos=(0, screen_height / 1.5), end_pos=(screen_width / 3, screen_height / 3), width=2)
    pygame.draw.line(WIN, line_color, start_pos=(screen_width / 1.5, 0), end_pos=(screen_width / 3, screen_height / 3), width=2)
    pygame.draw.line(WIN, line_color, start_pos=(screen_width / 1.5, screen_height / 1.5), end_pos=(screen_width / 3, screen_height / 3), width=2)

    pygame.draw.line(WIN, line_color, start_pos=(0, 0), end_pos=(screen_width / 1.5, 0), width=4)
    pygame.draw.line(WIN, line_color, start_pos=(0, screen_height / 1.5), end_pos=(screen_width / 1.5, screen_height / 1.5), width=4)
    pygame.draw.line(WIN, line_color, start_pos=(0, 0), end_pos=(0, screen_height / 1.5), width=4)
    pygame.draw.line(WIN, line_color, start_pos=(screen_width / 1.5, 0), end_pos=(screen_width / 1.5, screen_height / 1.5), width=4)



    pygame.display.update()

def main():
    global asteroid_width
    global asteroid_height
    global asteroid_x
    global asteroid_y

    clock = pygame.time.Clock()
    tick = 0
    run = True
    speed = 1
    while run:
        clock.tick(FPS)
        tick += 1
        if tick > FPS:
            tick = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        asteroid_width += 1
        asteroid_height += 1
        asteroid_x -= speed
        asteroid_y -= speed
        print(tick)

        ship_window()

    pygame.quit()

if __name__ == "__main__":
    main()