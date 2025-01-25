import pygame as pg
from color import *
from board import *
from mouse import *
from modeler import *
pg.init()

class Game:
    def reset(self):
        self.board = Board(display=self.screen)
        # self.board.board = [["x", "o", "x"], ["o", " ", " "], [" ", " ", " "]]
    def __init__(self):
        self.screen = pg.display.set_mode(Board.SIZE)
        self.reset()
        self.mouse = Mouse()
        self.clicked = False
        self.ai_turn = False
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
                        print(self.ai_turn)
                        if not self.ai_turn:
                            self.clicked = True 
                            self.board.board[b[0]][b[1]] = "x"
                            self.ai_turn = True
                        
            if self.ai_turn and not self.clicked:
                best_move = Modeler.find_best_move(self.board, "o")
                print(best_move)
                best_move_x = best_move.where[0]
                best_move_y = best_move.where[1]
                self.board.board[best_move_x][best_move_y] = best_move.player
                print(self.board.board)
                self.ai_turn = False
            
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
                
            self.screen.fill(Color.color("white"))
            self.board.draw()
            pg.display.update()
            self.clicked = False
    