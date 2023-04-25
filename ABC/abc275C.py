def main():
    point = []
    for i in range(9):
        S = list(input())
        for j, s in enumerate(S):
            if s == "#":
                point.append([i, j])
    count = 0
    for i0 in range(len(point) - 3):
        for i1 in range(i0 + 1, len(point) - 2):
            for i2 in range(i1 + 1, len(point) - 1):
                d0 = distance(point[i0], point[i1])
                d1 = distance(point[i0], point[i2])
                d2 = distance(point[i1], point[i2])
                if not judge3([d0, d1, d2]):
                    continue
                for i3 in range(i2 + 1, len(point)):
                    d3 = distance(point[i0], point[i3])
                    d4 = distance(point[i1], point[i3])
                    d5 = distance(point[i2], point[i3])
                    flag = judge4([d0, d1, d2, d3, d4, d5])
                    if flag:
                        count += 1

    print(count)


def distance(a: list, b: list) -> int:
    x0, y0 = a
    x1, y1 = b
    d = (x1 - x0) ** 2 + (y1 - y0) ** 2
    return d


def judge3(dists: list) -> bool:
    d0, d1, d2 = sorted(dists)
    if d0 == d1:
        if d2 == 2 * d0 or d2 == d0:
            return True
    if d1 == d2:
        if d1 == 2 * d0:
            return True
    return False


def judge4(dists: list) -> bool:
    d0, d1, d2, d3, d4, d5 = sorted(dists)
    if d0 == d1 == d2 == d3:
        if d4 == d5:
            if d4 == 2 * d0:
                return True
    return False


if __name__ == "__main__":
    main()
