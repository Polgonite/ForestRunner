import pygame

spritePath = "game\\assets\\characterSprite\\"

class playerClass():
    
    def __init__(self) -> None:
        
        self.idle = self.load_idle_sprites()

        self.right = self.load_right_sprites()

        self.die = self.load_die_sprites()

        self.jump = self.load_jump_sprites()

        self.slide = self.load_slide_sprites()

        self.rect = self.idle[0].get_rect()
        self.rect[1] = 142

        self.sprite = self.idle[0]

        self.isJumping = False

        self.isSliding = False

        self.isDead = False

        self.mask = pygame.mask.from_surface(self.idle[0])

        self.speed = [0, 0]

    def load_idle_sprites(self):
        idle = [pygame.image.load(spritePath + "adventurer-idle-00.png"), 
                pygame.image.load(spritePath + "adventurer-idle-01.png"), 
                pygame.image.load(spritePath + "adventurer-idle-02.png"), 
                pygame.image.load(spritePath + "adventurer-idle-03.png")]
        return idle

    def load_right_sprites(self):
        right = [pygame.image.load(spritePath + "adventurer-run-00.png"), 
                pygame.image.load(spritePath + "adventurer-run-01.png"), 
                pygame.image.load(spritePath + "adventurer-run-02.png"), 
                pygame.image.load(spritePath + "adventurer-run-03.png"), 
                pygame.image.load(spritePath + "adventurer-run-04.png"), 
                pygame.image.load(spritePath + "adventurer-run-05.png")]
        return right

    def load_die_sprites(self):
        die = [pygame.image.load(spritePath + "adventurer-die-00.png"), 
                pygame.image.load(spritePath + "adventurer-die-01.png"), 
                pygame.image.load(spritePath + "adventurer-die-02.png"), 
                pygame.image.load(spritePath + "adventurer-die-03.png"), 
                pygame.image.load(spritePath + "adventurer-die-04.png"), 
                pygame.image.load(spritePath + "adventurer-die-05.png"), 
                pygame.image.load(spritePath + "adventurer-die-06.png")]
        return die

    def load_jump_sprites(self):
        jump = [pygame.image.load(spritePath + "adventurer-jump-00.png"), 
                pygame.image.load(spritePath + "adventurer-jump-01.png"), 
                pygame.image.load(spritePath + "adventurer-jump-02.png"), 
                pygame.image.load(spritePath + "adventurer-jump-03.png"), 
                pygame.image.load(spritePath + "adventurer-smrslt-00.png"), 
                pygame.image.load(spritePath + "adventurer-smrslt-01.png"), 
                pygame.image.load(spritePath + "adventurer-smrslt-02.png"), 
                pygame.image.load(spritePath + "adventurer-smrslt-03.png"), 
                pygame.image.load(spritePath + "adventurer-fall-00.png"), 
                pygame.image.load(spritePath + "adventurer-fall-01.png")]
        return jump

    def load_slide_sprites(self):
        slide = [pygame.image.load(spritePath + "adventurer-stand-02.png"), 
                pygame.image.load(spritePath + "adventurer-stand-01.png"), 
                pygame.image.load(spritePath + "adventurer-stand-00.png"),
                pygame.image.load(spritePath + "adventurer-slide-00.png"), 
                pygame.image.load(spritePath + "adventurer-slide-01.png"),
                pygame.image.load(spritePath + "adventurer-stand-00.png"),
                pygame.image.load(spritePath + "adventurer-stand-01.png"), 
                pygame.image.load(spritePath + "adventurer-stand-02.png")]
        return slide

    def do_state_magic(self):
        self.mask = pygame.mask.from_surface(self.sprite)
        if self.rect[1] < 142:
            self.isJumping = True
            self.speed[1] += 0.05 
        else:
            self.isJumping = False
            self.speed[1] = 0

        
        if self.rect[1] > 142:
            self.rect[1] = 142
    
    def reset_position(self):
        self.rect[1] = 142