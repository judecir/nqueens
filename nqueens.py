from ortools.sat.python import cp_model
import chess

class CP_NQueens():
    def __init__(self, _nb_dim_board):
        self.model = cp_model.CpModel()
        self.nb_dim_board = _nb_dim_board
        # self.rg_dim_board =  range(1, self.nb_dim_board+1)
        self.vars = dict()
        self.solver = cp_model.CpSolver()

    def __str__(self):
        return f"{self.nb_dim_board}-Queens Problem"

    def variables(self):
        self.vars["row"] = {i: self.model.NewIntVar(lb=1, ub=self.nb_dim_board, name=f"row[{i}]") for i in
                            self.dim_board()}

    def constraints(self):
        for i in self.dim_board():
            for j in self.dim_board():
                if i < j:
                    # row
                    self.model.Add(self.vars["row"][i] != self.vars["row"][j])
                    # upward diagonal
                    self.model.Add(self.vars["row"][i] != self.vars["row"][j] + (j-i))
                    # downward diagonal
                    self.model.Add(self.vars["row"][i] != self.vars["row"][j] - (j-i))

        # self.model.AddAllDifferent([self.vars["row"][i] for i in self.nb_dim_board()])
        # self.model.AddAllDifferent([self.vars["row"][i] + i for i in self.nb_dim_board()])
        # self.model.AddAllDifferent([self.vars["row"][i] - i for i in self.nb_dim_board()])

    def modeling(self):
        self.variables()
        self.constraints()

    def solve(self):
        self.modeling()

        status = self.solver.Solve(self.model)
        if status == cp_model.OPTIMAL:
            print("Optimal")
            print([self.solver.Value(self.vars["row"][i]) for i in self.dim_board()])
        else:
            print(f"status={status}")

        return status

    def dim_board(self):
        return range(1, self.nb_dim_board + 1)

    def print_board(self):
        board = chess.Board()
        board.clear()

        # define queen
        queen = chess.Piece(piece_type=chess.QUEEN, color=chess.WHITE)
        for i in self.dim_board():
            square = (i-1)*8+self.solver.Value(self.vars["row"][i]) -1
            board.set_piece_at(square=square, piece=queen)

        return board