# Import librarys
import pygame
from main import playing_instance
import sys
import button
import sqlite3
import time
from player import Player







# Set up colors
# Colors
white = (255, 255, 255)
blue = (0, 0, 139)
black = (0,0,0)
red = (255,0,0)
button_color = (93, 63, 211)

pygame.init() # Start Pygame
clock = pygame.time.Clock() # Initialise the clock

# Setup the display
screen_width = 800
screen_height = 598
screen = pygame.display.set_mode((screen_width, screen_height))



# Set up fonts
font = pygame.font.Font(None, 36)

text_font = pygame.font.SysFont(None, 45)
play_btn_img = pygame.image.load("play_btn.png").convert()
settings_btn_img = pygame.image.load("settings_btn.png").convert()
leaderboard_btn_img = pygame.image.load("leaderboard_btn.png").convert()
create_btn_img=pygame.image.load("create_btn.png").convert()
login_btn_img=pygame.image.load("login_btn.png").convert()
one_btn_img=pygame.image.load("one_btn.png").convert()
two_btn_img=pygame.image.load("two_btn.png").convert()
three_btn_img=pygame.image.load("three_btn.png").convert()
four_btn_img=pygame.image.load("four_btn.png").convert()
five_btn_img=pygame.image.load("five_btn.png").convert()
six_btn_img=pygame.image.load("six_btn.png").convert()
seven_btn_img=pygame.image.load("seven_btn.png").convert()
eight_btn_img=pygame.image.load("eight_btn.png").convert()
nine_btn_img=pygame.image.load("nine_btn.png").convert()

      
#button instance
play_button = button.Button(320, 200, play_btn_img, 0.18)
settings_button = button.Button(320, 330, settings_btn_img, 0.18)
leaderboard_button = button.Button(320, 460, leaderboard_btn_img, 0.18)
create_button = button.Button(320, 460, create_btn_img, 0.18)
loginn_button = button.Button(320, 460, login_btn_img, 0.18)
one_button=button.Button(110, 140, one_btn_img, 1.0)
two_button=button.Button(340, 140, two_btn_img, 1.0)
three_button=button.Button(550, 140, three_btn_img, 1.0)
four_button=button.Button(110, 310, four_btn_img, 1.0)
five_button=button.Button(340, 310, five_btn_img, 1.0)
six_button=button.Button(550, 310, six_btn_img, 1.0)
seven_button=button.Button(110, 480, seven_btn_img, 1.0)
eight_button=button.Button(340, 480, eight_btn_img, 1.0)
nine_button=button.Button(550, 480, nine_btn_img, 1.0)


def do_pregame_music(started):
    global pregame_music
    if started and pregame_music is None:
        pregame_music = pygame.mixer.Sound('../sounds/pregame_music.mp3')
        pregame_music.play()
    elif not started and pregame_music is not None:
        pregame_music.stop()
        
def stop_music():
    global pregame_music
    if pregame_music is not None:
        pregame_music.stop()
    
    

        
#draw function      
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
        
#the login button clicked on login option screen
def login_login():
        
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
                return "login_option"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if user_input_box.collidepoint(event.pos):
                    user_input_active = True
                    password_input_active=False
                elif password_input_box.collidepoint(event.pos):
                    password_input_active = True
                    user_input_active=False
                    print(password_input_active)
                elif loginn_button.rect.collidepoint(event.pos):
                        print("Attempted to login")
                        conn=sqlite3.connect("account.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM account_info WHERE Username=? and Password=?", (user_input_text, password_input_text))
                        row=cursor.fetchone()
                        if row:
                            print("Success")
                            draw_text("Logged in successfully!", font, (255, 225, 200), 170, 350)
                            pygame.display.update()
                            clock.tick(60)
                            time.sleep(1)
                            return "success"
                        else:
                            print("Failed")
                            draw_text("Login Failed!", font, (255, 225, 200), 170, 350)
                            pygame.display.update()
                            clock.tick(60)
                            time.sleep(1)
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
        screen.fill(red)
        draw_text("LOGIN", text_font, (0, 0, 0), 370, 50)
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
        loginn_button.draw(screen)

        pygame.display.update()
        clock.tick(60)
        
