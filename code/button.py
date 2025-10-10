import pygame

#Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = int(image.get_width() * scale)
        height = int(image.get_height() * scale)
        
        self.image=pygame.transform.scale(image, (width, height))
        self.rect=self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self, surface):
        #get mouse pos
        pos=pygame.mouse.get_pos()
                
        
        #draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def hide(self):
        # Move the button off-screen
        self.rect.topleft = (-self.rect.width, -self.rect.height)

    def remove(self, surface):
        # Fill the button area with the background color to remove it
        background_color = (0, 0, 0)  # You can replace this with your background color
        surface.fill(background_color, self.rect)
 