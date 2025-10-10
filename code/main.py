import pygame, sys
from settings1 import *
from game_data import level_0, level_1, level_2, level_3, level_4
from level1 import Level
from player import Player
from ui import UI
from collision_detection import end_collision
import button
from levelscreen import levelscreen, stop_music, do_pregame_music
#PYGAME SETUP 
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((screen_width,screen_height))


pause_btn_img=pygame.image.load("code/pause_btn.png")
pause_button=button.Button(750, 20, pause_btn_img, 0.18)

quit_btn_img=pygame.image.load("code/quit_btn.png")
quit_button=button.Button(315, 350, quit_btn_img, 0.18)

restart_btn_img=pygame.image.load("code/restart_btn.png").convert()
restart_button=button.Button(315, 150, restart_btn_img, 0.18)

#level0= Level(level_0, screen, key_change)
#level1= Level(level_1, screen, key_change)
#level2= Level(level_2, screen, key_change)
dark_navy="#0e0b2e"

class playing:
    def __init__(self):
        #attributes
        self.max_health = 100
        self.current_health = 100
        self.keys = 0
        
        #sound
        self.level_music = pygame.mixer.Sound('sounds/level_music.mp3')
        
        #ui
        self.ui=UI(screen)
        
        # player
        #self.player = Player((0, 0), self.health_change)
        # Load and scale the image
        
        
    def key_change(self, amount):
        self.keys += amount
    
    def player_died(self):
        if self.current_health <= 0:
            self.current_health = 100
            self.keys = 0
            return True  # Indicates player died
        
            
        
    def health_change(self, amount):
        self.current_health += amount

    def restart_game(self, level):
        if level == 0:
            self.game_run_0()
        elif level == 1:
            self.game_run_1()
        elif level == 2:
            self.game_run_2()
        elif level == 3:
            self.game_run_3()
        elif level == 4:
            self.game_run_4()


    def game_run_0(self):
        self.current_health = 100
        self.keys = 0
        self.level_music.stop()
        level0 = Level(level_0, screen, self.key_change, self.health_change)
        self.level_music.play(loops=-1)
        running = True
        paused = False  # Flag to indicate whether the game is paused
        
        
        pause_bg = pygame.image.load("code/PauseScreen.png")
        pause_bg = pygame.transform.scale(pause_bg, (800, 600))
        pause_bg.set_alpha(5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.rect.collidepoint(event.pos):
                        paused = not paused
                    elif quit_button.rect.collidepoint(event.pos):
                        levelscreen()
                    elif restart_button.rect.collidepoint(event.pos):
                        self.restart_game(0)  # Restart level 0
                        
                    

            if not paused:  # Only run the level if the game is not paused
                screen.fill(dark_navy)
                level0.run()
                pause_button.draw(screen)
                self.ui.health(self.current_health, self.max_health)
                self.ui.keys_show(self.keys)

                if self.player_died():
                    self.level_music.stop()
                    self.restart_game(0)  # Restart level 0
            else:
                pause_button.draw(screen)
                screen.blit(pause_bg,(0,0))
                quit_button.draw(screen)
                restart_button.draw(screen)
                print("paused")
                            
            
            clock.tick(60)
            pygame.display.update()


            
                

    def game_run_1(self):
        self.current_health = 100
        self.keys = 0
        self.level_music.stop()
        level1 = Level(level_1, screen, self.key_change, self.health_change)
        self.level_music.play(loops=-1)
        running = True
        paused = False  # Flag to indicate whether the game is paused
        pause_bg = pygame.image.load("code/PauseScreen.png")
        pause_bg = pygame.transform.scale(pause_bg, (800, 600))
        pause_bg.set_alpha(5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.rect.collidepoint(event.pos):
                        paused = not paused
                        
                    elif quit_button.rect.collidepoint(event.pos):
                        levelscreen()
                        
                    elif restart_button.rect.collidepoint(event.pos):
                        self.restart_game(1)  # Restart level 1
                        
                    

            if not paused:  # Only run the level if the game is not paused
                screen.fill(dark_navy)
                level1.run()
                pause_button.draw(screen)
                self.ui.health(self.current_health, self.max_health)
                self.ui.keys_show(self.keys)

                if self.player_died():
                    self.level_music.stop()
                    self.restart_game(1)  # Restart level 1
            else:
                pause_button.draw(screen)
                screen.blit(pause_bg,(0,0))
                quit_button.draw(screen)
                restart_button.draw(screen)
                print("paused")
                            
            
            clock.tick(60)
            pygame.display.update()


    def game_run_2(self):
        self.current_health = 100
        self.keys = 0
        self.level_music.stop()
        level2 = Level(level_2, screen, self.key_change, self.health_change)
        self.level_music.play(loops=-1)
        running = True
        paused = False  # Flag to indicate whether the game is paused
        
        
        pause_bg = pygame.image.load("PauseScreen.png")
        pause_bg = pygame.transform.scale(pause_bg, (800, 600))
        pause_bg.set_alpha(5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.rect.collidepoint(event.pos):
                        paused = not paused
                        
                    elif quit_button.rect.collidepoint(event.pos):
                        levelscreen()
                        
                    elif restart_button.rect.collidepoint(event.pos):
                        self.restart_game(2)  # Restart level 2
                        
                    

            if not paused:  # Only run the level if the game is not paused
                screen.fill(dark_navy)
                level2.run()
                pause_button.draw(screen)
                self.ui.health(self.current_health, self.max_health)
                self.ui.keys_show(self.keys)

                if self.player_died():
                    self.level_music.stop()
                    self.restart_game(2)  # Restart level 2
            else:
                pause_button.draw(screen)
                screen.blit(pause_bg,(0,0))
                quit_button.draw(screen)
                restart_button.draw(screen)
                print("paused")
                            
            
            clock.tick(60)
            pygame.display.update()

    
    def game_run_1(self):
        self.current_health = 100
        self.keys = 0
        self.level_music.stop()
        level3 = Level(level_3, screen, self.key_change, self.health_change)
        self.level_music.play(loops=-1)
        running = True
        paused = False  # Flag to indicate whether the game is paused
        
        
        pause_bg = pygame.image.load("PauseScreen.png")
        pause_bg = pygame.transform.scale(pause_bg, (800, 600))
        pause_bg.set_alpha(5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.rect.collidepoint(event.pos):
                        paused = not paused
                        
                    elif quit_button.rect.collidepoint(event.pos):
                        levelscreen()
                        
                    elif restart_button.rect.collidepoint(event.pos):
                        self.restart_game(3)  # Restart level 3
                        
                    

            if not paused:  # Only run the level if the game is not paused
                screen.fill(dark_navy)
                level3.run()
                pause_button.draw(screen)
                self.ui.health(self.current_health, self.max_health)
                self.ui.keys_show(self.keys)

                if self.player_died():
                    self.level_music.stop()
                    self.restart_game(3)  # Restart level 3
            else:
                pause_button.draw(screen)
                screen.blit(pause_bg,(0,0))
                quit_button.draw(screen)
                restart_button.draw(screen)
                print("paused")
                            
            
            clock.tick(60)
            pygame.display.update()

            
    def game_run_4(self):
        self.current_health = 100
        self.keys = 0
        self.level_music.stop()
        level4 = Level(level_4, screen, self.key_change, self.health_change)
        self.level_music.play(loops=-1)
        running = True
        paused = False  # Flag to indicate whether the game is paused
        
        
        pause_bg = pygame.image.load("PauseScreen.png")
        pause_bg = pygame.transform.scale(pause_bg, (800, 600))
        pause_bg.set_alpha(5)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.rect.collidepoint(event.pos):
                        paused = not paused
                        
                    elif quit_button.rect.collidepoint(event.pos):
                        levelscreen()
                        
                    elif restart_button.rect.collidepoint(event.pos):
                        self.restart_game(4)  # Restart level 4
                        
                    

            if not paused:  # Only run the level if the game is not paused
                screen.fill(dark_navy)
                level4.run()
                pause_button.draw(screen)
                self.ui.health(self.current_health, self.max_health)
                self.ui.keys_show(self.keys)

                if self.player_died():
                    self.level_music.stop()
                    self.restart_game(4)  # Restart level 4
            else:
                pause_button.draw(screen)
                screen.blit(pause_bg,(0,0))
                quit_button.draw(screen)
                restart_button.draw(screen)
                print("paused")
                            
            
            clock.tick(60)
            pygame.display.update()


playing_instance = playing()