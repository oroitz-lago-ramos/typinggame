import pygame

    
class Input:
    
    def handle_menu_input(self,play_button_rect):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse click is within the bounds of the button
                if play_button_rect.collidepoint(mouse_pos):
                    return "start_game"
                
                
    def handle_game_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"