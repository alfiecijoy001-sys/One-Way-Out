import pygame
from blocks import Block
from settings import block_size, screen_width
from player import Player
#blocks=name of file
#Block=class
#block=actual tile

class Level:
    def __init__(self,level_data,surface):
        self.display_surface=surface
        self.setup_level(level_data)
        self.world_shift=0
        
    def setup_level(self,layout):
        self.blocks=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x=col_index * block_size
                y=row_index * block_size
                
                if cell == 'X':
                    block = Block((x,y),block_size)
                    self.blocks.add(block)
                    
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < (screen_width/2) and direction_x < 0:
            self.world_shift=8
            player.speed=0
        
        elif player_x > screen_width - (screen_width/2) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
            
    def horizontal_movement_collision(self):
        player = self.player.sprite
            
        player.rect.x += player.direction.x * player.speed
        
        
        #checking through all the sprites for a collision
        for sprite in self.blocks.sprites():
            #checks if both rectangles collide
            if sprite.rect.colliderect(player.rect):
                #if player is moving left and collides
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                
                #if player is moving right and collides
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    
                    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        #checking through all the sprites for a collision
        for sprite in self.blocks.sprites():
            #checks if both rectangles collide
            if sprite.rect.colliderect(player.rect):
                player.jumping = False
                
                #if player is moving up and collides
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                #if player is moving down and collides
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        
            
    def run(self):
        self.blocks.update(self.world_shift)
        self.blocks.draw(self.display_surface)
        self.scroll_x()
        
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)