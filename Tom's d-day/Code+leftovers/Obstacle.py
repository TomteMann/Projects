import pygame
import os


# File Importing (Changes Directory to Where the File is Saved)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        color = (66, 66, 66)
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))

shape = [
"  xxxxxxxx",
"xxxxxxxxxxxx",
"xxxxxxxxxxxx",
"xxxxxxxxxxxx",
"xxxxxxxxxxxx"


]
