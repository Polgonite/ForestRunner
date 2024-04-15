import pygame
import random

spritePath = "game\\assets\\obstacles\\"

class obstacleClass():
    
    def __init__(self) -> None:
        
        self.sprites = self.load_sprites()

        random_number = random.randint(0, len(self.sprites) - 1)

        self.sprite = self.sprites[random_number]

        self.rect = self.sprite.get_rect()
        if 0 <= random_number <= 4:
            self.rect[0] = 350
            self.rect[1] = 151
        elif 5 <= random_number <= 9:
            self.rect[0] = 350
            self.rect[1] = 138
        elif 10 <= random_number <= 14:
            self.rect[0] = 350
            self.rect[1] = 151

        self.isJumping = False

        self.speed = [-1, 0]

    def load_sprites(self):
        sprites = [pygame.image.load(spritePath + "Bush 1\\Bush 1_GREEN.png"), 
                    pygame.image.load(spritePath + "Bush 1\\Bush 1_RED.png"), 
                    pygame.image.load(spritePath + "Bush 1\\Bush 1_TEAL.png"), 
                    pygame.image.load(spritePath + "Bush 1\\Bush 1_YELLOW.png"), 
                    pygame.image.load(spritePath + "Bush 1\\Bush 1_YELLOWISH GREEN.png"),
                    pygame.image.load(spritePath + "Bush 2\\Bush 2_GREEN.png"), 
                    pygame.image.load(spritePath + "Bush 2\\Bush 2_RED.png"), 
                    pygame.image.load(spritePath + "Bush 2\\Bush 2_TEAL.png"), 
                    pygame.image.load(spritePath + "Bush 2\\Bush 2_YELLOW.png"), 
                    pygame.image.load(spritePath + "Bush 2\\Bush 2_YELLOWISH GREEN.png"),
                    pygame.image.load(spritePath + "Bush 5\\Bush 5_GREEN.png"), 
                    pygame.image.load(spritePath + "Bush 5\\Bush 5_RED.png"), 
                    pygame.image.load(spritePath + "Bush 5\\Bush 5_TEAL.png"), 
                    pygame.image.load(spritePath + "Bush 5\\Bush 5_YELLOW.png"), 
                    pygame.image.load(spritePath + "Bush 5\\Bush 5_YELLOWISH GREEN.png")]
        return sprites