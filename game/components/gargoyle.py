import pygame
import random

spritePath = "game\\assets\\obstacles\\gargoyle\\"

class gargoyleClass():
    
    def __init__(self) -> None:
        
        self.sprites = self.load_sprites()

        random_number = random.randint(0, 3)

        self.sprite = self.sprites[0]

        self.rect = self.sprite.get_rect()
        if random_number == 0:
            self.rect[0] = 350
            self.rect[1] = 142
        elif random_number == 1:
            self.rect[0] = 350
            self.rect[1] = 152
        elif random_number == 2:
            self.rect[0] = 350
            self.rect[1] = 101
        elif random_number == 3:
            self.rect[0] = 350
            self.rect[1] = 121


        self.isJumping = False

        self.speed = [-1, 0]

    def load_sprites(self):
        sprites = [pygame.transform.flip(pygame.image.load(spritePath + "gargoyle-fly-00.png"), True, False), 
                    pygame.transform.flip(pygame.image.load(spritePath + "gargoyle-fly-01.png"), True, False), 
                    pygame.transform.flip(pygame.image.load(spritePath + "gargoyle-fly-02.png"), True, False), 
                    pygame.transform.flip(pygame.image.load(spritePath + "gargoyle-fly-03.png"), True, False), 
                    pygame.transform.flip(pygame.image.load(spritePath + "gargoyle-fly-04.png"), True, False)]
        return sprites