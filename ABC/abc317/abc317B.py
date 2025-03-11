def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    tmp = A[0]
    for i in range(1, len(A)):
        if A[i] - tmp != 1:
            print(tmp + 1)
            return
        tmp = A[i]
    return 0


if __name__ == "__main__":
    main()
