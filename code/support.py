import pygame
from csv import reader
from settings1 import tile_size

# Function to import a layout from a CSV file
def import_csv_layout(path):
    terrain_map = []

    # Open the CSV file and read its contents
    with open(path) as map:
        # Use the CSV reader to iterate through each row
        level = reader(map, delimiter=',')
        for row in level:
            # Convert each row into a list and append it to the terrain_map
            terrain_map.append(list(row))
        # Return the resulting terrain_map
        return terrain_map
    
# Function to import and cut graphics from an image
def import_cut_graphics(path):
    # Load the image and convert it to alpha transparency
    surface = pygame.image.load(path).convert_alpha()
    # Calculate the number of tiles in the x and y directions
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []

    # Iterate through rows and columns to cut the image into tiles
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            y = row * tile_size
            x = col * tile_size
            # Create a new surface for each tile with alpha transparency
            new_surface = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            # Blit the portion of the original image onto the new surface
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            # Append the cut tile to the cut_tiles list
            cut_tiles.append(new_surface)

    # Return the list of cut tiles
    return cut_tiles