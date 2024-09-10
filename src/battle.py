import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, RED
import sys

# Function to render text
def render_text(text, font, color, pos, screen):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

# Battle screen display
def battle_screen(screen):
    print("DEBUG: Entering the Battle Screen") 
    font = pygame.font.SysFont(None, 36)
    running = True
    
    # Positions for the heroes
    team_a_positions = [(100, 100), (100, 200), (100, 300)]  # Left side for Team A
    team_b_positions = [(600, 100), (600, 200), (600, 300)]  # Right side for Team B
    
    while running:
        # background colour for the battle colosseum
        screen.fill(WHITE)
        
        ## Initial position for the heroes
        # Draw Team A Heroes
        for pos in team_a_positions:
            pygame.draw.rect(screen, GREEN, (*pos, 50, 50))  # (x, y, width, height)
            render_text("Hero A", font, BLACK, (pos[0], pos[1] - 30), screen)  # Hero label
        
        # Draw Team B Heroes
        for pos in team_b_positions:
            pygame.draw.rect(screen, RED, (*pos, 50, 50))  # (x, y, width, height)
            render_text("Hero B", font, BLACK, (pos[0], pos[1] - 30), screen)  # Hero label
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("DEBUG: Exiting the Battle screen")
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.update()