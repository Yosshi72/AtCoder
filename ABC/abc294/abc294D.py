def main():
    N, Q = map(int, input().split())
    non_call = 1
    called_but_nogone = {}
    for _ in range(Q):
        event = list(map(int, input().split()))
        if event[0] == 1:
            called_but_nogone[non_call]=0
            non_call += 1
        elif event[0] == 2:
            called_but_nogone.pop(event[1])
        elif event[0] == 3:
            for key in called_but_nogone.keys():
                print(key)
                break


if __name__ == "__main__":
    main()
