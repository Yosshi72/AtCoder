def main():
    N, T, M = map(int, input().split())
    nodes = {i + 1 for i in range(N)}
    team1 = {}
    team2 = {}

    for _ in range(M):
        a, b = map(int, input().split())
        if a in team1 or b in team2:
            team1.append(a)
            team2.append(b)
        elif b in team1 or a in team2:
            team1.append(b)
            team2.append(a)
    print(team1,team2)

    return 0


if __name__ == "__main__":
    main()
