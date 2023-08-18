def bfs(s,g,move):
    candidate = 0
    visited = [0]*(N+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        if t == g:
            if (visited[t]-1) <= move:
                candidate = 1
                return candidate
            else:
                break
        for w in adj_lst[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
    return candidate




N, M = map(int, input().split())
adj_lst = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

G, move = map(int, input().split())
result = 0
for i in range(1,N+1):
    result += bfs(i, G, move)
print(result)