def find_loop(graph):
    def dfs(node, visited, path):
        if node in path:
            # ループが見つかった場合、そのループを返す
            return path[path.index(node):]
        
        if node not in visited:
            visited.add(node)
            path.append(node)
            
            for neighbor in graph.get(node, []):
                loop = dfs(neighbor, visited, path)
                if loop:
                    return loop
            
            path.pop()

        return None

    for node in graph:
        visited = set()
        path = []
        loop = dfs(node, visited, path)
        if loop:
            return loop

    return None
def main():
    N = int(input())
    A = list(map(int,input().split()))
    graphs = {}
    for i in range(N):
        graphs[str(i+1)] = [str(A[i])]
    loops = find_loop(graphs)
    print(len(loops))
    print(*loops)
    return 0

if __name__ == "__main__":
    main()
