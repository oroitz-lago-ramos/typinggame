import pygame

class Display:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((800, 600))
        
        self.background_trees = pygame.image.load("assets/arbres.png")
        self.background_trees = pygame.transform.scale(self.background_trees, (self.width, self.background_trees.get_height()))
        
        self.title = pygame.image.load("assets/Titre.png")
        self.title = pygame.transform.scale(self.title, (self.title.get_width() / 2, self.title.get_height() / 2))
        
        self.panel = pygame.image.load("assets/cadre.png")
        self.panel = pygame.transform.scale(self.panel, (self.panel.get_width() - 50, self.panel.get_height() - 50))
        self.panel = pygame.transform.rotate(self.panel, 5)
        
        self.button_image = pygame.image.load("assets/button_image.png")
        self.font = pygame.font.SysFont("Arial", 35)
        self.play_button_rect = pygame.Rect(self.width / 2 + self.button_image.get_width() / 2, self.height / 2 + self.button_image.get_height() * 1.5, self.button_image.get_width(), self.button_image.get_height())
        
        self.plateform = pygame.image.load("assets/plateforme.png")
        self.plateform = pygame.transform.scale(self.plateform, (self.plateform.get_width() / 2, self.plateform.get_height() / 2))

    def draw_game(self, character): #, word
        self.draw_background()
        
        self.screen.blit(self.plateform, (280, 280))

        character.draw(self.screen)
        # word.draw(self.screen)

        pygame.display.flip() 
        
    def draw_menu(self):
        """Draws the menu screen"""
        self.draw_background()
        
        #Draws the background panel, the title and the play button
        self.screen.blit(self.panel, (self.width / 2 - self.panel.get_width() / 2, self.height / 2 - self.panel.get_height() / 2))
        self.screen.blit(self.title, (self.width / 2 - self.title.get_width() / 1.4, 50))
        self.screen.blit(self.button_image, (self.width / 2 + self.button_image.get_width() / 2, self.height / 2 + self.button_image.get_height() * 1.5))
        
        #Draws the text on the play button
        play_text = self.font.render("PLAY", True, (0, 0, 0))
        play_text_x = self.width / 2 + self.button_image.get_width() / 2  + play_text.get_width() / 1.5
        play_text_y = self.height / 2 + self.button_image.get_height() * 1.5  + play_text.get_height() / 3.5
        self.screen.blit(play_text, (play_text_x, play_text_y))

        pygame.display.flip()
        
    def draw_background(self):
        '''Draws the background - sky and trees'''
        self.screen.fill((123, 203, 238))
        self.screen.blit(self.background_trees, (0, self.height - self.background_trees.get_height()))
        


    