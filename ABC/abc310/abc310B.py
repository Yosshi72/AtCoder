def main():
    N, M = map(int, input().split())
    items = []
    for _ in range(N):
        items.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(i + 1, N):
            if items[i][0] <= items[j][0]:
                litem = items[i]
                hitem = items[j]
            else:
                litem = items[j]
                hitem = items[i]

            lfunc = litem[2:]
            hfunc = hitem[2:]

            if is_subset(hfunc, lfunc):
                if litem[0] < hitem[0] or litem[1] > hitem[1]:
                    print("Yes")
                    return 0
    print("No")
    return 0


def is_subset(a, b):
    return set(a).issubset(set(b))


if __name__ == "__main__":
    main()
