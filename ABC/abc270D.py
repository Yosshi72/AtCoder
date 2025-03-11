def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    index=K-1
    takahasi=0
    turn=True
    while index>=0:
        times=N//A[index]
        if turn==True:
            if times%2==0:
                takahasi+=A[index]*(times//2)
            else:
                takahasi+=A[index]*(times//2+1)
                turn=False
        else:
            takahasi+=A[index]*(times//2)
            if times%2==1:
                turn=True
        N-=A[index]*times
        index-=1
    print(takahasi)

if __name__=="__main__":
    main()