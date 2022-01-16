from nqueens import *

if __name__ == '__main__':
    problem1 = CP_NQueens(8)
    print(problem1)
    print(problem1.solve())
    print("Board: ")
    problem1.print_board()