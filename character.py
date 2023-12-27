import pygame
from pygame import Vector2

class Character:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 64
        self.width = 64
        self.position = Vector2(0, self.screen_height - self.height)
        self.image = pygame.image.load("assets/character.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.total_life = 3
        self.life = self.total_life