def main():
    N = int(input())
    S = list(input())
    Q = int(input())

    upper_or_lower = 0
    window = []
    for _ in range(Q):
        t, x, c = map(str, input().split())
        t, x = int(t), int(x)
        if t == 1 :
            window.append([x-1,c])
        else: 
            upper_or_lower = t
            for w in window:
                S[w[0]] = w[1]
            window = []
    S = "".join(S)
    if upper_or_lower == 2:
        S = S.lower()
    elif upper_or_lower == 3:
        S = S.upper()
    S = list(S)
    for w in window:
        S[w[0]] = w[1]
    print(*S, sep ="")
    return 0


if __name__ == "__main__":
    main()
