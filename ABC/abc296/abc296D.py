def main():
    N,M=map(int,input().split())
    X=[]
    for a in range(1,N+1):
        b=int(M/a)
        if a*b!=M:
            b+=1
        if a>b:
            break
        if b<=N:
            X.append(a*b)
    if len(X)==0:
        print(-1)
    else:
        print(min(X))
if __name__=="__main__":
    main()