def main():
    N, D = map(int, input().split())
    judge = [False] * N
    judge[0] = True
    queue = [0]
    position = []
    for _ in range(N):
        x, y = map(int, input().split())
        position.append([x, y])
    while len(queue) > 0:
        i = queue.pop(0)
        for j in range(N):
            if judge[j]:
                continue
            dist = distance(position[i], position[j])
            if dist <= D**2 and judge[i]:
                judge[j] = True
                queue.append(j)

    for i in range(N):
        if judge[i]:
            print("Yes")
        else:
            print("No")


def distance(p0, p1):
    dist = (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2
    return dist


if __name__ == "__main__":
    main()
