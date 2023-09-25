import pygame as pg
from board import *
pg.init()

class Mouse:
    def __init__(self):
        self.x, self.y = pg.mouse.get_pos()
    
    def which_box(self):
        self.x, self.y = pg.mouse.get_pos()
        x_pos = int(self.x / (Board.SIZE[0] / 3))
        y_pos = int(self.y / (Board.SIZE[1] / 3))
        return (y_pos, x_pos)
        