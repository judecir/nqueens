from ortools.sat.python import cp_model

class CP_NQueens():
    def __init__(self, nqueens):
        self.nqueens = nqueens
        self.model = cp_model.CpModel()
        
        self.vars = dict()
        self.solver = cp_model.CpSolver()

    def __str__(self):
        return f"{self.nqueens.n}-Queens Problem"

    def variables(self):
        self.vars["row"] = {i: self.model.NewIntVar(lb=1, ub=self.nqueens.n, name=f"row[{i}]") for i in
                            self.nqueens.get_rg_board()}

    def constraints(self):
        # columns different
        self.model.AddAllDifferent([self.vars["row"][i] for i in self.nqueens.get_rg_board()])
        # upward diagonal different
        self.model.AddAllDifferent([self.vars["row"][i] + i for i in self.nqueens.get_rg_board()])
        # downward diagonal different
        self.model.AddAllDifferent([self.vars["row"][i] - i for i in self.nqueens.get_rg_board()])

    def modeling(self):
        self.variables()
        self.constraints()

    def solve(self):
        self.modeling()

        status = self.solver.Solve(self.model)
        if status == cp_model.OPTIMAL:
            print("Optimal")
            print([self.solver.Value(self.vars["row"][i]) for i in self.nqueens.get_rg_board()])
        else:
            print(f"status={status}")

        return status

