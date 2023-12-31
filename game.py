# game.py
from character import Character
# from word import Word
from display import Display
from input import Input
import pygame

class Game:
    def __init__(self):
        self.display = Display()
        screen_width = self.display.width
        screen_height = self.display.height
        
        self.character = Character(screen_width, screen_height)
        
        # self.word = Word()
        
        self.input = Input()
        
        self.state = "menu"
        self.isRunning = True

    def run(self):
        while self.isRunning:
            if self.state == "menu":
                self.menu()
                action = self.input.handle_menu_input(self.display.play_button_rect)
                
                if action == "quit":
                    self.isRunning = False
                elif action == "start_game":
                    self.state = "game"
    
            elif self.state == "game":
                self.game()
                action = self.input.handle_game_input()
                
                if action == "quit":
                    self.isRunning = False
                    
            elif self.state == "game_over":
                self.game_over()
    
    def menu(self):
        self.display.draw_menu()
    
    def game(self):
        self.display.draw_game(self.character)
    
    def game_over(self):
        pass