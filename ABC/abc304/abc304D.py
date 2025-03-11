import bisect


def main():
    W, H = map(int, input().split())
    N = int(input())
    strawberries = []
    for _ in range(N):
        p, q = map(int, input().split())
        strawberries.append([p, q])
    A = int(input())
    a = list(map(int, input().split()))
    B = int(input())
    b = list(map(int, input().split()))

    min_straw = N + 1
    max_straw = 0
    pieces = [[0] * (A + 1) for _ in range(B + 1)]
    for p in strawberries:
        x = p[0]
        y = p[1]
        piece_x = bisect.bisect(a, x)
        piece_y = bisect.bisect(b, y)
        pieces[piece_x][piece_y] += 1

    count = 0
    for piece in pieces:
        for p in piece:
            if p < min_straw:
                min_straw = p
            if p > max_straw:
                max_straw = p
            count += p
            if count == N:
                print(min_straw, max_straw)
                return
    print(min_straw, max_straw)


if __name__ == "__main__":
    main()
