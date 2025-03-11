def main():
    N = int(input())
    info = []
    totalZ = 0
    takahashiZ = 0 
    for _ in range(N):
        x, y, z = map(int,input().split())
        if x > y :
            takahashiZ += z
        else:
            info.append([((x+y)//2)+1-x,z])
        totalZ += z
    wantZ = (totalZ//2)+1-takahashiZ
    if wantZ <=0 :
        print(0)
        return 

    dp = [["inf"]* (wantZ+1) for _ in range(N)]
    for n in range(N):
        for i in range(len(dp[n])):
            if 
    print(wantZ,info)
    return 0

if __name__ == "__main__":
    main()