#create button clicked on login screen      
def create_account():
        
    # Set up input box
    user_input_box = pygame.Rect(300, 200, 200, 32)
    user_input_text = ""
    password_input_box = pygame.Rect(300, 240, 200, 32)
    password_input_text = ""
    user_input_active = False
    password_input_active=False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "login_option"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if user_input_box.collidepoint(event.pos):
                    user_input_active = True
                    password_input_active=False
                elif password_input_box.collidepoint(event.pos):
                    password_input_active = True
                    user_input_active=False
                    print(password_input_active)
                    
                elif create_button.rect.collidepoint(event.pos):
                    print("Account created")
                    conn=sqlite3.connect("account.db")

                    #create the customer details table
                    conn.execute('''CREATE TABLE  IF NOT EXISTS account_info(Username TEXT, Password TEXT, time INTEGER);''')
        
                    conn.execute("INSERT INTO account_info (Username, Password, time) \
                        VALUES (?, ?,?)",(user_input_text, password_input_text,vTime));

                    conn.commit()

                else:
                    user_input_active = False
                    password_input_active=False
            elif event.type == pygame.KEYDOWN:
                if user_input_active:
                    if event.key == pygame.K_RETURN:
                        print(user_input_text)
                    elif event.key == pygame.K_BACKSPACE:
                        user_input_text = user_input_text[:-1]
                    else:
                        user_input_text += event.unicode
                        
                elif password_input_active:
                    if event.key == pygame.K_RETURN:
                        print(password_input_text)
                    elif event.key == pygame.K_BACKSPACE:
                        password_input_text = password_input_text[:-1]
                    else:
                        password_input_text += event.unicode
        screen.fill(blue)
        draw_text("CREATE", text_font, (255, 255, 255), 370, 50)
        # Render username input box
        pygame.draw.rect(screen, white, user_input_box, 3)
        text_surface_user = font.render(user_input_text, True, black)
        width_user = max(100, text_surface_user.get_width() + 20)
        user_input_box.w = width_user
        screen.blit(text_surface_user, (user_input_box.x + 10, user_input_box.y + 5))
        draw_text("Username:", font, (255, 255, 255), 150, 205)
        

        # Render password input box
        pygame.draw.rect(screen, white, password_input_box, 3)
        text_surface_password = font.render(password_input_text, True, black)
        width_password = max(100, text_surface_password.get_width() + 20)
        password_input_box.w = width_password
        screen.blit(text_surface_password, (password_input_box.x + 10, password_input_box.y + 5))
        draw_text("Password:", font, (255, 255, 255), 150, 245)
        vTime=int(0)
        create_button.draw(screen)
        pygame.display.update()
        clock.tick(60)

# Function for the splash screen
def splash():
    # Main Loop
    while True:
        # Make the clock tick
        clock.tick(60)

        # Set the background colour
        screen.fill(pygame.Color("Purple"))
        
        draw_text("Exited game", text_font, (0, 0, 0), 350, 300)
        
        # Refresh the screen     
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return "mainGame"
#maingame function
def mainGame():
    while True:
        clock.tick(60)
        
        # Load background image
        bg = pygame.image.load("MainScreen.png")
        bg = pygame.transform.scale(bg, (800, 600))
        
        # Loop through the events that have occurred
        # since the last cycle
        for event in pygame.event.get():
            # Quit (x is clicked)
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    play_button.clicked = True
                    print("Play Button Clicked")
                    return "login"
                elif settings_button.rect.collidepoint(pygame.mouse.get_pos()):
                    settings_button.clicked = True
                    print("Settings Button Clicked")
                elif leaderboard_button.rect.collidepoint(pygame.mouse.get_pos()):
                    leaderboard_button.clicked = True
                    print("Leaderboard Button Clicked")
                    
            
            
        # Refresh the screen     
        screen.blit(bg, (0, 0))
        play_button.draw(screen)
        settings_button.draw(screen)
        leaderboard_button.draw(screen)
        pygame.display.update()
        
