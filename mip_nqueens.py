from ortools.linear_solver import pywraplp

class MIP_NQueens():
    def __init__(self, nqueens):
        self.nqueens = nqueens
        self.model = pywraplp.Solver.CreateSolver("scip")

        self.vars = dict()

    def __str__(self):
        return f"{self.nqueens.n}-Queens Problem"

    def variables(self):
        self.vars["x"] = {(i, j): self.model.IntVar(lb=0, ub=1, name=f'x[{i, j}]')
                            for i in self.nqueens.get_rg_board()
                            for j in self.nqueens.get_rg_board()}


    def constraints(self):
        # one queen in each row
        for i in self.nqueens.get_rg_board():
            self.model.Add(sum(self.vars["x"][(i, j)] for j in self.nqueens.get_rg_board()) == 1)
        # one queen in each column
        for j in self.nqueens.get_rg_board():
            self.model.Add(sum(self.vars["x"][(i, j)] for i in self.nqueens.get_rg_board()) == 1)

    def objective_function(self):
        self.model.Maximize(sum(self.vars["x"][(i,j)] for j in self.nqueens.get_rg_board()(self.nqueens.n)
                                for i in self.nqueens.get_rg_board()(self.nqueens.n)))
    def modeling(self):
        self.variables()
        self.constraints()
        self.objective_function()

    def solve(self):
        self.modeling()
        print("Solving")
        #Solve
        status = self.model.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            print("Optimal")
            print([self.vars["x"][(i,j)].solution_value()
                    for i in self.nqueens.get_rg_board()
                    for j in self.nqueens.get_rg_board()])
        else:
            print(f"status={status}")

        return status