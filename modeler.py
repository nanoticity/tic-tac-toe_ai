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

    def graphviz_move(self, num):
        string = f"""{num} [
            label = "{self.board_after_move()}"
        ]
        start -> {num} [label = " {f"{self.player}: ({self.where[0]}, {self.where[1]})"}"]
        """
        return string
    
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
    def set_tree(board, player):
        board.moves = Move.possible_moves(board, player)
        for move in board.moves:
            after_move = move.board_after_move()
            if not after_move.is_game_over():
                Modeler.set_tree(after_move, Board.other_player(player))

if __name__ == "__main__":
    from board import *

    b = Board([["x", "o", "x"], ["o", " ", "x"], [" ", " ", "o"]])

    moves = Move.possible_moves(b, "o")
    assert [m.where for m in moves] == [(1, 1), (2, 0), (2, 1)]

    m = moves[0].board_after_move()
    ml = [["x", "o", "x"], ["o", "o", "x"], [" ", " ", "o"]]
    assert Board(ml) == m
    b.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "o"
    Modeler.set_tree(b, "o")
    b.score_tree("o")
    
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
"""
    Modeler.set_tree(b, "x")
    print(b.graphviz_possible_moves())
    with open("moves.dot", "w") as file:
        file.write(b.graphviz_possible_moves())

    Modeler.set_tree(b, "o")
    with open("tree.dot", "w") as file:
        file.write(b.graph_move_tree())

"""
