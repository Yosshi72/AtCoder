def main():
    N,M=map(int,input().split())
    graph=[0 for _ in range(N)]

    for m in range(M):
        a,b = map(int,input().split())
        if a>b:
            graph[a-1]+=1
        else:
            graph[b-1]+=1

    count=0
    for g in graph:
        if g==1:
            count+=1
    print(count)
if __name__=="__main__":
    main()
    
