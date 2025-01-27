from board import *
from math import factorial

class Move:
    def __init__(self, board, player, where):
        # Board before the move
        self.board = board
        self.where = where
        self.children = []
        self.player = player
        self.board_after = Move.compute_board_after_move(self)
        
    def board_after_move(self):
        return self.board_after

    # Given a board, return all the possible moves
    def possible_moves(board, player):
        possible = []
        for row, col, field in board.for_each_field():
            if field == " ":
                possible.append(Move(board, player, (row, col)))
        return possible

    def graph(self, file):
        file.write(f"""
                   
            {id(self.board)} -> {id(self.board_after)} [
            label = \"  {f"{self.board_after.score}p {self.player}:{self.where[0]},{self.where[1]}"}\"
            ]""")

    # Board after the move
    def compute_board_after_move(board):
        b = Board(board.board.display)
        b.board = board.board.clone()
        b.board[board.where[0]][board.where[1]] = board.player
        return b

    def __repr__(self) -> str:
        return f"{self.player}, {self.where}, {self.board_after .score}\n{self.board_after_move()}"

class Modeler:
    def set_tree(board, player):
        board.moves = Move.possible_moves(board, player)
        for move in board.moves:
            after_move = move.board_after_move()
            if not after_move.is_game_over():
                Modeler.set_tree(after_move, Board.other_player(player))
    
    # Score the tree from the perspective of the player            
    def score_tree(board, player):
        weight = factorial(board.empty_squares() + 1)
        if board.who_wins() == player:
            board.score = weight
        elif board.who_wins() == Board.other_player(player):
            board.score = -weight
        elif board.is_full():
            board.score = 0
        else:
            board.score = 0
            for m in board.moves:
                Modeler.score_tree(m.board_after, player)
                board.score += m.board_after.score       
    
    def find_best_move(board, player):
        Modeler.set_tree(board, player)
        Modeler.score_tree(board, player)
        best = board.moves[0]
        print("searching for best move:")
        for move in board.moves:
            print(move)
            if move.board_after.score > best.board_after.score:
                best = move
        print("best move: ", best)
        return best

if __name__ == "__main__":
    from board import *

    b = Board([['o', 'x', ' '], [' ', 'x', ' '], [' ', ' ', ' ']])
    b = Board([["x", "o", "x"], [" ", "o", " "], ["x", " ", " "]])

    moves = Move.possible_moves(b, "o")
    #assert [m.where for m in moves] == [(1, 1), (2, 0), (2, 1)]

    m = moves[0].board_after_move()
    ml = [["x", "o", "x"], ["o", "o", "x"], [" ", " ", "o"]]
    #assert Board(ml) == m
    #b.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "o"
    Modeler.set_tree(b, "o")
    Modeler.score_tree(b, "o")
    Modeler.find_best_move(b, "o")
    
    with open("moves.dot", "w") as file:
        file.write("digraph moves {")
        file.write("  rankdir=LR")
        file.write("""
        node [
            shape = "rect"
            style = "filled"
            fillcolor = "white"
        ]
                   """)
        b.graph_tree(file, "o")
        file.write("}")