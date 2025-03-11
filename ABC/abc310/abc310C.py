def main():
    N = int(input())
    S = {}
    for _ in range(N):
        s = input()
        inv_s = s[::-1]
        if not s in S.keys() and not inv_s in S.keys():
            S[s] = 0
    print(len(S))
    return 0


if __name__ == "__main__":
    main()
