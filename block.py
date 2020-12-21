from pygame import *
width = 20
height = 20


class Plat(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((width, height))
        self.image = image.load('grass.png')
        self.rect = Rect(x, y, width, height)


class Spike(Plat):
    def __init__(self, x, y):
        Plat.__init__(self, x, y)
        self.image = image.load('saw.png')


class Trophey(Plat):
    def __init__(self, x, y):
        Plat.__init__(self, x, y)
        self.image = image.load('star.png')
