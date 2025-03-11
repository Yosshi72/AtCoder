from collections import deque

def get_reachable_cells(grid):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
    start = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S'][0]
    reachable = {(start[0], start[1]): []}

    queue = deque([((start[0], start[1]), d) for d in directions])  # Add all possible starting moves to queue
    while queue:
        (i, j), (dx, dy) = queue.popleft()
        x, y = i + dx, j + dy
        while 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#':
            if (x, y) not in reachable or (dx, dy) not in reachable[(x, y)]:
                reachable[(x, y)] = reachable.get((x, y), []) + [(dx, dy)]
                for direction in directions:
                    queue.append(((x, y), direction))
            x, y = x + dx, y + dy

    return reachable

def main():
    N,M = map(int,input().split())
    grids = []
    for _ in range(N):
        S = list(input())
        grids.append(S)
    grids[1][1] = "S"
    reachable_cells = get_reachable_cells(grids)
    print(reachable_cells)
    print(len(reachable_cells))
    return 0

if __name__ == "__main__":
    main()
