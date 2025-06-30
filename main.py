# main.py
import pygame
import sys
import time
import random
from maze_generator import generate_maze_with_path

# Game settings
WIDTH, HEIGHT = 600, 650  # Extra space on top for UI
ROWS, COLS = 20, 20
TILE_SIZE = WIDTH // COLS
UI_HEIGHT = HEIGHT - WIDTH

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 135, 245)    # Player color
GREEN = (34, 177, 76)     # Goal color
GRAY = (200, 200, 200)    # Grid color
RED = (200, 0, 0)         # Obstacle lines

# Pygame setup
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 22)

# Game state initialization
maze, path = generate_maze_with_path(ROWS, COLS)
player_pos = [0, 0]
goal_pos = random.choice(path[1:])  # Choose goal from the path, not the start
start_time = time.time()
move_count = 0
game_over = False

def draw_path():
    # Dotted line path for guidance (optional visual aid)
    for i, (r, c) in enumerate(path):
        if [r, c] not in ([0, 0], goal_pos) and i % 2 == 0:
            dot_rect = pygame.Rect(
                c * TILE_SIZE + TILE_SIZE // 3,
                r * TILE_SIZE + UI_HEIGHT + TILE_SIZE // 3,
                TILE_SIZE // 3, TILE_SIZE // 3
            )
            pygame.draw.rect(win, (180, 180, 255), dot_rect)

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE + UI_HEIGHT, TILE_SIZE, TILE_SIZE)
            cell = maze[row][col]
            if cell == 1:  # Wall
                pygame.draw.rect(win, BLACK, rect)
            elif cell == 2:  # Obstacle (draw red dotted lines)
                pygame.draw.rect(win, WHITE, rect)
                for i in range(0, TILE_SIZE, 6):
                    pygame.draw.line(
                        win, RED,
                        (col * TILE_SIZE + i, row * TILE_SIZE + UI_HEIGHT + i),
                        (col * TILE_SIZE + i + 2, row * TILE_SIZE + UI_HEIGHT + i + 2),
                        1
                    )
            else:  # Empty space
                pygame.draw.rect(win, WHITE, rect)
            pygame.draw.rect(win, GRAY, rect, 1)  # Grid lines

def draw_player():
    rect = pygame.Rect(player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE + UI_HEIGHT, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(win, BLUE, rect)

def draw_goal():
    rect = pygame.Rect(goal_pos[1] * TILE_SIZE, goal_pos[0] * TILE_SIZE + UI_HEIGHT, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(win, GREEN, rect)

def draw_ui():
    pygame.draw.rect(win, (240, 240, 240), (0, 0, WIDTH, UI_HEIGHT))
    elapsed = int(time.time() - start_time)

    # Display move count, timer, and instructions
    win.blit(font.render(f"Moves: {move_count}", True, BLACK), (10, 10))
    win.blit(font.render(f"Time: {elapsed}s", True, BLACK), (220, 10))
    win.blit(font.render("Press R to Restart | Q to Quit", True, BLACK), (400, 10))

    if game_over:
        win.blit(font.render("You Reached the Goal!", True, RED), (WIDTH // 2 - 120, 40))

def move_player(d_row, d_col):
    global move_count, game_over
    new_row = player_pos[0] + d_row
    new_col = player_pos[1] + d_col
    if 0 <= new_row < ROWS and 0 <= new_col < COLS:
        if maze[new_row][new_col] == 0:
            player_pos[0], player_pos[1] = new_row, new_col
            move_count += 1
        if [new_row, new_col] == goal_pos:
            game_over = True

def reset_game():
    global maze, path, player_pos, goal_pos, move_count, game_over, start_time
    maze, path = generate_maze_with_path(ROWS, COLS)
    player_pos = [0, 0]
    goal_pos = random.choice(path[1:])
    move_count = 0
    game_over = False
    start_time = time.time()

def game_loop():
    while True:
        win.fill(WHITE)
        draw_ui()
        draw_maze()
        draw_path()
        draw_goal()
        draw_player()

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_LEFT:
                        move_player(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        move_player(0, 1)
                    elif event.key == pygame.K_UP:
                        move_player(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        move_player(1, 0)
                if event.key == pygame.K_r:
                    reset_game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

game_loop()