import pygame
from font import DialogBox
from settings import WIDTH, HEIGHT
from story import render_story, main_dialog, sand_frog_dialog, forest_frog_dialog, forest_blob_dialog
from pusher import main as pusher_main
from rect_save import main as rect_save_main
from platformer import main as platformer_main


font_path = "../Graphics/NormalFont.ttf"
font = pygame.font.Font(font_path, 28)

class LevelManager:
    def __init__(self, player, display_surface):
        self.display_surface = display_surface
        self.player = player
        self.landspeeder = True
        self.dialog_box = DialogBox(10, HEIGHT - 200, WIDTH - 20, HEIGHT * (2/9), "../Graphics/test/DialogueBoxSimple.png", "", font)
        self.dialogs = main_dialog

        self.current_dialog_index = 0
        
        self.sand_frog = sand_frog_dialog
        
        self.forest_frog = forest_frog_dialog
        
        self.forest_blob = forest_blob_dialog
        
        


        self.current_elder_god_dialog_index = 0
        self.showing_sand_frog = False

        self.showing_forest_frog = False

        self.showing_dialog = True
        self.dialogs_completed = False  

        self.pusher = True 
        self.frog = True
        self.star_key = False
        
        self.showing_blob = False
        self.blob = True
        self.blob_key = False


    def check_position_for_different_level(self):
        if self.player.rect.centerx >= 1970 and self.player.rect.centerx <= 2130 and self.player.rect.centery >= 960 and self.player.rect.centery <= 970:
            if self.landspeeder:
                print("Other game started")
                self.showing_sand_frog = True
                render_story(self.dialog_box)
                if self.showing_sand_frog:
                    self.dialog_box.set_text(self.sand_frog[self.current_elder_god_dialog_index])
                    self.dialog_box.render(self.display_surface)
        if self.player.rect.centerx >= 1709 and self.player.rect.centerx <= 1890 and self.player.rect.centery >= 3970 and self.player.rect.centery <= 3990:
            if self.frog:
                print("Other game started")
                self.showing_forest_frog = True
                render_story(self.dialog_box)
                if self.showing_forest_frog:
                    self.dialog_box.set_text(self.forest_frog[self.current_elder_god_dialog_index])
                    self.dialog_box.render(self.display_surface)
        if self.player.rect.centerx >= 750 and self.player.rect.centerx <= 920 and self.player.rect.centery >= 2500 and self.player.rect.centery <= 2530:
            if self.blob:
                print("Other game started")
                self.showing_blob = True
                render_story(self.dialog_box)
                if self.showing_blob:
                    self.dialog_box.set_text(self.forest_blob[self.current_elder_god_dialog_index])
                    self.dialog_box.render(self.display_surface)

            
    def start_pusher(self):
        if self.player.rect.centerx >= 1030 and self.player.rect.centerx <= 1090 and self.player.rect.centery >= 3610 and self.player.rect.centery <= 3650:
            if self.star_key:
                pusher_main()
                self.player.movable = True
                self.star_key = False
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init()
                pygame.mixer.music.load('../Graphics/Good Time.ogg')
                pygame.mixer.music.play(-1, 0.0, 5000)
    
    def start_landspeeder(self):
        
        rect_save_main() 
        self.landspeeder = False
        self.player.movable = True
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.music.load('../Graphics/Good Time.ogg')
        pygame.mixer.music.play(-1, 0.0, 5000)
        
    def start_platformer(self):
        if self.player.rect.centerx >= 1020 and self.player.rect.centerx <= 1080 and self.player.rect.centery >= 2140 and self.player.rect.centery <= 2160:
            if self.blob_key:
                platformer_main()
                self.blob_key = False
                self.player.movable = True
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init()
                pygame.mixer.music.load('../Graphics/Good Time.wav')
                pygame.mixer.music.play(-1, 0.0, 5000)
                
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            print("in here")    
            if self.showing_dialog:
                print("not here")
                if event.key == pygame.K_RETURN:
                    print("why yes")
                    self.current_dialog_index += 1
                    if self.current_dialog_index >= len(self.dialogs):
                        print("Dialogs completed")
                        self.showing_dialog = False
                        self.current_dialog_index = 0
                        self.dialogs_completed = True
                        self.player.movable = True
            elif self.showing_sand_frog:
                self.player.movable = False
                if event.key == pygame.K_RETURN:
                    self.current_elder_god_dialog_index += 1
                    if self.current_elder_god_dialog_index >= len(self.sand_frog):
                        self.showing_sand_frog = False
                        self.current_elder_god_dialog_index = 0
                        self.start_landspeeder() 
            elif self.showing_forest_frog:
                self.player.movable = False
                if event.key == pygame.K_RETURN:
                    self.current_elder_god_dialog_index += 1
                    if self.current_elder_god_dialog_index >= len(self.forest_frog):
                        self.showing_forest_frog = False
                        self.current_elder_god_dialog_index = 0
                        self.star_key = True
                        self.player.movable = True
                        self.frog = False
            elif self.showing_blob:
                self.player.movable = False
                if event.key == pygame.K_RETURN:
                    self.current_elder_god_dialog_index += 1
                    if self.current_elder_god_dialog_index >= len(self.forest_blob):
                        self.showing_blob = False
                        self.current_elder_god_dialog_index = 0
                        self.blob = False
                        self.player.movable = True
                        self.blob_key = True          