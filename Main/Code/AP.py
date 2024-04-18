import pygame, sys
from level import Level
from settings import WIDTH, HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("COP-290")
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                    
                self.level.handle_event(event) 
                
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
    game = Game()
    game.run()
