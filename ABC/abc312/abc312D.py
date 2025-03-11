def main():
    S = input()
    result = count_valid_parentheses(S)
    print(result)
    return 0

def count_valid_parentheses(S):
    MOD = 998244353
    n = len(S)
    dp = [[0, 0] for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        c = S[i - 1]
        if c == '(':
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        elif c == ')':
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        else:  # c == '?'
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % MOD
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 2) % MOD
    print(dp)
    return dp[n][1]

if __name__ == "__main__":
    main()
