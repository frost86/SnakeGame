import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Set window dimensions
width = 600
height = 400
game_window = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption('Snake Game')

# Set clock speed (FPS)
clock = pygame.time.Clock()

# Snake properties
snake_block = 10  # Size of the snake segments
snake_speed = 15  # Movement speed of the snake

# Define the snake
def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_window, green, [segment[0], segment[1], snake_block, snake_block])

# Display the score
def display_score(score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])

# Random food position
def random_food_position():
    return (random.randrange(0, width - snake_block) // 10 * 10, 
            random.randrange(0, height - snake_block) // 10 * 10)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0
    snake_list = []
    length_of_snake = 1

    # Initial food position
    food_x, food_y = random_food_position()

    while not game_over:

        # Handle game over screen
        while game_close:
            game_window.fill(black)
            font = pygame.font.SysFont(None, 50)
            message = font.render("Game Over! Press Q to Quit or C to Play Again", True, red)
            game_window.blit(message, [width // 8, height // 3])
            pygame.display.update()

            # Check for restart or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handle snake movement and input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Check for collision with walls
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change

        # Update the game window
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [food_x, food_y, snake_block, snake_block])

        # Update snake position
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake and display score
        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x, food_y = random_food_position()
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()