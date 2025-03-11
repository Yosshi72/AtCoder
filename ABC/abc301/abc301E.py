from collections import deque

def main():
    H,W,T=map(int,input().split())
    A=[]
    start=None
    goal=None
    candy=[]
    for h in range(H):
        A_row=list(input())
        A.append(A_row)
        for c in range(len(A_row)):
            if A_row[c]=="S":
                start=[h,c]
            elif A_row[c]=="G":
               goal=[h,c]
            elif A_row[c]=="o":
                candy.append([h,c])
    candy.insert(0, start)
    candy.insert(len(candy), goal)
    dists=[[0 if i==j else None for i in range(len(candy))]for j in range(len(candy))]
    for i,s in enumerate(candy):
        dist=bfs(A,s)
        for j,c in enumerate(candy):
            dists[i][j]=dist[c[0]][c[1]]
    print(dists)

def bfs(maze, start):
    INF = float("inf")
    h, w = len(maze), len(maze[0])
    dist = [[INF] * w for _ in range(h)]
    si, sj = start
    dist[si][sj] = 0
    queue = deque([(si, sj)])
    while queue:
        i, j = queue.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            if maze[ni][nj] == "#":
                continue
            if dist[ni][nj] != INF:
                continue
            dist[ni][nj] = dist[i][j] + 1
            queue.append((ni, nj))
    return dist

    
if __name__=="__main__":
    main()