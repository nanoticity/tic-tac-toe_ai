import pygame as pg
screen = pg.display.set_mode((600, 600))

# Makes an imaginary 3x3 grid on the screen, checks which box it is in

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    x, y = pg.mouse.get_pos()
    if x in range(0, 201):
        if y in range(0, 201):
            print(0)
        elif y in range(201, 401):
            print(3)
        else:
            print(6)
    elif x in range(201, 401):
        if y in range(0, 201):
            print(1)
        elif y in range(201, 401):
            print(4)
        else:
            print(7)
    else:
        if y in range(0, 201):
            print(2)
        elif y in range(201, 401):
            print(5)
        else:
            print(8)