import pygame, sys
from settings1 import *
from game_data import level_0, level_1, level_2, level_3, level_4
from level1 import Level
from player import Player
from ui import UI
from collision_detection import end_collision

#PYGAME SETUP 
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((screen_width,screen_height))

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
        self.level_music = pygame.mixer.Sound('../sounds/level_music.mp3')
        
        #ui
        self.ui=UI(screen)
        
        # player
        self.player = Player((0, 0), self.health_change)            
        
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
        level0 = Level(level_0, screen, self.key_change, self.health_change)
        self.level_music.play(loops = -1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(dark_navy)
            level0.run()
            self.ui.health(self.current_health, self.max_health)
            self.ui.keys_show(self.keys)

            if self.player_died():
                self.level_music.stop()
                self.restart_game(0)  # Restart level 0

            # Call end_collision function
            end_collision(self.player, level0.goal)
                

            clock.tick(60)
            pygame.display.update()

    def game_run_1(self):
        level1 = Level(level_1, screen, self.key_change, self.health_change)
        self.level_music.play(loops = -1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(dark_navy)
            level1.run()
            self.level_music.play()
            self.ui.health(self.current_health, self.max_health)
            self.ui.keys_show(self.keys)

            if self.player_died():
                self.level_music.stop()
                self.restart_game(1)  # Restart level 1

            clock.tick(60)
            pygame.display.update()

    def game_run_2(self):
        level2 = Level(level_2, screen, self.key_change, self.health_change)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(dark_navy)
            level2.run()
            self.level_music.play()
            self.ui.health(self.current_health, self.max_health)
            self.ui.keys_show(self.keys)

            if self.player_died():
                self.level_music.stop()
                self.restart_game(2)  # Restart level 2

            clock.tick(60)
            pygame.display.update()
    
    def game_run_3(self):
        level3 = Level(level_3, screen, self.key_change, self.health_change)
        self.level_music.play(loops = -1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(dark_navy)
            level3.run()
            self.level_music.play()
            self.ui.health(self.current_health, self.max_health)
            self.ui.keys_show(self.keys)

            if self.player_died():
                self.level_music.stop()
                self.restart_game(3)  # Restart level 0

            clock.tick(60)
            pygame.display.update()
            
    def game_run_4(self):
        level4 = Level(level_4, screen, self.key_change, self.health_change)
        self.level_music.play(loops = -1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(dark_navy)
            level4.run()
            self.level_music.play()
            self.ui.health(self.current_health, self.max_health)
            self.ui.keys_show(self.keys)

            if self.player_died():
                self.level_music.stop()
                self.restart_game(4)  # Restart level 0

            clock.tick(60)
            pygame.display.update()

playing_instance = playing()
