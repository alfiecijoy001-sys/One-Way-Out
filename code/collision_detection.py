import pygame

# Function to check for collisions
def end_collision(player, goal):
    # Check if the player collides with the goal
    if pygame.sprite.spritecollideany(player, goal):
        print("Collision detected!") 