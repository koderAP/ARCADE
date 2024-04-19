import pygame
from font import DialogBox
from settings import WIDTH, HEIGHT
from story import render_story
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
        self.dialogs = [
            "Greetings,     young     traveler!",
            "Welcome    to      the     icy     regions     of      Eldoria.\n\nI    am      the     Elder     guardian    of      this    land.",
            "I      sense     a     brave       spirit      within    you,      eager     to    explore     and     learn.\n\nAre    you     ready   to      embark      on      a   journey     of      discovery?",
            "While      the      icy      terrain      holds      its      own      mysteries,\n\nthere      is      much      more      to      explore      beyond      these      frosty      lands.",
            "Seek      out      the      warmth      of      the      desert      sands,\n\nwhere      a      wise      Elder      Frog      awaits.",
            "Their      knowledge      may      hold      the      key      to      \n\nunlocking      new      adventures      and      challenges.",
            "Venture      forth,      young      adventurer,\n\nand      may      the      winds      of      destiny      guide      your      path!"
        ]

        self.current_dialog_index = 0
        
        self.sand_frog = [
            "Ah,      young      traveler,      you      have      found      your      way      to      the      sands      \n\nof      our      realm.",
            "Welcome!      Here,      amidst      the      swirling      dunes,      \n\nwisdom      awaits      those      who      seek      it.",

            "In      the      vast      expanse      of      this      desert,      \n\ndanger      lurks      in      the      form      of      rocky      obstacles.",
            "But      fear      not,      for      with      courage      and      swift      reflexes,      \n\nyou      can      navigate      this      terrain.",

            "Listen      closely,      young      one.      Board      the      landspeeder,      \n\nand      venture      forth      into      the      sandy      wilderness.",
            "Steer      clear      of      the      treacherous      rocks      that      dot      the      landscape,      \n\nand      your      journey      shall      be      a      fruitful      one.",

            "May      the      Force      be      with      you."

        ]
        
        self.forest_frog = [
            "Greetings,      traveler.      If      it's      shelter      you      seek,      \n\nour      old      home      lies      just      beyond      these      ancient      trees.",

            "Nestled      within      this      forsaken      forest,      \nour      once      vibrant      abode      now      stands      silent      and      still.",
            "But      within      its      walls      lies      a      secret,      \na      game      of      challenges      and      puzzles      awaiting      discovery.",

            "The      path      to      our      dwelling      may      be      obscured      by      nature's      grasp,      but      fear      not.      Follow      the      overgrown      trail,      and      soon      you      shall      stand      before      the      entrance      to      our      humble      sanctuary.",

            "As      you      step      through      the      threshold,      prepare      yourself      for      a      descent      into      the      unknown.      The      floors      below      hold      the      keys      to      unlocking      the      mysteries      of      our      past.",

            "The      house      you      seek      was      once      the      home      of      an      old      man      who      cherished      his      collection      of      miniature      frogs.      Many      tales      were      told      of      their      playful      antics      and      the      hidden      wonders      within      these      walls.",

            "But      beware,      for      the      journey      ahead      is      not      for      the      faint      of      heart.      Only      those      with      resolve      and      wit      shall      prevail      in      the      face      of      adversity.",

            "So      venture      forth,      intrepid      traveler,      and      may      the      echoes      of      our      tales      guide      your      steps      through      the      shadows      of      our      forsaken      home."

        ]
        
        self.forest_blob = [
            "Greetings,      traveler.      If      it's      shelter      you      seek,      \n\nour      old      home      lies      just      beyond      these      ancient      trees.",
            "Nestled      within      this      forsaken      forest,      \nour      once      vibrant      abode      now      stands      silent      and      still.",
        ]
        
        


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

     
    def fade_out(self):
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        for alpha in range(0, 255, 10):  # Increase alpha for fade-out effect
            fade_surface.set_alpha(alpha)
            self.display_surface.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.Clock().tick(30)  # Adjust as needed
       
    def start_pusher(self):
        if self.player.rect.centerx >= 1030 and self.player.rect.centerx <= 1090 and self.player.rect.centery >= 3610 and self.player.rect.centery <= 3650:
            if self.star_key:
                self.fade_out()
                pusher_main()
                self.fade_out()
                self.player.movable = True
                self.star_key = False
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init()
                pygame.mixer.music.load('../Graphics/Good Time.ogg')
                pygame.mixer.music.play(-1, 0.0, 5000)
    
    def start_landspeeder(self):
        self.fade_out()
        rect_save_main() 
        self.fade_out()
        self.landspeeder = False
        self.player.movable = True
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.music.load('../Graphics/Good Time.ogg')
        pygame.mixer.music.play(-1, 0.0, 5000)
        
    def start_platformer(self):
        if self.player.rect.centerx >= 1020 and self.player.rect.centerx <= 1080 and self.player.rect.centery >= 2140 and self.player.rect.centery <= 2160:
            if self.blob_key:
                self.fade_out()
                platformer_main()
                self.fade_out()
                self.blob_key = False
                self.player.movable = True
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init()
                pygame.mixer.music.load('../Graphics/Good Time.ogg')
                pygame.mixer.music.play(-1, 0.0, 5000)
                
    # def memory(self):
        
        
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