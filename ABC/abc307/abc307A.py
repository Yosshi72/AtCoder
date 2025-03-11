def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = []
    for i in range(N):
        partA = A[7 * i : 7 * (i + 1)]
        S.append(sum(partA))
    print(*S)
    return 0


if __name__ == "__main__":
    main()
