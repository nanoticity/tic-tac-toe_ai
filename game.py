import pygame as pg
from color import *
from board import *
from mouse import *
from modeler import *
import asyncio
pg.init()

class Game:
    def reset(self):
        self.board = Board(display=self.screen)
        self.board.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    def __init__(self):
        self.screen = pg.display.set_mode([Board.SIZE[0] + 200, Board.SIZE[1]])
        pg.display.set_caption("Tic Tac Toe!")
        self.reset()
        self.mouse = Mouse()
        self.clicked = False
        self.ai_turn = False
    def text(self, to_write, pos, size, color):
        font = pg.font.Font(None, size)
        text = font.render(to_write, True, color)
        textpos = text.get_rect(centerx = pos[0], centery = pos[1])
        self.screen.blit(text, textpos)
    
    async def title(self):
        title = True
        while title:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    title = False
                if e.type == pg.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        title = False
            self.screen.fill(Color.color("white"))
            self.text("Tic Tac Toe! By Nano", (400, 100), 100, Color.color("black"))
            self.text("Click anywhere on the screen to play.", (400, 200), 50, Color.color("black"))
            self.text("Made with Pygame and Pyodide", (400, 300), 35, Color.color("black"))
            self.text("Repo: https://github.com/nanoticity/tic-tac-toe_ai", (400, 350), 35, Color.color("black"))
            self.text("I think you know how to play", (400, 400), 35, Color.color("black"))
            self.text("But with an unbeateble AI", (400, 450), 35, Color.color("black"))
            self.text("Good luck beating it!", (400, 500), 35, Color.color("black"))
            self.text("For High Seas 2024-2025", (400, 550), 35, Color.color("black"))
            pg.display.update()
            await asyncio.sleep(0.02)
        
    async def run(self):
        await self.title()
        probs = [58, 13, 29]
        run = True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
                if e.type == pg.MOUSEBUTTONDOWN and not self.clicked:
                    b = self.mouse.which_box()
                    if self.board.board[b[0]][b[1]] == " ":
                        if not self.ai_turn:
                            self.clicked = True 
                            self.board.board[b[0]][b[1]] = "x"
                            self.ai_turn = True
                        
            if self.ai_turn and not self.clicked:
                best_move = Modeler.find_best_move(self.board, "o")
                best_move_x = best_move.where[0]
                best_move_y = best_move.where[1]
                self.board.board[best_move_x][best_move_y] = best_move.player
                Modeler.set_tree(self.board, "x")
                Modeler.score_tree(self.board, "x")
                probs = list(Modeler.compute_probs(self.board))
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
                await asyncio.sleep(3)
                run = False 
                
            self.screen.fill(Color.color("white"))
            self.board.draw()
            pg.draw.line(self.screen, Color.color("black"), (600, 0), (600, 600), 10)
            self.text("Live Chances", (705, 40), 37, Color.color("black"))
            self.text("Win: " + str(probs[0]) + "%", (700, 150), 50, Color.color("darkolivegreen4"))
            self.text("Tie: " + str(probs[1]) + "%", (700, 300), 50, Color.color("gold3"))
            self.text("Loss: " + str(probs[2]) + "%", (700, 450), 50, Color.color("orangered3"))
            pg.display.update()
            self.clicked = False
            await asyncio.sleep(0.02)
    