import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def update(self, shift):
        self.rect.x += shift
        
        
class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image=surface
  
        
        
class Crate(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('graphics/terrain/crate.png').convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))
        
class Door(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('graphics/character/spawn_door.png').convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))
        
class Keys(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('graphics/keys/key_tiles.png').convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))
    
        