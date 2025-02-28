import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 0)

# Snake settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Clock and font
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

# Function to display the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(SCREEN, BLACK, [x[0], x[1], snake_block, snake_block])

# Animated background pattern
def draw_pattern():
    for i in range(0, WIDTH, 20):
        for j in range(0, HEIGHT, 20):
            color = YELLOW if (i // 20 + j // 20) % 2 == 0 else BLUE
            pygame.draw.rect(SCREEN, color, [i, j, 20, 20])

# Message display
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH / 2, HEIGHT / 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:
        while game_close:
            SCREEN.fill(WHITE)
            message("You lost! Press C-Continue or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                if event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change

        draw_pattern()
        pygame.draw.rect(SCREEN, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()


