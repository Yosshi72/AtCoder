def main():
    N = int(input())
    board = [[] for _ in range(37)]

    for i in range(N):
        c = int(input())
        A = list(map(int,input().split()))

        for a in A:
            board[a].append([i+1,c])
    X = int(input())
    if len(board[X]):
        min_value = min(x[1] for x in board[X])
        result = [x[0] for x in board[X] if x[1] == min_value]
        print(len(result))
        print(*result)
        return
    print(0)
    print()
    return 0

if __name__ == "__main__":
    main()
