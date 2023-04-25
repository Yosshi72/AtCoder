def main():
    N,M=map(int,input().split())
    edges=[[float("inf") for _ in range(N+1)]for _ in range(N+1)]
    for n in range(1,N+1):
        edges[n][n]=0
    for _ in range(M):
        u,v=map(int,input().split())
        edges[u][v]=1
        edges[v][u]=1
    K=int(input())
    dists=warshall(N,edges)
    colors=[0 for _ in range(N+1)]
    for _ in range(K):
        p,min_d=map(int,input().split())
        d=dists[p]


def warshall(N:int,d:list)->list:
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

if __name__=="__main__":
    main()