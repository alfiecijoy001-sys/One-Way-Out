import pygame

class UI:
    def __init__(self,surface):
        #basic setup
        self.display_surface= surface
        #key count
        self.key_count=pygame.image.load('graphics/ui/key_tiles.png').convert_alpha()
        self.key_rect = self.key_count.get_rect(topleft=(50,61))
        self.font=pygame.font.Font('graphics/ui/dragonhunter.ttf.ttf',30)
        #health bar
        self.health_bar=pygame.image.load('graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (57,34)
        self.bar_width = 197
        self.bar_height = 14
        
    def health(self, current, full):
        self.display_surface.blit(self.health_bar, (20,25))
        health_ratio= current/full
        current_bar_width=self.bar_width * health_ratio
        health_bar_rect = pygame.Rect((self.health_bar_topleft), (current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface, '#dc4949', health_bar_rect)
    
    def keys_show(self, amount):
        self.display_surface.blit(self.key_count, self.key_rect)
        key_amount_surface= self.font.render(str(amount), False, '#33323d')
        key_amount_rect=key_amount_surface.get_rect(midleft = (self.key_rect.right + 4,self.key_rect.centery))
        self.display_surface.blit(key_amount_surface, key_amount_rect)
        
        
        