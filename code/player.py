import pygame
from math import sin

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, health_change):
        super().__init__()
        
        # Load and scale the image
        self.original_image = pygame.image.load('user_character.png')
        self.original_image = pygame.transform.scale(self.original_image, (53, 57))
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=pos)
        
        
        self.health_change = health_change
        self.invincible = False
        self.invincibility_time= 900
        self.pain_time=0

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -20
        self.jumping = False
        self.looking_right = True
        
        

    def flip_image(self):
        if self.invincible:
            alpha= self.wave()
            self.image.set_alpha(alpha)
            
        else:
            self.image.set_alpha(255)
            
        if self.looking_right:
            self.image = self.original_image
            
        else:
            self.image = pygame.transform.flip(self.original_image, True, False)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.looking_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.looking_right = False
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if not self.jumping:
                self.jump()
                self.jumping = True
                print(self.rect)
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def get_damage(self):
        if not self.invincible:
            self.health_change(-33.4)
            self.invincible = True
            self.pain_time=pygame.time.get_ticks()
            
    def replay(self):
        if not self.invincible:
            self.health_change(-100)
            
    def wave(self):
        number = sin(pygame.time.get_ticks())
        if number >= 0: return 255 #255 is not invisible
        
        else: return 0 #invisible, fully transparent
            
            
    def invincible_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.pain_time >= self.invincibility_time:
                self.invincible = False
                
    def off_screen(self):
        if self.rect.bottom >= 598:
            print("died")
            self.replay()
        

    def update(self):
        self.get_input()
        self.flip_image()  # Call the image flipping method
        self.invincible_timer()
        self.wave()
        self.off_screen()
        
