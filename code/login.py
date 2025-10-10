import pygame
import sys

# Initialize Pygame
pygame.init()

def login():
    run = False
    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    button_color = (50, 150, 255)

    # Fonts
    font = pygame.font.Font(None, 36)

    # Button class
    class Button:
        def __init__(self, x, y, width, height, text, action=None):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.action = action

        def draw(self):
            pygame.draw.rect(screen, button_color, self.rect)
            text_surface = font.render(self.text, True, white)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    # Create buttons
    login_button = Button(300, 400, 200, 50, "Login", action="login")
    quit_button = Button(300, 500, 200, 50, "Quit", action="quit")

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for button in [login_button, quit_button]:
                        if button.rect.collidepoint(event.pos):
                            if button.action == "login":
                                print("Login button clicked!")
                                # Add your login logic here
                            elif button.action == "quit":
                                pygame.quit()
                                sys.exit()

        # Clear the screen
        screen.fill(black)

        # Draw buttons
        login_button.draw()
        quit_button.draw()

        # Refresh the screen
        pygame.display.update()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

