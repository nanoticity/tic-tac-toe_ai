from board import *


class Move:

    def __init__(self, board, player, where):
        # Board before the move
        self.board = board
        self.where = where
        self.children = []
        self.player = player

    # Given a board, return all the possible moves
    def possible_moves(board, player):
        possible = []
        for row, col, field in board.for_each_field():
            if field == " ":
                possible.append(Move(board, player, (row, col)))
        return possible

    # Board after the move
    def board_after_move(self):
        b = Board(self.board.display)
        b.board = self.board.clone()
        b.board[self.where[0]][self.where[1]] = self.player
        return b


class Modeler:
    def __init__(self, machine_player, board=Board()):
        self.board = board
        self.machine_player = machine_player

    def other_player(player):
        if player == "x":
            return "o"
        else:
            assert player == "o"
            return "x"

    def set_tree(board, player):
        board.moves = Move.possible_moves(board, player)
        for move in board.moves:
            after_move = move.board_after_move()
            if not after_move.is_game_over():
                Modeler.set_tree(after_move, Modeler.other_player(player))

    # def score_tree


if __name__ == "__main__":
    from board import *

    b = Board("")
    b.board = [["x", "o", "x"], ["o", " ", "x"], [" ", " ", "o"]]

    moves = Move.possible_moves(b, "o")
    assert [m.where for m in moves] == [(1, 1), (2, 0), (2, 1)]

    m = moves[0].board_after_move()
    ml = [["x", "o", "x"], ["o", "o", "x"], [" ", " ", "o"]]
    assert Board(ml) == m

    Modeler.set_tree(b, "o")
    print(b)
