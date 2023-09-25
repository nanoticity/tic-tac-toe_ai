import pygame as pg
from color import *
pg.init()

class Board:
    SIZE = [600, 600]
    def __init__(self, display):
        self.display = display
        self.board = [["x", " ", " "],
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
    
    def draw_x(self, pos):
        middle_pos = (pos[1] * (Board.SIZE[0] / 3) + Board.SIZE[0] / 6, pos[0] * (Board.SIZE[1] / 3) + Board.SIZE[1] / 6) 
        points = [middle_pos, (middle_pos[0] - 75, middle_pos[1] - 75), middle_pos, (middle_pos[0] + 75, middle_pos[1] - 75), middle_pos, (middle_pos[0] + 75, middle_pos[1] + 75), middle_pos, (middle_pos[0] - 75, middle_pos[1] + 75)]
        # box = 2
        # 1. box + (box + 1)
        # box = 5
        # 2. box * 100
        # box = 500
        pg.draw.polygon(self.display, Color.color("black"), points, 10)