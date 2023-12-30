import pygame
import random

WSize = (720, 480)

screen = pygame.display.set_mode(WSize)

TSide = 30
MSize = WSize[0] // TSide, WSize[1] // TSide

start_pos = MSize[0] // 2, MSize[1] // 2
snake = [start_pos]
alive = True

direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

apple = random.randint(0, MSize[0]-1), random.randint(0, MSize[1]-1)

FPS = 6
clock = pygame.time.Clock()

pygame.font.init()
font_gameover = pygame.font.SysFont('Arial', 45)


run = True
while run:
    clock.tick(FPS)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_d and direction != 2:
                    direction = 0
                if event.key == pygame.K_s and direction != 3:
                    direction = 1
                if event.key == pygame.K_a and direction != 0:
                    direction = 2
                if event.key == pygame.K_w and direction != 1:
                    direction = 3
            else:
                if event.key == pygame.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    apple = random.randint(0, MSize[0]-1), random.randint(0, MSize[1]-1)
                    FPS = 6


    [pygame.draw.rect(screen, "green", (x * TSide, y * TSide, TSide - 1, TSide - 1)) for x, y in snake]
    pygame.draw.rect(screen, "red", (apple[0] * TSide, apple[1] * TSide, TSide - 1, TSide - 1))

    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < MSize[0] and 0 <= new_pos[1] < MSize[1]) or new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                FPS += 1
                apple = random.randint(0, MSize[0]-1), random.randint(0, MSize[1]-1)
            else:
                snake.pop(-1)
    else:
        text = font_gameover.render('GAME OVER', True, 'white')
        screen.blit(text, (WSize[0] // 2 - text.get_width() // 2, WSize[1] // 2 - 40))

    pygame.display.flip()
