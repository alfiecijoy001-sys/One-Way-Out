import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("user input")

user_ip  =""
font=pygame.font.Font(None, 40)
text_box = pygame.Rect(75,75,100,50)
active = False
color = pygame.Colour("black")


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT():
            pygame.quit()
            quit()
        elif events.type == pygane.MOUSEBUTTON:
            if text_box.collidepoint(events.pos):
                active=True
            else:
                active=False
        elif events.type == pygame.KEYDOWN:
            if active:
                if events.key == pygame.K_BACKSPACE:
                    user_ip = user_ip[:-1]
                else:
                    user_ip += events.unicode
    screen.fill("blue")
    pygame.display.update()
            