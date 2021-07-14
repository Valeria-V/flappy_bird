import pygame

class Main:

    def __init__(self):

        self.window = pygame.display.set_mode([360,640]) #windows and display
        self.tittle = pygame.display.set_caption("Flappy Bird") #tittle game

        #variables
        self.loop = True
        self.fps = pygame.time.Clock()

    #function close display
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    #function draw
    def draw(self):
        pass

    #function update
    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()

Main().update()