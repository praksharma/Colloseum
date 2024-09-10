import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from battle import battle_screen

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Colosseum Battle")

# Set up fonts
font = pygame.font.SysFont(None, 55)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Render welcome message for the main screen
def render_text(text, font, color, pos):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

# Main loop
def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        
        # Display Title
        render_text("Colosseum Simulator", font, BLACK, (150, 150))
        
        # Display Start Battle button
        start_button = pygame.Rect(300, 300, 250, 50)  # x, y, width, height
        pygame.draw.rect(screen, GREEN, start_button)
        render_text("Start Battle", font, BLACK, (320, 310))
        
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos): # Start Battle button clicked
                    print("DEBUG: Start Battle clicked")  # Placeholder for action
                    # Start the battle screen when button clicked
                    battle_screen(screen)
        
        # Update display
        pygame.display.update()

# Run the main menu
if __name__ == "__main__":
    main_menu()