from collections import defaultdict, deque


def find_strongest_programmer(N, M, relations):
    # グラフと次数リストの初期化
    graph = defaultdict(list)
    indegree = [0] * (N + 1)

    # グラフの構築と次数リストの更新
    for A, B in relations:
        graph[A].append(B)
        indegree[B] += 1

    # 次数が0（つまり、誰よりも強い）の頂点を探す
    zero_indegree = [i for i in range(1, N + 1) if indegree[i] == 0]

    # 最強のプログラマーが一人だけ存在しない場合
    if len(zero_indegree) != 1:
        return -1

    strongest_programmer = zero_indegree[0]
    queue = deque([strongest_programmer])

    # BFSを使ってグラフを探索
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # グラフ内の全てのノードを探索したか確認
    if any(indegree[i] != 0 for i in range(1, N + 1)):
        return -1

    return strongest_programmer


def main():
    N, M = map(int, input().split())
    pros = []
    for _ in range(M):
        a, b = map(int, input().split())
        pros.append((a, b))
    print(find_strongest_programmer(N, M, pros))

    return 0


if __name__ == "__main__":
    main()
