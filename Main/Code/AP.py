import pygame
import sys
from button import Button
from map import display
from level_manager import LevelManager
from settings import WIDTH, HEIGHT
from story import render_story

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.music.load('../Graphics/Good Time.ogg')
pygame.mixer.music.play(-1, 0.0, 5000)

def run_game(map, level):
        # Render game elements
        map.visible_sprites.custom_draw(map.player)
        map.visible_sprites.update()   

        
        level.check_position_for_different_level()
        
        
        # Render story
        render_story(level.dialog_box)

        # Render dialog box
        if level.showing_dialog:
            level.dialog_box.set_text(level.dialogs[level.current_dialog_index])
            # level.handle_event(event)
            print(level.current_dialog_index)
            level.dialog_box.render(map.display_surface)
            
        level.start_starpusher()
        level.start_platformer()


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("../Graphics/tilemap/backGround.png")
BG = pygame.transform.scale(BG, (int(BG.get_width() * 1.1), int(BG.get_height() * 1.1)))

def get_font(size): 
    return pygame.font.Font("../Graphics/NormalFont.ttf", size)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("COP-290")
        self.clock = pygame.time.Clock()
        
        self.map = display()
        self.level = LevelManager(self.map.player, self.map.display_surface)
        
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                    
                self.level.handle_event(event) 
                
            run_game(self.map, self.level)
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

def play():
    while True:

        game = Game()
        game.run()
    

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(340, 450), 
                            text_input="PLAY", font=get_font(75), base_color="black", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(840, 450), 
                            text_input="QUIT", font=get_font(75), base_color="black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()