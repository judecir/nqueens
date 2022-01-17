class Nqueens():
    def __init__(self, n):
        self.n = n
        self.solution = dict()
        self.fl_solution = False

    def __str__(self):
        r = f"{self.n}-Queens Problem"
        if self.fl_solution:
            r += "Solution: "
            r + str(self.solution)

        return r

    def get_rg_board(self):
        return range(1, self.n + 1)
