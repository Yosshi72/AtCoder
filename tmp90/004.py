import copy
import numpy as np

def main():
    H,W=map(int,input().split())
    A=[]
    row_sum=[]
    col_sum=[]

    for h in range(H):
        row=list(map(int,input().split()))
        A.append(row)
        row_sum.append(sum(row))
    A_T=np.array(copy.deepcopy(A)).T
    for w in range(W):
        col_sum.append(sum(A_T[w]))
    for h in range(H):
        b_row=[]
        for w in range(W):
            b_row.append(row_sum[h]+col_sum[w]-A[h][w])
        print(*b_row) 
if __name__=="__main__":
    main()
