def main():
    N, P, Q = map(int, input().split())
    D = list(map(int, input().split()))

    print(min(P, Q + min(D)))
    return 0


if __name__ == "__main__":
    main()
