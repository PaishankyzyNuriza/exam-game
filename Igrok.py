from pygame import *
import block
from game import screen
import pygame
win = False
speed = 8
width = 20
height = 20
jump = 10
gravitation = 0.9


class Igrok(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.speedX = 0
        self.speedY = 0
        self.naZemle = False
        self.startX = x
        self.startY = y
        self.image = Surface((width, height))
        self.image = image.load('alienGreen_stand_.png')
        self.rect = Rect(x, y, width, height)

    def update(self, levo, pravo, verh, platform):
        if verh:
            if self.naZemle:
                self.speedY = -jump

        if levo:
            self.speedX = -speed

        if pravo:
            self.speedX = speed

        if not (pravo or levo):
            self.speedX = 0

        if not self.naZemle:
            self.speedY = self.speedY + gravitation

        self.naZemle = False
        self.rect.y = self.rect.y + self.speedY
        self.collision(0, self.speedY, platform)
        self.rect.x = self.rect.x + self.speedX
        self.collision(self.speedX, 0, platform)

    def collision(self, speedX, speedY, platform):
        for n in platform:
            if sprite.collide_rect(self, n):
                if isinstance(n, block.Spike):
                    self.death()
                if isinstance(n, block.Trophey):
                    win = True
                    if win == if cond is True:
                        t = pygame.font.Font(None, 80)
                        text = t.render('You Win!!!', 3, (0, 0, 0))
                        screen.blit(text, (250, 250))
                if speedX > 0:
                    self.rect.right = n.rect.left

                if speedX < 0:
                    self.rect.left = n.rect.right

                if speedY > 0:
                    self.rect.bottom = n.rect.top
                    self.naZemle = True
                    self.speedY = 0

                if speedY < 0:
                    self.rect.top = n.rect.bottom
                    self.speedY = 0

    def death(self):
        time.wait(600)
        self.teleport(self.startX, self.startY)

    def teleport(self, X, Y):
        self.rect.x = X
        self.rect.y = Y
