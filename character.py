import pygame
from pygame import Vector2

class Character:
    def __init__(self, screen_width, screen_height):
        self.height = 64
        self.width = 64
        self.position = Vector2(280, screen_height - self.height * 4)
        # self.image = pygame.image.load("assets/character.png")
        # self.rect = self.image.get_rect()
        # self.rect.center = self.position
        self.total_life = 3
        self.life = self.total_life
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.position.x, self.position.y, self.width, self.height))  # Draw a white rectangle as the character