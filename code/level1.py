
import pygame
from settings1 import tile_size, screen_width, screen_height
from support import import_csv_layout, import_cut_graphics
from tiles import Tile, StaticTile, Crate, Keys, Door
from enemy import Enemy
from player import Player
import button
from levelscreen import levelscreen, stop_music, do_pregame_music



screen = pygame.display.set_mode((screen_width, screen_height))
back_btn_img=pygame.image.load("code/back_btn.png").convert()
restart_btn_img=pygame.image.load("code/restart_btn.png").convert()
back_button=button.Button(300, 200, back_btn_img, 0.25)
restart_button=button.Button(300, 350, restart_btn_img, 0.25)

clock = pygame.time.Clock() # Initialise the clock




class Level:
    def __init__(self, level_data, surface, key_change, health_change):
        
        self.display_surface=surface
        self.world_shift = 0
        
        self.current_x=None
        
        #player
        player_layout = import_csv_layout(level_data['player'])
        self.player=pygame.sprite.GroupSingle()
        self.goal=pygame.sprite.GroupSingle()
        self.player_setup(player_layout, health_change)
        
        self.coin_collect = pygame.mixer.Sound('sounds/coin_collect.mp3')
        self.enemy_kill = pygame.mixer.Sound('sounds/enemy_kill.mp3')
        self.losing_health = pygame.mixer.Sound('sounds/losing_health.mp3')
        
        #ui
        self.key_change= key_change
        
        #crate setup
        crate_layout=import_csv_layout(level_data['crates'])
        self.crate_sprites = self.create_tile_group(crate_layout, 'crates')
        
        #land setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        
        #keys setup
        keys_layout = import_csv_layout(level_data['keys'])
        self.keys_sprites = self.create_tile_group(keys_layout, 'keys')
        
        #enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')
        
        #door
        door_layout = import_csv_layout(level_data['door'])
        self.door_sprites = self.create_tile_group(door_layout, 'door')
        
        #constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, 'constraints')
        
    #draw function      
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.display_surface.blit(img, (x,y))
        
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../graphics/terrain/cave_tilesnew.png')
                        tile_surface= terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)
                        
                    if type == 'crates':
                        sprite=Crate(tile_size, x, y)
                        
                    if type == 'keys':
                        sprite=Keys(tile_size, x, y)
                        
                    if type == 'enemies':
                        sprite=Enemy(tile_size, x, y)
                        
                    if type == 'constraints':
                        sprite=Tile(tile_size, x, y)
                        
                    if type == 'door':
                        sprite=Door(tile_size, x, y)
                        
                    sprite_group.add(sprite)
        
        return sprite_group
    
    
    
    def player_setup(self, layout, health_change):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':   #0 is the player
                    sprite=Player((x,y), health_change)
                    self.player.add(sprite)
                '''if val == '1':   #1 is the goal
                    door_surface= pygame.image.load('../graphics/character/spawn_door.png').convert_alpha()
                    y -= 30 #adjusting height of y co-ordinate of door
                    sprite = StaticTile(tile_size, x, y, door_surface)
                    self.goal.add(sprite)'''
                    
            
            
            
    
    
    def enemy_collision_flipped(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.flipped()
            

        
        
    def horizontal_movement_collision(self):
        player = self.player.sprite
            
        player.rect.x += player.direction.x * player.speed
        
        collidable_sprites= self.terrain_sprites.sprites() + self.crate_sprites.sprites() 
        #checking through all the sprites for a collision
        for sprite in collidable_sprites:
            #checks if both rectangles collide
            if sprite.rect.colliderect(player.rect):
                #if player is moving left and collides
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.current_x=player.rect.left
                #if player is moving right and collides
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x=player.rect.right
                    
                    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites= self.terrain_sprites.sprites() + self.crate_sprites.sprites() 
        
        #checking through all the sprites for a collision
        for sprite in collidable_sprites:
            #checks if both rectangles collide
            if sprite.rect.colliderect(player.rect):
                player.jumping = False
                self.world_shift = 0
                player.speed=0
                #if player is moving up and collides
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                #if player is moving down and collides
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < (screen_width/1.5) and direction_x < 0:
            self.world_shift=8
            player.speed=0
        
        elif player_x > screen_width - (screen_width/1.5) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
            
            
    def touching_enemy(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite, self.enemy_sprites, False)
        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_top = enemy.rect.top
                enemy_center = enemy.rect.centery
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -19
                    self.enemy_kill.play()
                    enemy.kill()
                else:
                    self.player.sprite.get_damage()
                    if not self.losing_health_played:
                        self.losing_health.play()
                        self.losing_health_played = True
        else:
            self.losing_health_played = False
    
    def check_key_collisions(self):
       collided_keys=pygame.sprite.spritecollide(self.player.sprite, self.keys_sprites, True)
       if collided_keys:
           
           self.coin_collect.play()
           for key in collided_keys:
               self.key_change(1)
               

       
       
       
    def check_complete(self):
        global level_complete_displayed
        level_complete_displayed=False
        # Check if the player collides with the goal
        if pygame.sprite.spritecollideany(self.player.sprite, self.door_sprites):
            print("Collision detected!")
            complete_bg = pygame.image.load("code/CompleteScreen.png")
            complete_bg = pygame.transform.scale(complete_bg, (800, 600))
            if not level_complete_displayed:
                complete_bg.set_alpha(255)
                screen.blit(complete_bg, (0, 0))
                level_complete_displayed = True
            back_button.draw(screen)
            restart_button.draw(screen)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(event.pos):
                        print("Back clicked")
                        back_button.hide()  # Move the button off-screen
                        back_button.remove(screen)  # Remove the button from the screen
                        restart_button.hide()  # Move the button off-screen
                        restart_button.remove(screen)  # Remove the button from the screen
                        complete_bg.set_alpha(0)
                        level_complete_displayed = True
                        screen.blit(complete_bg, (0, 0))
                        levelscreen()
                        
                    elif restart_button.rect.collidepoint(event.pos):
                        print("Restart Clicked")
                        back_button.hide()  # Move the button off-screen
                        back_button.remove(screen)  # Remove the button from the screen
                        restart_button.hide()  # Move the button off-screen
                        restart_button.remove(screen)  # Remove the button from the screen
                        complete_bg.set_alpha(0)
                        level_complete_displayed = True
                        screen.blit(complete_bg, (0, 0))
                        self.player.sprite.replay()
                        
                    
                        
                        
                        
                            
            
               
    def run(self):
        #land
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        
        
        #enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_flipped()
        self.enemy_sprites.draw(self.display_surface)
        
        #crates
        self.crate_sprites.draw(self.display_surface)
        self.crate_sprites.update(self.world_shift)
        
        #keys
        self.keys_sprites.draw(self.display_surface)
        self.keys_sprites.update(self.world_shift)
        
        #door
        self.door_sprites.draw(self.display_surface)
        self.door_sprites.update(self.world_shift)
        
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        
        #self.end_collision()
        #self.check_death()
        #self.check_complete()
        self.touching_enemy()
        self.check_key_collisions()
        self.check_complete()
        #self.fell_off()
        
level_complete_displayed = False
screen=pygame.display.set_mode((screen_width,screen_height))
        