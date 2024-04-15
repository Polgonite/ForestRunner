import pygame
import math

spritePath = "game\\assets\\Background layers\\"

class gameEnvironment():
    
    def __init__(self) -> None:
        
        self.layer00 = self.load_layer("Layer_0000_9.png")
        self.layer01 = self.load_layer("Layer_0001_8.png")
        self.layer02 = self.load_layer("Layer_0002_7.png")
        self.layer03 = self.load_layer("Layer_0003_6.png")
        self.layer04 = self.load_layer("Layer_0004_Lights.png")
        self.layer05 = self.load_layer("Layer_0005_5.png")
        self.layer06 = self.load_layer("Layer_0006_4.png")
        self.layer07 = self.load_layer("Layer_0007_Lights.png")
        self.layer08 = self.load_layer("Layer_0008_3.png")
        self.layer09 = self.load_layer("Layer_0009_2.png")
        self.layer10 = self.load_layer("Layer_0010_1.png")
        self.layer11 = self.load_layer("Layer_0011_0.png")

        self.layers = []
        self.layers.append(self.layer00)
        self.layers.append(self.layer01)
        self.layers.append(self.layer02)
        self.layers.append(self.layer03)
        self.layers.append(self.layer04)
        self.layers.append(self.layer05)
        self.layers.append(self.layer06)
        self.layers.append(self.layer07)
        self.layers.append(self.layer08)
        self.layers.append(self.layer09)
        self.layers.append(self.layer10)
        self.layers.append(self.layer11)

    def load_layer(self, filename):
        layer = pygame.image.load(spritePath + filename)
        return layer

    def background(self):
        return self.layer01
