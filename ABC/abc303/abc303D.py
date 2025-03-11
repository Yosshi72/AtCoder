def main():
    X, Y, Z = map(int, input().split())
    S = input()

    dp_table = [[float("inf")] * 2 for _ in range(len(S) + 1)]
    dp_table[0][0] = 0
    for i in range(len(S)):
        if S[i] == "a":
            dp_table[i + 1][0] = min(dp_table[i][0] + X, dp_table[i][1] + X + Z)
            dp_table[i + 1][1] = min(dp_table[i][1] + Y, dp_table[i][0] + X + Z)
        else:
            dp_table[i + 1][0] = min(dp_table[i][1] + X + Z, dp_table[i][0] + Y)
            dp_table[i + 1][1] = min(dp_table[i][0] + X + Z, dp_table[i][1] + X)
    print(min(dp_table[len(S)]))


if __name__ == "__main__":
    main()
