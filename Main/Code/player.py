import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/Anim/down_idle/idle_down.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -20)
        
        self.import_player_assets()
        self.status = 'up'
        self.frame_index = 0
        self.animation_speed = 0.15
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.movable = False
        
        self.obstacle_sprites = obstacle_sprites
        
    def import_player_assets(self):
        character_path = '../Graphics/test/Anim/'
        self.animations = {'up':[], 'down':[], 'left':[], 'right':[], 'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + '/' + animation
            self.animations[animation] = import_folder(full_path)
            for i in range(len(self.animations[animation])):
                self.animations[animation][i] = pygame.transform.scale(self.animations[animation][i], (self.animations[animation][i].get_width() * 4, self.animations[animation][i].get_height() * 4))
            
        
    def input(self):
        
        # if self.movable:
        keys = pygame.key.get_pressed()
        if self.movable:                
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else :
                self.direction.x = 0
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else :
                self.direction.y = 0
       
    def get_status(self):
        
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'
       
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if self.hitbox.colliderect(sprite.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if self.hitbox.colliderect(sprite.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
         
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
         
    def update(self):  
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
        
        