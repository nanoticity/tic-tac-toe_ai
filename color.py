import pygame as pg
pg.init()

class Color:
    
    def color(name):
        col = name
        return pg.color.Color(str(col))