import pygame
import random
pygame.init()

x,y=600,400
window= pygame.display.set_mode((x,y))
pygame.display.set_caption("GAME")

green = (200,255,0)
blk = (200,200,200)
blu = (255,255,0)

clock = pygame.time.Clock()

def values():
    speed = [random.randint(1,10),random.randint(1,10)]
    radius = random.randint(1,30)
    colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    pos = [random.randint(radius,x-radius),random.randint(radius,y-radius)]
    return {"SP":speed,"RAD":radius,"COL":colour,"POS":pos}

ball_num = [values() for i in range(20)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.fill(green)
    for ball in ball_num:
        ball["POS"][0] += ball["SP"][0]
        ball["POS"][1] += ball["SP"][1]

        if ball["POS"][0] <= 0 or ball["POS"][0] >= x:
            ball["SP"][0] =- ball["SP"][0]
        if ball["POS"][1] <= 0 or ball["POS"][1] >= y:
            ball["SP"][1] = - ball["SP"][1]

        pygame.draw.circle(window, ball["COL"], (ball['POS'][0], ball['POS'][1]), ball['RAD'])

    clock.tick(20)
    pygame.display.update()