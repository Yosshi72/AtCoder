def main():
    N,M=map(int,input().split())
    friendship = [[0]* N for _ in range(N)]
    for _ in range(M):
        row = list(map(int,input().split()))
        for i in range(len(row)-1):
            friendship[row[i]-1][row[i+1]-1] = friendship[row[i+1]-1][row[i]-1] =1
    
    count = N*(N-1)
    for j in range(N):
        count -= sum(friendship[j])
    print(count//2)
if __name__=="__main__":
    main()