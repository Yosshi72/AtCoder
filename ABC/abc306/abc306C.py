def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = {str(i): 0 for i in range(1, N + 1)}
    ans = []
    for i in range(3 * N):
        count[str(A[i])] += 1
        if count[str(A[i])] == 2:
            ans.append(A[i])
    print(*ans)


if __name__ == "__main__":
    main()
