import pygame
import button

clock=pygame.time.Clock()

# Setup the display
screen_width = 800
screen_height = 598
screen = pygame.display.set_mode((screen_width, screen_height))

one_btn_img=pygame.image.load("code/one_btn.png").convert()
two_btn_img=pygame.image.load("code/two_btn.png").convert()
three_btn_img=pygame.image.load("code/three_btn.png").convert()
four_btn_img=pygame.image.load("code/four_btn.png").convert()
five_btn_img=pygame.image.load("code/five_btn.png").convert()
six_btn_img=pygame.image.load("code/six_btn.png").convert()
seven_btn_img=pygame.image.load("code/seven_btn.png").convert()
eight_btn_img=pygame.image.load("code/eight_btn.png").convert()
nine_btn_img=pygame.image.load("code/nine_btn.png").convert()

      
#button instance
one_button=button.Button(110, 140, one_btn_img, 1.0)
two_button=button.Button(340, 140, two_btn_img, 1.0)
three_button=button.Button(550, 140, three_btn_img, 1.0)
four_button=button.Button(110, 310, four_btn_img, 1.0)
five_button=button.Button(340, 310, five_btn_img, 1.0)
six_button=button.Button(550, 310, six_btn_img, 1.0)
seven_button=button.Button(110, 480, seven_btn_img, 1.0)
eight_button=button.Button(340, 480, eight_btn_img, 1.0)
nine_button=button.Button(550, 480, nine_btn_img, 1.0)

pregame_music=None

def do_pregame_music(started):
    global pregame_music
    if started and pregame_music is None:
        pregame_music = pygame.mixer.Sound('sounds/pregame_music.mp3')
        #pregame_music.set_volume(0)
        #pregame_music.play()
    elif not started and pregame_music is not None:
        pregame_music.stop()
        
def stop_music():
    global pregame_music
    if pregame_music is not None:
        pregame_music.stop()
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
        level_bg = pygame.image.load("code/LevelScreen.png")
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
        
