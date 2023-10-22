import pygame as pg
from color import *
pg.init()

class Board:
    SIZE = [600, 600]
    def __init__(self, display):
        self.display = display
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
    
    def draw(self):
        for i in range(1, 3):
            pg.draw.line(self.display, Color.color("black"), (int(i * (self.SIZE[0] / 3)), 0), (int(i * (self.SIZE[0] / 3)), self.SIZE[1]))
        for i in range(1, 3):
            pg.draw.line(self.display, Color.color("black"), (0, int(i * (self.SIZE[1] / 3))), (self.SIZE[0], int(i * (self.SIZE[1] / 3))))
            
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == "x":
                    self.draw_x((row, col))
                elif self.board[row][col] == "o":
                    self.draw_o((row, col))
    
    def draw_x(self, pos):
        middle_pos = (pos[1] * (Board.SIZE[0] / 3) + Board.SIZE[0] / 6, pos[0] * (Board.SIZE[1] / 3) + Board.SIZE[1] / 6) 
        points = [middle_pos, (middle_pos[0] - 75, middle_pos[1] - 75), middle_pos, (middle_pos[0] + 75, middle_pos[1] - 75), middle_pos, (middle_pos[0] + 75, middle_pos[1] + 75), middle_pos, (middle_pos[0] - 75, middle_pos[1] + 75)]
        # box = 2
        # 1. box + (box + 1)
        # box = 5
        # 2. box * 100
        # box = 500
        pg.draw.polygon(self.display, Color.color("black"), points, 10)
    
    def draw_o(self, pos):
        middle_pos = (pos[1] * (Board.SIZE[0] / 3) + Board.SIZE[0] / 6, pos[0] * (Board.SIZE[1] / 3) + Board.SIZE[1] / 6)
        pg.draw.circle(self.display, Color.color("black"), middle_pos, 75, 10)
    
    def is_full(self):
        for row in self.board:
            for field in row:
                if field == " ":
                    return False
        return True
    
    def _who_wins(self):
        for row in self.board:
            if row[0] == row[1] and row[0] == row[2]:
                return row[0]
        for col in range(len(self.board[0])):
            if self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col]:
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return self.board[0][2]
        return None
    
    def who_wins(self):
        w = self._who_wins()
        if w == " " or w == None:
            return None
        else:
            return w

if __name__ == "__main__":
    b = Board("")
    b.board = [["x", "o", "x"],
               ["x", "o", "o"],
               ["x", "x", "o"]]
    assert b.who_wins() == "x"
    b.board = [["o", "o", "x"],
               ["o", "o", "o"],
               ["x", "x", "o"]]
    assert b.who_wins() == "o"
    b.board = [["o", "o", "x"],
               ["x", "o", "o"],
               ["x", "x", "o"]]
    assert b.who_wins() == "o"
    b.board = [["o", "o", "x"],
               ["x", "o", "o"],
               ["o", "x", "x"]]
    assert b.who_wins() == None
    b.board = [["o", "o", "x"],
               ["x", "o", "o"],
               ["o", "x", "x"]]
    assert b.is_full() == True
    b.board = [[" ", "o", "x"],
               ["x", "o", "o"],
               ["o", "x", "x"]]
    assert b.is_full() == False
