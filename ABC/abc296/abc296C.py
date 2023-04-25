def main():
    N,X=map(int,input().split())
    if X<0:
        X*=-1
    A=list(map(int,input().split()))
    sort_A=sorted(A)
    i=0
    j=0
    while True:
        if sort_A[j]-sort_A[i]<X:
            j+=1
        elif sort_A[j]-sort_A[i]>X:
            i+=1
        else:
            print("Yes")
            break
        if i ==N or j==N:
            print("No")
            break
if __name__=="__main__":
    main()