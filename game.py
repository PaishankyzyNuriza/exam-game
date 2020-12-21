import pygame
from pygame import *
from Igrok import *
from block import *


WIDTH = 800
HEIGHT = 600
DISPLAY = (WIDTH, HEIGHT)
Platform_wid = 20
Platform_hei = 20
Platform_block = (Platform_wid, Platform_hei)
screen = pygame.display.set_mode(DISPLAY)


def main():
    pygame.init()
    pygame.display.set_caption("Platformer")
    BG = pygame.image.load('colored_land.png')
    screen.blit(BG, (0, 0))
    pygame.display.flip()

    player = Igrok(25, 560)
    levo = pravo = False
    verh = False

    hitGround = pygame.sprite.Group()
    platform = []
    hitGround.add(player)
    level1 = [
        "----------------------------------------",
        "-                                      -",
        "-                                      -",
        "-              ---     --             *-",
        "-        ------       -     --    ------",
        "-                                      -",
        "------                           /     -",
        "-                                      -",
        "-------------///------------     -------",
        "-                                      -",
        "-                                      -",
        "-                    -------------------",
        "-                                      -",
        "---      ------   ----                 -",
        "-                     -  ------      ---",
        "-      ---             -               -",
        "-                       -         --   -",
        "- --/--                   -            -",
        "-      /                   /           -",
        "-       /                              -",
        "--       -------               -       -",
        "-                   -------            -",
        "-                                      -",
        "--                              --------",
        "-                                      -",
        "-                 -----                -",
        "----------///-----     -----///-----   -",
        "-                                      -",
        "-                                      -",
        "-------------------///------------------"]
    x = 0
    y = 0

    for j in level1:
        for k in j:
            if k == "-":
                plat = Plat(x, y)
                hitGround.add(plat)
                platform.append(plat)
            if k == "/":
                spike = Spike(x, y)
                hitGround.add(spike)
                platform.append(spike)
            if k == "*":
                star = Trophey(x, y)
                hitGround.add(star)
                platform.append(star)
            x = x + Platform_wid
        y = y + Platform_hei
        x = 0

    s = True
    while s:
        pygame.time.Clock().tick(30)
        for q in pygame.event.get():
            if q.type == QUIT:
                s = False
            if q.type == KEYDOWN and q.key == K_LEFT:
                levo = True
            if q.type == KEYDOWN and q.key == K_RIGHT:
                pravo = True
            if q.type == KEYUP and q.key == K_LEFT:
                levo = False
            if q.type == KEYUP and q.key == K_RIGHT:
                pravo = False
            if q.type == KEYDOWN and q.key == K_UP:
                verh = True
            if q.type == KEYUP and q.key == K_UP:
                verh = False
        pygame.display.update()
        screen.blit(BG, (0, 0))
        hitGround.draw(screen)
        player.update(levo, pravo, verh, platform)


if __name__ == "__main__":
    main()
