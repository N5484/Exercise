import pygame, sys
from pygame import *
from pygame.locals import QUIT

pygame.init()
WIDTH = 1600
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
x = 600  # 
y = 350  # square coordinates
a = 50  # square size
r = 0
g = 255
b = 255
rgb = [r, g, b] # colors
step = 0

clock = time.Clock()
while True:
    screen.blit(image.load('ve.png'), (20, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_p:
                pygame.image.save(screen, "screenshot.jpeg")
            if event.key == K_c:    # clear the screen
                screen.fill((0, 0, 0))  
        
        elif event.type == MOUSEWHEEL:    # resize the square
            if event.y < 0:
                a += 8
                x -= 4
                y -= 4
            elif a >= 12:
                a -= 8
                x += 4
                y += 4
    keys = pygame.key.get_pressed()

    def move(k1, k2, c, v, n):      # move square
        if (keys[k1] or keys[k2]) and c:
            v += n
        return v

    start = (x, y)
    
    x = move(K_RIGHT, K_d, x < WIDTH, x, 5)       # right
    x = move(K_LEFT, K_a, x > 0, x, -5)           # left
    y = move(K_DOWN, K_s, y < HEIGHT, y, 5)       # down
    y = move(K_UP, K_w, y > 0, y, -5)             # up
    
    if (x, y) != start:           # change color
        if rgb[step] <= 253:
            rgb[step] += 2
            if step < 2:
                rgb[step + 1] -= 2
            else:
                rgb[0] -= 2
        elif step == 2:
            step = 0
        else:
            step += 1

    draw.rect(screen, (rgb[0], rgb[1], rgb[2]), (x, y, a, a), 1)
    display.update()
    clock.tick(11)

    pygame.display.update()