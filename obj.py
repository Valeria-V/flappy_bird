import pygame

#extend class exist pygame
class Obj(pygame.sprite.Sprite):

    #get image
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x # 0 = position x
        self.rect[1] = y # 1 = position y