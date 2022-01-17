from cp_nqueens import *
from mip_nqueens import *
from nqueens import *
from board import *

if __name__ == '__main__':
    n = 8
    print("CP")
    cp = CP_NQueens(n)
    print(cp)
    print(cp.solve())


    # print("MIP")
    # mip = MIP_NQueens(n)
    # print(mip)
    # print(mip.solve())