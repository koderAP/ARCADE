import pygame
from pygame.locals import *
from pygame import mixer
from os import path
import pandas as pd

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    screen_width = 1200
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    font_path = "../Graphics/NormalFont.ttf"
    font = pygame.font.Font(font_path, 50)
    font_score = font

    tile_size = 40
    tile_size_x = 50
    tile_size_y = 40
    game_over = 0
    level = 1
    max_levels = 7
    score = 0

    white = (255, 255, 255)
    blue = (0, 0, 255)

    bg_img = pygame.transform.scale(pygame.image.load('../Graphics/platform/sky.png'), (screen_width, screen_height))

    pygame.mixer.music.load('../Graphics/platform/music.wav')
    pygame.mixer.music.play(-1, 0.0, 5000)
    coin_fx = pygame.mixer.Sound('../Graphics/platform/coin.wav')
    coin_fx.set_volume(0.5)
    jump_fx = pygame.mixer.Sound('../Graphics/platform/jump.wav')
    jump_fx.set_volume(0.5)
    game_over_fx = pygame.mixer.Sound('../Graphics/platform/game_over.wav')
    game_over_fx.set_volume(0.5)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def reset_level(level):
        player.reset(100, screen_height - 130)
        blob_group.empty()
        platform_group.empty()
        coin_group.empty()
        lava_group.empty()
        exit_group.empty()

        if path.exists(f'../Map/Platform/level{level}_data.csv'):
            df = pd.read_csv(f'../Map/Platform/level{level}_data.csv', header=None)
            world_data = df.values.tolist()

        world = World(world_data)
        score_coin = Coin(tile_size // 2, tile_size // 2)
        coin_group.add(score_coin)
        return world


    class Player():
        def __init__(self, x, y):
            self.reset(x, y)

        def update(self, game_over):
            dx = 0
            dy = 0
            walk_cooldown = 5
            col_thresh = 20

            if game_over == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_w] and self.jumped == False and self.in_air == False:
                    jump_fx.play()
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_w] == False:
                    self.jumped = False
                if key[pygame.K_a]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_d]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_a] == False and key[pygame.K_d] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                self.in_air = True
                for tile in world.tile_list:
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

                if pygame.sprite.spritecollide(self, blob_group, False):
                    game_over = -1
                    game_over_fx.play()

                if pygame.sprite.spritecollide(self, lava_group, False):
                    game_over = -1
                    game_over_fx.play()

                if pygame.sprite.spritecollide(self, exit_group, False):
                    game_over = 1

                for platform in platform_group:
                    if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                            self.vel_y = 0
                            dy = platform.rect.bottom - self.rect.top
                        elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                            self.rect.bottom = platform.rect.top - 1
                            self.in_air = False
                            dy = 0
                        if platform.move_x != 0:
                            self.rect.x += platform.move_direction

                self.rect.x += dx
                self.rect.y += dy

            elif game_over == -1:
                self.image = self.dead_image
                draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
                if self.rect.y > 200:
                    self.rect.y -= 5

            screen.blit(self.image, self.rect)

            return game_over

        def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'../Graphics/platform/guy{num}.png')
                img_right = pygame.transform.scale(img_right, (int(40 * screen_width/1000), int(60*screen_height/1000)))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('../Graphics/platform/ghost.png')
            self.dead_image = pygame.transform.scale(self.dead_image, (int(40 * screen_width/1000), int(80*screen_height/1000)))
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = True

    class World():
        def __init__(self, data):
            self.tile_list = []
            dirt_img = pygame.image.load('../Graphics/platform/dirt.png')
            grass_img = pygame.image.load('../Graphics/platform/grass.png')
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size_x, tile_size_y))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size_x
                        img_rect.y = row_count * tile_size_y
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size_x, tile_size_y))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size_x
                        img_rect.y = row_count * tile_size_y
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        blob = Enemy(col_count * tile_size_x, row_count * tile_size_y + 15)
                        blob_group.add(blob)
                    if tile == 4:
                        platform = Platform(col_count * tile_size_x, row_count * tile_size_y, 1, 0)
                        platform_group.add(platform)
                    if tile == 5:
                        platform = Platform(col_count * tile_size_x, row_count * tile_size_y, 0, 1)
                        platform_group.add(platform)
                    if tile == 6:
                        lava_frames = [pygame.transform.scale(pygame.image.load('../Graphics/platform/lava_frame1.png'), (tile_size_x, tile_size_y)), pygame.transform.scale(pygame.image.load('../Graphics/platform/lava_frame2.png'), (tile_size_x, tile_size_y))]
                        lava = Lava(col_count * tile_size_x, row_count * tile_size_y + (tile_size_y // 2), lava_frames)
                        lava_group.add(lava)
                    if tile == 7:
                        coin = Coin(col_count * tile_size_x + (tile_size_x // 2), row_count * tile_size_y + (tile_size_y // 2))
                        coin_group.add(coin)
                    if tile == 8:
                        exit = Exit(col_count * tile_size_x, row_count * tile_size_y - (tile_size_y // 2))
                        exit_group.add(exit)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('../Graphics/platform/blob.png'), (tile_size_x,1.2* tile_size_y))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > tile_size_x:
                self.move_direction *= -1
                self.move_counter *= -1

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, move_x, move_y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/platform/platform.png')
            self.image = pygame.transform.scale(img, (tile_size_x * 1.2, tile_size_y // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_counter = 0
            self.move_direction = 1
            self.move_x = move_x
            self.move_y = move_y

        def update(self):
            self.rect.x += self.move_direction * self.move_x
            self.rect.y += self.move_direction * self.move_y
            self.move_counter += 1
            if abs(self.move_counter) > tile_size_x:
                self.move_direction *= -1
                self.move_counter *= -1

    class Lava(pygame.sprite.Sprite):
        def __init__(self, x, y, gif_frames):
            pygame.sprite.Sprite.__init__(self)
            self.gif_frames = gif_frames
            self.image = self.gif_frames[0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.frame_index = 0
            self.frame_cooldown = 0
            self.frame_delay = 10  # Adjust this value to control the speed of the animation

        def update(self):
            if self.frame_cooldown <= 0:
                self.frame_index = (self.frame_index + 1) % len(self.gif_frames)
                self.image = self.gif_frames[self.frame_index]
                self.frame_cooldown = self.frame_delay
            else:
                self.frame_cooldown -= 1

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/platform/coin.png')
            self.image = pygame.transform.scale(img, (tile_size_x // (1.2 * 1.5), tile_size_y // 1.5))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class Exit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/platform/exit.png')
            self.image = pygame.transform.scale(img, (tile_size_x, int(tile_size_y * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    player = Player(100, screen_height - 130)

    blob_group = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    lava_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    exit_group = pygame.sprite.Group()

    score_coin = Coin(tile_size_x // 2, tile_size_y // 2)
    coin_group.add(score_coin)

    if path.exists(f'../Map/Platform/level{level}_data.csv'):
        df = pd.read_csv(f'../Map/Platform/level{level}_data.csv', header=None)
        world_data = df.values.tolist()
    world = World(world_data)

    run = True
    while run:
        clock.tick(fps)
        screen.blit(bg_img, (0, 0))

        world.draw()

        if game_over == 0:
            blob_group.update()
            platform_group.update()
            lava_group.update()  # Update lava animation

            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X ' + str(score), font_score, white, tile_size_x - 10, 10)

        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        if game_over == -1:
            draw_text('GAME OVER!', font, [0,0,0], (screen_width // 2) - 200, screen_height // 2)

        if game_over == 1:
            level += 1
            if level <= max_levels:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    level = level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

        pygame.display.update()

    # pygame.quit()

# if __name__ == "__main__":
#     main()
