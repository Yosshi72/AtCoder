def main():
    N,S=map(int,input().split())
    dp=[[[False,""] for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0][0]=True
    for n in range(1,N+1):
        a,b=map(int,input().split())
        for s in range(S+1):
            if dp[n-1][s][0]==True:
                if s+a>S and s+b>S:
                    break
                if s+a<=S:
                    dp[n][s+a][0]=True
                    dp[n][s+a][1]=dp[n-1][s][1]
                    dp[n][s+a][1]+="H"
                if s+b<=S:
                    dp[n][s+b][0]=True
                    dp[n][s+b][1]=dp[n-1][s][1]
                    dp[n][s+b][1]+="T"
    if dp[N][S][0]==True:
        print("Yes")
        print(dp[N][S][1])
    else:
        print("No")

if __name__=="__main__":
    main()
