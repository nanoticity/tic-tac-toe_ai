import pygame as pg
from color import *
from board import *
from mouse import *
pg.init()

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(Board.SIZE)

        self.board = Board(self.screen)
        self.mouse = Mouse()
    
    def run(self):
        run = True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
                if e.type == pg.MOUSEBUTTONDOWN:
                    b = self.mouse.which_box()
                    self.board.board[b[0]][b[1]] = "x"
                    
            self.screen.fill(Color.color("white"))
            self.board.draw()
            pg.display.update()
    