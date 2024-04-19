import pygame
from level_manager import LevelManager
from player import Player
from support import import_csv_layout, import_folder
from tiles import BigTile, Tile
from settings import TILESIZE
from story import render_story

def maximize_image(image):
    return pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))

class display:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.level = LevelManager(self.player, self.display_surface)
    
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
                                random_tree_image = maximize_image(random_tree_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '564':
                                random_tree_image = graphics['trees'][5]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '696':
                                random_tree_image = graphics['trees'][6]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '109':
                                random_tree_image = graphics['trees'][7]
                                random_tree_image = maximize_image(random_tree_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '10':
                                random_tree_image = graphics['trees'][8]
                                random_tree_image = maximize_image(random_tree_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                            if col == '630':
                                random_tree_image = graphics['trees'][9]
                                random_tree_image = maximize_image(random_tree_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'trees', random_tree_image)
                                
                        if style == 'stone_d':
                            if col == '231':
                                random_stone_image = graphics['stone'][0]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '596':
                                random_stone_image = graphics['stone'][1]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone1', random_stone_image)
                            if col == '728':
                                random_stone_image = graphics['stone'][2]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone2', random_stone_image)
                            if col == '104':
                                random_stone_image = graphics['stone'][3]
                                random_stone_image = maximize_image(random_stone_image)
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
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)  
                            if col == '627':
                                random_stone_image = graphics['grass'][4]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '62':
                                random_stone_image = graphics['grass'][5]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '293':
                                random_stone_image = graphics['grass'][6]
                                random_stone_image = maximize_image(random_stone_image)
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'stone', random_stone_image)
                            if col == '298':
                                random_stone_image = graphics['grass'][7]
                                random_stone_image = maximize_image(random_stone_image)
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
                            if col == '369':
                                random_tree_image = graphics['house'][2]
                                random_tree_image = maximize_image(random_tree_image)
                                BigTile((x, y), [self.visible_sprites, self.obstacle_sprites], 'house', random_tree_image)
                            
                   
        self.player = Player((3260,2990), [self.visible_sprites], self.obstacle_sprites) 
                                        
    def run(self, level):
        # Render game elements
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()   

        
        level.check_position_for_different_level()
        
        
        # Render story
        render_story(level.dialog_box)

        # Render dialog box
        if level.showing_dialog:
            level.dialog_box.set_text(level.dialogs[level.current_dialog_index])
            # level.handle_event(event)
            print(level.current_dialog_index)
            level.dialog_box.render(self.display_surface)
            
        level.start_starpusher()
        level.start_platformer()
        
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