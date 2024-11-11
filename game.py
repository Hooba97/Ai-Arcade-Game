import pygame
import sys
import random
import time

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collect Game")

# Colors and font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
GOLD = (255, 215, 0)
DARK_BLUE = (0, 0, 150)
RED = (255, 0, 0)

font = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

# Game states
MENU, GAME, HOW, CONFIRM_EXIT = "menu", "game", "How To Play", "confirm_exit"
game_state = MENU

# Player properties
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 40
player_color = BLUE
player_speed = 10  # Slightly increased for smoother movement

# Coin properties
coin_radius = 20
coin_pos = [random.randint(coin_radius, WIDTH - coin_radius), random.randint(coin_radius, HEIGHT - coin_radius)]

# Score, level system, and difficulty
score = 0
level = 1
coins_needed_for_level_up = [5, 7, 9, 11]  # Coins required to level up
coins_collected = 0  # Tracking coins collected for level progression
timer = 30
last_timer_update = time.time()  # Timer update reference
obstacle_walls = []

# Menu options
menu_options = ["Start Game", "How To Play", "Exit"]
selected_option = 0

coin_sound = pygame.mixer.Sound("coin_collect.wav")


# Helper function to create a wall of obstacles
def create_wall():
    wall_length = random.randint(1, 2)  # Smaller wall size
    orientation = random.choice(["horizontal", "vertical"])
    start_x = random.randint(0, WIDTH - 25 * wall_length)
    start_y = random.randint(0, HEIGHT - 25 * wall_length)

    wall = []
    for i in range(wall_length):
        if orientation == "horizontal":
            wall.append(pygame.Rect(start_x + i * 50, start_y, 40, 40))  # Smaller wall
        else:
            wall.append(pygame.Rect(start_x, start_y + i * 50, 40, 40))  # Smaller wall
    return wall

# Initial wall for the first level
obstacle_walls.append(create_wall())

# Main game loop
clock = pygame.time.Clock()

def reset_game():
    global player_pos, score, coins_collected, timer, level, obstacle_walls
    player_pos = [WIDTH // 2, HEIGHT // 2]
    score = 0
    coins_collected = 0
    timer = 30
    level = 1
    obstacle_walls = [create_wall()]

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_state == MENU:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        reset_game()
                        game_state = GAME
                    elif selected_option == 2:
                        game_state = HOW
                    elif selected_option == 3:
                        pygame.quit()
                        sys.exit()
            elif game_state == GAME:
                if event.key == pygame.K_ESCAPE:
                    game_state = CONFIRM_EXIT
            elif game_state == HOW:
                if event.key == pygame.K_ESCAPE:
                    game_state = MENU
            elif game_state == CONFIRM_EXIT:
                if event.key == pygame.K_y:  # Yes to confirm exit
                    game_state = MENU
                elif event.key == pygame.K_n:  # No to cancel
                    game_state = GAME

    if game_state == MENU:
        # Display menu
        for i, option in enumerate(menu_options):
            color = DARK_BLUE if i == selected_option else BLACK
            text_surface = font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100 + i * 60))
            screen.blit(text_surface, text_rect)

    elif game_state == HOW:
        # Display the How To Play screen text
        screen.fill(WHITE)
        HOW_text = [
            "Coin Collect Game",
            "Use the arrow keys to collect coins.",
            "Avoid obstacles and level up every few coins.",
            "Press ESC to return to the menu."
        ]
        for i, line in enumerate(HOW_text):
            text_surface = font_small.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - 200, HEIGHT // 3 + i * 40))

    elif game_state == GAME:
        screen.fill(BLACK)

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
            player_pos[1] += player_speed

        # Draw player
        pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

        # Draw coin
        pygame.draw.circle(screen, GOLD, coin_pos, coin_radius)
        dollar_sign = font_small.render("$", True, BLACK)
        dollar_sign_rect = dollar_sign.get_rect(center=(coin_pos[0], coin_pos[1]))
        screen.blit(dollar_sign, dollar_sign_rect)

        # Draw obstacle walls
        for wall in obstacle_walls:
            for segment in wall:
                pygame.draw.rect(screen, RED, segment)

        # Collision with coin
        player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
        coin_rect = pygame.Rect(coin_pos[0] - coin_radius, coin_pos[1] - coin_radius, coin_radius * 2, coin_radius * 2)
        if player_rect.colliderect(coin_rect):
            score += 1
            coins_collected += 1
            coin_sound.play()  # Play sound when coin is collected
            coin_pos = [random.randint(coin_radius, WIDTH - coin_radius), random.randint(coin_radius, HEIGHT - coin_radius)]
            timer += 1  # Increase timer by 1 seconds

            # Increase difficulty every level
            if coins_collected >= sum(coins_needed_for_level_up[:level]):
                level += 1
                obstacle_walls.append(create_wall())  # Add a new wall for each level

        # Collision with obstacles
        for wall in obstacle_walls:
            for segment in wall:
                if player_rect.colliderect(segment):
                    player_pos = [WIDTH // 2, HEIGHT // 2]  # Reset player to center

        # Timer update every second
        if time.time() - last_timer_update >= 1:
            timer -= 1
            last_timer_update = time.time()
            if timer <= 0:
                game_state = MENU  # Return to menu if time is up

        # Display score, level, and coins to next level
        score_text = font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        level_text = font_small.render(f"Level: {level}", True, WHITE)
        screen.blit(level_text, (WIDTH - 150, 10))

        # Show the score required for the next level
        score_required = sum(coins_needed_for_level_up[:level])
        score_text = font_small.render(f"Score to Next Level: {score_required}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT - 40))

    elif game_state == CONFIRM_EXIT:
        screen.fill(WHITE)
        confirm_text = font_small.render("Are you sure you want to exit? (Y/N)", True, BLACK)
        screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)  # Limit the game to 60 frames per second
