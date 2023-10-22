import pygame as pg
from color import *
from board import *
from mouse import *
pg.init()

class Game:
    def reset(self):
        self.playerx_turn = True
        self.board = Board(self.screen)
    def __init__(self):
        self.screen = pg.display.set_mode(Board.SIZE)
        self.reset()
        self.mouse = Mouse()
        self.clicked = False
    def text(self, to_write, pos, size, color):
        font = pg.font.Font(None, size)
        text = font.render(to_write, True, color)
        textpos = text.get_rect(centerx = pos[0], centery = pos[1])
        self.screen.blit(text, textpos)
    def run(self):
        run = True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
                if e.type == pg.KEYDOWN:
                    self.reset()
                if e.type == pg.MOUSEBUTTONDOWN and not self.clicked:
                    b = self.mouse.which_box()
                    if self.board.board[b[0]][b[1]] == " ":
                        if self.playerx_turn:
                            self.board.board[b[0]][b[1]] = "x"
                        else:
                            self.board.board[b[0]][b[1]] = "o"
                    
                        self.playerx_turn = not self.playerx_turn
                        winner = self.board.who_wins()
                        full = self.board.is_full()
                        message = None
                        if winner:
                            message = "The winner is " + winner.upper()
                        elif full:
                            message = "It is a tie"
                        if message:
                            self.board.draw()
                            self.text(message, (300, 300), 100, Color.color("red"))
                            pg.display.update()
                            pg.time.wait(3000)
                            self.reset()
                            
                    self.clicked = True
            self.screen.fill(Color.color("white"))
            self.board.draw()
            pg.display.update()
            self.clicked = False
    