import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    sumA = [0]
    for a in range(1, len(A) - 1):
        if a % 2 == 1:
            sumA.append(sumA[-1] + A[a + 1] - A[a])
        else:
            sumA.append(sumA[-1])
    for _ in range(Q):
        sleepTime = 0
        l, r = map(int, input().split())

        indexLeft = bisect.bisect(A, l)
        indexRight = bisect.bisect(A, r)
        if indexLeft % 2 == 0:
            sleepTime += l - A[indexLeft-1]
        sleepTime += sumA[indexRight - 1] - sumA[indexLeft - 1]
        if indexRight %2 ==0:
            sleepTime -= (A[indexRight]-r)
        print(sleepTime)

    return 0


if __name__ == "__main__":
    main()
