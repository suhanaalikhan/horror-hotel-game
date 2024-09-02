import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
JUMPSCARE_COLOR = (255, 255, 255)
JUMPSCARE_INTERVAL = 10  # Time in seconds between jumpscares

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Horror Hotel")

# Load assets
player_image = pygame.image.load('player.png')  # Replace with your image path
jumpscare_image = pygame.image.load('jumpscare.png')  # Replace with your image path

# Game setup
player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
player_size = 50
player_speed = 5

# Function to display jumpscare
def display_jumpscare():
    window.blit(jumpscare_image, (0, 0))
    pygame.display.update()
    pygame.time.delay(500)  # Jumpscare display time

# Game loop
clock = pygame.time.Clock()
last_jumpscare_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Update display
    window.fill(BACKGROUND_COLOR)
    window.blit(player_image, (player_pos[0], player_pos[1]))

    # Check for jumpscare
    current_time = time.time()
    if current_time - last_jumpscare_time > JUMPSCARE_INTERVAL:
        display_jumpscare()
        last_jumpscare_time = current_time

    pygame.display.update()
    clock.tick(30)  # FPS

pygame.quit()
