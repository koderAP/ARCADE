import pygame
from settings import *
from tile import Tile
from bigtile import BigTile
from player import Player
from support import import_csv_layout, import_folder
from rect_save import main as rect_save_main
from font import DialogBox
from story import render_story
from starpusher import main as starpusher_main
from platformer import main as platformer_main

font_path = "../Graphics/NormalFont.ttf"
font = pygame.font.Font(font_path, 28)


def maximize_image(image):
    return pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.landspeeder = True
        
        self.create_map()
        
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

        self.starpusher = True 
        self.frog = True
        self.star_key = False
        
        self.showing_blob = False
        self.blob = True
        self.blob_key = False


    def create_map(self):
        layout = {
            'boundary': import_csv_layout('../Map/Ground_Boundary.csv'),
            'grass': import_csv_layout('../map/Ground_Grass.csv'),
            'trees': import_csv_layout('../map/Ground_SmallTree.csv'),
            'stone': import_csv_layout('../map/Ground_Stone.csv'),
            'stone_d': import_csv_layout('../map/Ground_Stone_d.csv'),
            'big_tree': import_csv_layout('../map/Ground_BigTree.csv'),
            'house': import_csv_layout('../map/Ground_House.csv'),
        }
        
        graphics = {
            'grass': import_folder('../Graphics/grass'),
            'stone': import_folder('../Graphics/stone'),
            'deity': import_folder('../Graphics/deity'),
            'trees': import_folder('../Graphics/trees'),
            'big_tree': import_folder('../Graphics/bigtree'),
            'house': import_folder('../Graphics/house'),
        }
        
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                            
                        if style == 'trees':
                            if col == '205':
                                random_tree_image = graphics['trees'][0]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '0':
                                random_tree_image = graphics['trees'][1]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '2':
                                random_tree_image = graphics['trees'][2]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '6':
                                random_tree_image = graphics['trees'][3]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '16':
                                random_tree_image = graphics['trees'][4]
                                random_tree_image = pygame.transform.scale(random_tree_image, (random_tree_image.get_width() * 4, random_tree_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '564':
                                random_tree_image = graphics['trees'][5]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '696':
                                random_tree_image = graphics['trees'][6]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '109':
                                random_tree_image = graphics['trees'][7]
                                random_tree_image = pygame.transform.scale(random_tree_image, (random_tree_image.get_width() * 4, random_tree_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '10':
                                random_tree_image = graphics['trees'][8]
                                random_tree_image = pygame.transform.scale(random_tree_image, (random_tree_image.get_width() * 4, random_tree_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '630':
                                random_tree_image = graphics['trees'][9]
                                random_tree_image = pygame.transform.scale(random_tree_image, (random_tree_image.get_width() * 4, random_tree_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                                
                        if style == 'stone_d':
                            if col == '231':
                                random_stone_image = graphics['stone'][0]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '596':
                                random_stone_image = graphics['stone'][1]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone1', random_stone_image)
                            if col == '728':
                                random_stone_image = graphics['stone'][2]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone2', random_stone_image)
                            if col == '104':
                                random_stone_image = graphics['stone'][3]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone3', random_stone_image)
                                
                        if style == 'grass':
                            if col == '268':
                                random_stone_image = graphics['grass'][0]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '269':
                                random_stone_image = graphics['grass'][1]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '270':
                                random_stone_image = graphics['grass'][2]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '495':
                                random_stone_image = graphics['grass'][3]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)  
                            if col == '627':
                                random_stone_image = graphics['grass'][4]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '62':
                                random_stone_image = graphics['grass'][5]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '293':
                                random_stone_image = graphics['grass'][6]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '298':
                                random_stone_image = graphics['grass'][7]
                                random_stone_image = pygame.transform.scale(random_stone_image, (random_stone_image.get_width() * 4, random_stone_image.get_height() * 4))
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)

                        if style == 'big_tree':
                            if col == '52':
                                random_tree_image = graphics['big_tree'][0]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'big_tree', random_tree_image)
                            if col == '48':
                                random_tree_image = graphics['big_tree'][1]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'big_tree', random_tree_image)
                            if col == '132':
                                random_tree_image = graphics['big_tree'][3]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'big_tree', random_tree_image)
                            if col == '128':
                                random_tree_image = graphics['big_tree'][4]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'big_tree', random_tree_image)
                        
                        if style == 'house':
                            if col == '132':
                                random_tree_image = graphics['house'][0]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'house', random_tree_image)
                            if col == '487':
                                random_tree_image = graphics['house'][1]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'house', random_tree_image)
                            
                   
        self.player = Player((3260,2990), [self.visible_sprites], self.obstacle_sprites) 
                                        
    def run(self):
        # Render game elements
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()   

        
        self.check_position_for_different_level()
        
        print(self.player.rect.centerx, self.player.rect.centery)
        
        # Render story
        render_story(self.dialog_box)

        # Render dialog box
        if self.showing_dialog:
            self.dialog_box.set_text(self.dialogs[self.current_dialog_index])
            self.dialog_box.render(self.display_surface)
            
        self.start_starpusher()
        self.start_platformer()
            



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

            
    def start_starpusher(self):
        if self.player.rect.centerx >= 1030 and self.player.rect.centerx <= 1090 and self.player.rect.centery >= 3610 and self.player.rect.centery <= 3650:
            if self.star_key:
                starpusher_main()
                self.player.movable = True
                self.star_key = False
    
    def start_landspeeder(self):
        
        rect_save_main() 
        self.landspeeder = False
        self.player.movable = True
        
    def start_platformer(self):
        if self.player.rect.centerx >= 1020 and self.player.rect.centerx <= 1080 and self.player.rect.centery >= 2140 and self.player.rect.centery <= 2160:
            if self.blob_key:
                platformer_main()
                self.blob_key = False
                self.player.movable = True
                
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.showing_dialog:
                if event.key == pygame.K_RETURN:
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
                        

        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()
        
        self.floor_surface = pygame.image.load('../Graphics/tilemap/Ground.png').convert_alpha()
        self.floor_surface = pygame.transform.scale(self.floor_surface, (self.floor_surface.get_width() * 4, self.floor_surface.get_height() * 4))
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    
    def custom_draw(self,player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
