def main():
    N = int(input())
    dp = [[0, 0] for _ in range(N + 1)]  # [health, stomach ache]
    for n in range(1, N + 1):
        x, y = map(int, input().split())
        if x == 0:
            dp[n][0] = max(dp[n - 1][0], dp[n - 1][0] + y, dp[n - 1][1] + y)
            dp[n][1] = dp[n - 1][1]
        else:
            dp[n][0] = dp[n - 1][0]
            dp[n][1] = max(dp[n - 1][0] + y, dp[n - 1][1])
    print(max(dp[N]))
    return 0


if __name__ == "__main__":
    main()
