from board import *

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
        return f"{self.player}, {self.where}\n{self.board_after_move()}"

class Modeler:
    def set_tree(self, board, player):
        board.moves = Move.possible_moves(board, player)
        for move in board.moves:
            after_move = move.board_after_move()
            if not after_move.is_game_over():
                self.set_tree(after_move, Board.other_player(player))
                
    def score_tree(self, board, player):
        if board.who_wins() == player:
            board.score = 1
        elif board.who_wins() == Board.other_player(player):
            board.score = -1
        elif board.is_full():
            board.score = 0
        else:
            board.score = 0
            for m in board.moves:
                self.score_tree(m.board_after, player)
                board.score += m.board_after.score
    
    def find_best_move(self, board):
        self.set_tree()
        self.score_tree()
        best = board.moves[0]
        for move in board.moves:
            if move.board.score > best.board.score:
                best = move.board.score
                
        return best

if __name__ == "__main__":
    from board import *

    b = Board([["x", "o", "x"], ["o", " ", "x"], [" ", " ", "o"]])

    moves = Move.possible_moves(b, "o")
    assert [m.where for m in moves] == [(1, 1), (2, 0), (2, 1)]

    m = moves[0].board_after_move()
    ml = [["x", "o", "x"], ["o", "o", "x"], [" ", " ", "o"]]
    assert Board(ml) == m
    #b.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "o"
    modeler = Modeler()
    modeler.set_tree(b, "o")
    modeler.score_tree(b, "o")
    
    with open("moves.dot", "w") as file:
        file.write("digraph moves {")
        file.write("""
        node [
            shape = "rect"
            style = "filled"
            fillcolor = "white"
        ]
                   """)
        b.graph_tree(file)
        file.write("}")