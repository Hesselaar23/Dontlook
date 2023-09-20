import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Elemental Duel")

# Define player attributes with reduced speeds and size
player_size = 30
player1_x = 100
player1_y = screen_height // 2
player1_speed = 0.2  # Reduced speed

player2_x = screen_width - 100
player2_y = screen_height // 2
player2_speed = 0.2  # Reduced speed

# Define ability attributes
ability_size = 10
ability_speed = 0.5  # Adjusted ability speed
ability_cooldown = 2000  # Number of frames to wait before firing again
player1_cooldown = 0
player2_cooldown = 0

# Initialize ability positions
ability1_x = None
ability1_y = None
ability2_x = None
ability2_y = None

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= player1_speed
    if keys[pygame.K_s]:
        player1_y += player1_speed
    if keys[pygame.K_a]:
        player1_x -= player1_speed
    if keys[pygame.K_d]:
        player1_x += player1_speed

    # Player 2 controls (changed to "ijkl")
    if keys[pygame.K_i]:
        player2_y -= player2_speed
    if keys[pygame.K_k]:
        player2_y += player2_speed
    if keys[pygame.K_j]:
        player2_x -= player2_speed
    if keys[pygame.K_l]:
        player2_x += player2_speed

    # Boundary checks (prevent players from going off-screen)
    player1_x = max(0, min(screen_width - player_size, player1_x))
    player1_y = max(0, min(screen_height - player_size, player1_y))
    
    # Ensure that player 2 does not go off-screen or collide with player 1
    player2_x = max(0, min(screen_width - player_size, player2_x))
    player2_y = max(0, min(screen_height - player_size, player2_y))
    
    # Update ability cooldowns
    if player1_cooldown > 0:
        player1_cooldown -= 1
    if player2_cooldown > 0:
        player2_cooldown -= 1

    # Player 1 ability (fire when pressing "q" and cooldown is 0)
    if keys[pygame.K_q] and player1_cooldown == 0:
        player1_cooldown = ability_cooldown
        # Create an ability rectangle in the direction of player 2
        ability1_x = player1_x + player_size // 2 - ability_size // 2
        ability1_y = player1_y + player_size // 2 - ability_size // 2
        ability1_direction = (player2_x - player1_x, player2_y - player1_y)
        ability1_length = (ability1_direction[0] ** 2 + ability1_direction[1] ** 2) ** 0.5
        ability1_direction = (ability1_direction[0] / ability1_length, ability1_direction[1] / ability1_length)
        
    # Player 2 ability (fire when pressing "u" and cooldown is 0)
    if keys[pygame.K_u] and player2_cooldown == 0:
        player2_cooldown = ability_cooldown
        # Create an ability rectangle in the direction of player 1
        ability2_x = player2_x + player_size // 2 - ability_size // 2
        ability2_y = player2_y + player_size // 2 - ability_size // 2
        ability2_direction = (player1_x - player2_x, player1_y - player2_y)
        ability2_length = (ability2_direction[0] ** 2 + ability2_direction[1] ** 2) ** 0.5
        ability2_direction = (ability2_direction[0] / ability2_length, ability2_direction[1] / ability2_length)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw player characters
    pygame.draw.rect(screen, (255, 0, 0), (player1_x, player1_y, player_size, player_size))  # Player 1 in red
    pygame.draw.rect(screen, (0, 0, 255), (player2_x, player2_y, player_size, player_size))  # Player 2 in blue

    # Draw abilities
    if ability1_x is not None and ability1_y is not None:
        pygame.draw.rect(screen, (255, 0, 0), (ability1_x, ability1_y, ability_size, ability_size))  # Player 1's ability in red
        ability1_x += ability_speed * ability1_direction[0]
        ability1_y += ability_speed * ability1_direction[1]
        
    if ability2_x is not None and ability2_y is not None:
        pygame.draw.rect(screen, (0, 0, 255), (ability2_x, ability2_y, ability_size, ability_size))  # Player 2's ability in blue
        ability2_x += ability_speed * ability2_direction[0]
        ability2_y += ability_speed * ability2_direction[1]

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
