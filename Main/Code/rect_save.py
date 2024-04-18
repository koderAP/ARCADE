from PIL import Image
import pygame
import time
import random
import math
from tile import Tile
pygame.font.init()

WIDTH, HEIGHT = 1200, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge")

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_FRAMES = [pygame.transform.scale(pygame.image.load(f'Trash/frame_{i}.png'), (PLAYER_WIDTH * 2, PLAYER_HEIGHT * 2)) for i in range(3)]

PLAYER_VEL = 10
PLAYER_FRAME_DURATION = 50  # Duration for each frame in milliseconds

STONE_WIDTH = 70
STONE_HEIGHT = 60
STONE_VEL = 5

BIG_STONE_WIDTH = 130
BIG_STONE_HEIGHT = 100
BIG_STONE_VEL = 5

STONE_IMAGE = pygame.image.load("../Graphics/sand/Obstacles/01.png")
STONE_IMAGE = pygame.transform.scale(STONE_IMAGE, (STONE_WIDTH, STONE_HEIGHT))
BIG_STONE_IMAGE = pygame.image.load("../Graphics/sand/Obstacles/4.png")
BIG_STONE_IMAGE = pygame.transform.scale(BIG_STONE_IMAGE, (BIG_STONE_WIDTH , BIG_STONE_HEIGHT))

FONT = pygame.font.SysFont("arial", 30)

def draw(player, player_frame, elapsed_time, stones, big_stones):
        
    time_text = FONT.render(f"Time: {round(elapsed_time, 2)}s", 5, "white")
    WIN.blit(time_text, (10, 10))
    
    # Blit the current player frame
    WIN.blit(player_frame, (player.x, player.y))
    
    for stone in stones:
        WIN.blit(STONE_IMAGE, (stone.x, stone.y))
    
    for big_stone in big_stones:
        WIN.blit(BIG_STONE_IMAGE, (big_stone.x, big_stone.y))
    
    pygame.display.update()

def main():
    
    bg = pygame.image.load("../Graphics/sand/sand0_0.png").convert()
    bg = pygame.transform.scale(bg, (int(bg.get_width() * 1.5), int(bg.get_height() * 1.5)))

    bg_height = bg.get_height()
    tiles = math.ceil(HEIGHT / bg_height) + 1

    scroll = 0
    
    run = True
    
    player = pygame.Rect(500, HEIGHT - 2 * PLAYER_HEIGHT, PLAYER_WIDTH - 5, PLAYER_HEIGHT - 5)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()
    elapsed_time = 0
    
    stone_add_increment = 1000
    stone_count = 3
    
    stones = []
    big_stones = []
    current_frame = 0  # Index of the current player frame
    frame_timer = 0
    
    hit = False
    
    while run:
        
        dt = clock.tick(60)  # Limit to 60 frames per second
        stone_count += dt
        elapsed_time = time.time() - start_time
        
    
        for i in range(0, tiles):
            WIN.blit(bg, (0, -(i * bg_height + scroll)))
            
        scroll -= 5
        
        if abs(scroll) > bg_height:
            scroll = 0
        
        if stone_count > stone_add_increment:
            for _ in range(2):
                stone_x = random.randint(0, WIDTH - STONE_WIDTH)
                stone = pygame.Rect(stone_x, -STONE_HEIGHT, STONE_WIDTH, STONE_HEIGHT)
                stones.append(stone)

                stone_x = random.randint(0, WIDTH - BIG_STONE_WIDTH)
                big_stone = pygame.Rect(stone_x, -BIG_STONE_HEIGHT, BIG_STONE_WIDTH, BIG_STONE_HEIGHT)
                big_stones.append(big_stone)

            stone_add_increment = max(50, stone_add_increment - 10)
            stone_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x < WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y > 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y < HEIGHT - PLAYER_HEIGHT:
            player.y += PLAYER_VEL
        
        # Update player frame animation
        frame_timer += dt
        if frame_timer >= PLAYER_FRAME_DURATION:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(PLAYER_FRAMES)
        
        player_frame = PLAYER_FRAMES[current_frame]
        
        player_hitbox = player.inflate(-40, -10)  
        
        for stone in stones[:]:
            stone.y += STONE_VEL
            stone_hitbox = stone.inflate(-10, -10)  
            if stone.y > HEIGHT:
                stones.remove(stone)
            elif stone_hitbox.colliderect(player_hitbox):
                stones.remove(stone)
                hit = True
                break

        for big_stone in big_stones[:]:
            big_stone.y += BIG_STONE_VEL
            big_stone_hitbox = big_stone.inflate(-20, -20) 
            if big_stone.y > HEIGHT:
                big_stones.remove(big_stone)
            elif big_stone_hitbox.colliderect(player_hitbox):
                big_stones.remove(big_stone)
                hit = True
                break

        if elapsed_time >= 60:
            run = False
            return 
        
        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)
            main()
        
        draw(player, player_frame, elapsed_time, stones, big_stones)  
