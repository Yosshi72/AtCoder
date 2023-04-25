import numpy as np
from scipy.sparse.csgraph import connected_components

def main():
    N,M=map(int,input().split())
    L=[[0 for _ in range(N)]for _ in range(N)]
    for _ in range(M):
        u,v=map(int,input().split())
        L[u-1][v-1]=1
        L[v-1][u-1]=1
    n, labels = connected_components(np.array(L))
    print(labels)

if __name__=="__main__":
    main()