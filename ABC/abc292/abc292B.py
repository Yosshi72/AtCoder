def main():
    N, Q = map(int, input().split())
    flags = [0 for _ in range(N)]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            flags[x-1] += 1
        elif c == 2:
            flags[x-1] += 2
        elif c == 3:
            if flags[x-1] >= 2:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
