def main():
    N=int(input())
    A=[]
    B=[]
    for n in range(N):
        A.append(list(map(int,input().split())))
    for n in range(N):
        B.append(list(map(int,input().split())))
    rotate_A=rotate(N,A)
    flag=[True for _ in range(4)]
    for k in range(4):
        for i in range(N):
            for j in range(N):
                if rotate_A[k][i][j]==1 and B[i][j]!=1:
                    flag[k]=False
    if True in flag:
        print("Yes")
        return 0
    print("No")

def rotate(N:int,A:list)->list:
    rotate_A=[[[0 for _ in range(N)]for _ in range(N)] for _ in range(4)]
    for i in range(N):
        for j in range(N):
            if A[i][j]==1:
                rotate_A[0][i][j]=1
                rotate_A[1][N-1-j][i]=1
                rotate_A[2][N-1-i][N-1-j]=1
                rotate_A[3][j][N-1-i]=1
    return rotate_A
if __name__=="__main__":
    main()