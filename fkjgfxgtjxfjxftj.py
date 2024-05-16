import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Chase Game")

# Set player properties
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size * 2
player_speed = 5

# Set zombie properties
zombie_size = 50
zombie_x = random.randint(0, screen_width - zombie_size)
zombie_y = random.randint(0, screen_height - zombie_size)
zombie_speed = 3

# Initialize player health
player_health = 100

# Load images
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (player_size, player_size))

zombie_img = pygame.image.load('zombie.png')
zombie_img = pygame.transform.scale(zombie_img, (zombie_size, zombie_size))

# Set clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed < screen_height - player_size:
        player_y += player_speed

    # Update zombie position
    if zombie_x < player_x:
        zombie_x += zombie_speed
    if zombie_x > player_x:
        zombie_x -= zombie_speed
    if zombie_y < player_y:
        zombie_y += zombie_speed
    if zombie_y > player_y:
        zombie_y -= zombie_speed

    # Check for collision
    if abs(player_x - zombie_x) < player_size and abs(player_y - zombie_y) < player_size:
        player_health -= 10
        zombie_x = random.randint(0, screen_width - zombie_size)
        zombie_y = random.randint(0, screen_height - zombie_size)

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw zombie
    screen.blit(zombie_img, (zombie_x, zombie_y))

    # Display player health
    font = pygame.font.SysFont('arial', 20)
    text = font.render("Health: " + str(player_health), True, RED)
    screen.blit(text, (screen_width - 150, 20))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
