def bfs(s):
    q = [s]
    visited = [0] * 101
    visited[s] = 1

    while q:
        now = q.pop(0)
        # 갈 수 있는 지점 다 보라

        for to in graph[now]:
            if visited[to]:
                continue
            q.append(to)
            # 기존 방문보다 1개 더 갔다
            visited[to] = visited[now] + 1
    max_visited = max(visited)
    for i in range(100, -1, -1):
        if visited[i] == max_visited:
            return i


for tc in range(1,11):
    N, start = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0,N,2):
        f = numbers[i]
        t = numbers[i+1]
        graph[f].append(t)
    print(f'#{tc} {bfs(start)}')