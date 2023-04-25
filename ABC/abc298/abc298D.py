def main():
    Q=int(input())
    S="1"
    for _ in range(Q):
        query=list(map(int,input().split()))
        if query[0]==1:
            S+=str(query[1])
        elif query[0]==2:
            S=S.strip(S[0])
        elif query[0]==3:
            num=int(S)
            num%=998244353
            print(num)
    return 0

if __name__=="__main__":
    main()