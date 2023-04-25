def main():
    N,T=map(int,input().split())
    C=list(map(int,input().split()))
    R=list(map(int,input().split()))
    color_T=[]
    color_1=[]
    for i,c in enumerate(C):
        if c==T:
            color_T.append([R[i],i])
        if c==C[0]:   
            color_1.append([R[i],i])
    if len(color_T)!=0:
        winner=max(color_T)
        print(winner[1]+1)
    else:
        winner=max(color_1)
        print(winner[1]+1)

if __name__=="__main__":
    main()