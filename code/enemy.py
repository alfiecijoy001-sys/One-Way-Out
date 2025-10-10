import pygame
from tiles import StaticTile
from random import randint

class Enemy(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('../graphics/enemies/sized_character.png').convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))
        self.speed = randint(2, 4)
        self.original_image = self.image  # Store original image for flipping

    def move(self):
        self.rect.x += self.speed

    def flipped_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image  # Revert to original image when moving right

    def flipped(self):
        self.speed = self.speed * -1 # Reverse the speed to change direction

    def update(self, shift):
        self.rect.x += shift
        self.move()
        self.flipped_image()

        