#intital screen
def init_screen():
    do_pregame_music(started)
    while True:
        clock.tick(60)
        # Load background image
        bg = pygame.image.load("MainScreen.png")
        bg = pygame.transform.scale(bg, (800, 600))
            
        # Loop through the events that have occurred
        # since the last cycle
        for event in pygame.event.get():
            # Quit (x is clicked)
            if event.type == pygame.QUIT:
                return "quit"
                #pygame.quit()
            elif event.type == pygame.KEYDOWN:
                print("HERE")
                return "mainGame"
                
           
        screen.blit(bg, (0, 0))
        draw_text("Press any key to continue", text_font, (250, 250, 250), 200, 420)
        # Refresh the screen     
        pygame.display.update()

# Login Screen with options
def login_option():
    run = False  
    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Colors
    white = (255, 255, 255)
    blue = (0, 0, 139)
    button_color = (93, 63, 211)

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
    login_button = Button(250, 300, 300, 50, "Login", action="login")
    create_button = Button(250, 400, 300, 50, "Create", action="create")
    quit_button = Button(250, 500, 300, 50, "Quit", action="quit")

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for button in [login_button, create_button, quit_button]:
                        if button.rect.collidepoint(event.pos):
                            if button.action == "login":
                                print("Login button clicked")
                                return"login_login"
                                
                                
                            elif button.action == "create":
                                print("Create button clicked")
                                return"create_account"
                            elif button.action == "quit":
                                return "mainGame"
                                print("Login exited")

        # Clear the screen
        screen.fill(blue)
        draw_text("Login to your account OR Create a new one", text_font, (255, 255, 255), 100, 50)
        draw_text("to save your progress", text_font, (255, 255, 255), 100, 80)
        # Draw buttons
        login_button.draw()
        create_button.draw()
        quit_button.draw()

        # Refresh the screen
        pygame.display.update()

        # Cap the frame rate
        pygame.time.Clock().tick(60)


   
   
   
def levelscreen():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if one_button.rect.collidepoint(event.pos):
                    print("1st level")
                    stop_music()  
                    return "first_level"
                    started = False
                    do_pregame_music(started)
                    
                        
                elif two_button.rect.collidepoint(event.pos):
                    print("2nd level")
                    stop_music()
                    return "second_level"
                    started = False
                    do_pregame_music(started)
                
                elif three_button.rect.collidepoint(event.pos):
                    print("3rd level")
                    stop_music()
                    return "third_level"
                    started = False
                    do_pregame_music(started)
                elif four_button.rect.collidepoint(event.pos):
                    print("4th level")
                    stop_music()
                    return "fourth_level"
                    started = False
                    do_pregame_music(started)
                elif five_button.rect.collidepoint(event.pos):
                    print("5th level")
                    stop_music()
                    return "fifth_level"
                    started = False
                    do_pregame_music(started)
            
        # Load background image
        level_bg = pygame.image.load("LevelScreen.png")
        level_bg = pygame.transform.scale(level_bg, (800, 600))
        screen.blit(level_bg, (0, 0))
        print("Level screen")
        one_button.draw(screen)
        two_button.draw(screen)
        three_button.draw(screen)
        four_button.draw(screen)
        five_button.draw(screen)
        six_button.draw(screen)
        seven_button.draw(screen)
        eight_button.draw(screen)
        nine_button.draw(screen)
        # Refresh the screen
        pygame.display.update()
    

    
    
    
    


#start application

died=False
started=True
pregame_music = None
play_button.clicked = False
settings_button.clicked = False
leaderboard_button.clicked = False
one_button.clicked = False
two_button.clicked = False
state = "splash"
running = True

while running:
    if state=="quit":
        state=splash()
    elif state=="splash":
        state=init_screen()
    elif state=="mainGame":
        state=mainGame()
    elif state == "login":
        state = login_option()
    elif state == "login_option":
        state=login_option()
    elif state == "login_login":
        state=login_login()
    elif state == "create_account":
        state=create_account()
    elif state == "success":   #logged in successfully
        state=levelscreen()
    elif state == "first_level":
        state= playing_instance.game_run_0()
    elif state == "second_level":
        state= playing_instance.game_run_1()
    elif state == "third_level":
        state= playing_instance.game_run_2()
    elif state == "fourth_level":
        state= playing_instance.game_run_3()
    elif state == "fifth_level":
        state= playing_instance.game_run_4()
        
pygame.quit()
sys.exit()





