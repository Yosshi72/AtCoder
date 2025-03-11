def main():
    N, H, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i, p in enumerate(P):
        if p + H >= X:
            print(i + 1)
            return

    return 0


if __name__ == "__main__":
    main()
