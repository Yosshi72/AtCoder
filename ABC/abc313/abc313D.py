def main():
    N, K = map(int, input().split())
    priA0 = ["?"] * (N + 1)
    priA1 = ["?"] * (N + 1)
    priA0[1] = 0
    priA1[1] = 1
    X = [(1 + j) % 5 for j in range(K)]
    print(createQuery(X))
    T = int(input())

    privT = T
    nowT = T

    for i in range(1, N):
        X = [1+(i + j) % N for j in range(K)]
        X =sorted(X)
        print(createQuery(X))
        T = int(input())

        privT, nowT = nowT, T
        print(X[-1],(X[0]-1) % (N))
        if privT == nowT:
            priA0[X[-1]] = priA0[(X[0]-1) % (N)]
            priA1[X[-1]] = priA1[(X[0]-1) % (N)]
        else:
            priA0[X[-1]] = (priA0[(X[0]-1) % (N)]+1 ) % 2
            priA1[X[-1]] = (priA1[(X[0]-1) % (N)] +1) % 2
        print(priA0, priA1)
    return 0


def createQuery(X) -> str:
    query = "?"
    for x in X:
        query += " " + str(x)
    return query


if __name__ == "__main__":
    main()
