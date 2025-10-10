import pygame
import sys

pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up input box
user_input_box = pygame.Rect(300, 200, 200, 32)
user_input_text = ''
password_input_box = pygame.Rect(300, 240, 200, 32)
password_input_text = ''
user_input_active = False
password_input_active=False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if user_input_box.collidepoint(event.pos):
                user_input_active = True
                password_input_active=False
            elif password_input_box.collidepoint(event.pos):
                password_input_active = True
                user_input_active=False
                print(password_input_active)
            else:
                user_input_active = False
                password_input_active=False
        elif event.type == pygame.KEYDOWN:
            if user_input_active:
                if event.key == pygame.K_RETURN:
                    print(user_input_text)
                    user_input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input_text = user_input_text[:-1]
                else:
                    user_input_text += event.unicode
                    
            elif password_input_active:
                if event.key == pygame.K_RETURN:
                    print(password_input_text)
                    password_input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    password_input_text = password_input_text[:-1]
                else:
                    password_input_text += event.unicode
    screen.fill(white)

    # Render username input box
    pygame.draw.rect(screen, black, user_input_box, 3)
    text_surface_user = font.render(user_input_text, True, black)
    width_user = max(100, text_surface_user.get_width() + 20)
    user_input_box.w = width_user
    screen.blit(text_surface_user, (user_input_box.x + 10, user_input_box.y + 5))
    draw_text("Username:", font, (0, 0, 0), 150, 205)

    # Render password input box
    pygame.draw.rect(screen, black, password_input_box, 3)
    text_surface_password = font.render(password_input_text, True, black)
    width_password = max(100, text_surface_password.get_width() + 20)
    password_input_box.w = width_password
    screen.blit(text_surface_password, (password_input_box.x + 10, password_input_box.y + 5))
    draw_text("Password:", font, (0, 0, 0), 150, 245)

    pygame.display.update()
    clock.tick(30)
