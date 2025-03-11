def main():
    N, M = map(int,input().split())
    S = []
    for _ in range(N):
        rowS = list(input())
        S.append(rowS)
    results = []
    for i in range(N-8):
        for j in range(M-8):
            if S[i][j] == "#":
                if judgeNineBlock(i,j,S):
                    if RightDownNeighbor(i,j,S):
                        if judgeNineBlock(i+6,j+6,S):
                            if LeftUpNeighbor(i,j,S):
                                results.append([i+1,j+1])
    
    for res in results:
        print(*res)

    return 0

def judgeNineBlock(i, j , S) -> bool:
    if S[i][j+1] == "#" and S[i][j+2] == "#" and S[i+1][j] == "#" and S[i+1][j+1] == "#" and S[i+1][j+2] == "#" and S[i+2][j] == "#" and S[i+2][j+1]=="#" and S[i+2][j+2] == "#":
        return True
    return False

def RightDownNeighbor(i,j,S) -> bool:
    if S[i][j+3] == "." and S[i+1][j+3] == "." and S[i+2][j+3] == "." and S[i+3][j+3] == "." and S[i+3][j+2] == "." and S[i+3][j+1] == "." and S[i+3][j] == ".":
        return True
    return False

def LeftUpNeighbor(i,j,S) -> bool:
    if S[i+5][j+5] == "." and S[i+6][j+5] == "." and S[i+7][j+5] == "." and S[i+8][j+5] == "." and S[i+5][j+6] == "." and S[i+5][j+7] == "." and S[i+5][j+8] == ".":
        return True
    return False
if __name__ == "__main__":
    main()
