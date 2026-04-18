import pygame
import random

# 1st_window_tab
def window():
    # Dimensions of the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Breaker !!")
    return screen
def move_bar():
    pygame.init()
    tab = window()


    # Start position
    x = 400
    y = 500

    width = 20
    height = 20
    vel = 5
    run = True
    while run:
        for moves in pygame.event.get():
            if moves.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 800 - width:
            x += vel
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 600 - height:
            y += vel
        tab.fill((0, 0, 0))
        pygame.draw.rect(tab, (255, 0, 0), (x, y, width, height))
        pygame.display.update()

def ball():
    # x += dx
    # y += dy
    screen = window()
    ball_x = 400
    ball_y = 500
    ball_radius = 10
    dx = 4
    dy = 4
    lunch = move_bar()
    run = True
    while run:
        balls = pygame.key.get_pressed()
        for balls in ball():
            ball_x += dx #壁反射
            ball_y += dy
            if ball_x <= 0 or ball_x >= 800:
                dx *= -1
            if ball_y <=0 or ball_y >= 600:
                dy *= -1

            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 25), (ball_x, ball_y), ball_radius)

    pygame.quit()
if __name__ == "__main__":
     move_bar()