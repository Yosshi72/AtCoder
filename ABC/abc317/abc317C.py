import heapq

def max_distance(N, M, roads):
    graph = [[] for _ in range(N + 1)]

    for A, B, C in roads:
        graph[A].append((B, C))
        graph[B].append((A, C))

    def dijkstra(start):
        distances = [float('inf')] * (N + 1)
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            dist, node = heapq.heappop(queue)

            if dist > distances[node]:
                continue

            for neighbor, edge_dist in graph[node]:
                new_dist = dist + edge_dist

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))

        return distances

    max_dist = 0
    for i in range(1, N + 1):
        distances = dijkstra(i)
        max_dist = max(max_dist, max(distances))

    return max_dist

# 入力
N ,M = map(int,input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

result = max_distance(N, M, roads)
print(result)
