
from aux_functions import *
import chess


class Board():
    def __init__(self, solution):
        self.nb_dim_board

    # def print_board(self):
    #     board = chess.Board()
    #     board.clear()
    #
    #     # define queen
    #     queen = chess.Piece(piece_type=chess.QUEEN, color=chess.WHITE)
    #     for i in rg_dim_board(self.nb_dim_board):
    #         square = (i-1)*8+self.solver.Value(self.vars["row"][i]) -1
    #         board.set_piece_at(square=square, piece=queen)
    #
    #     return board