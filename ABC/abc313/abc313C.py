def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)
    minA , maxA =A[0],A[0]
    for a in A:
        minA = min(minA,a)
        maxA = max(maxA,a)
    print(minA,maxA)
    return 0


if __name__ == "__main__":
    main()
