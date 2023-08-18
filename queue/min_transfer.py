def bfs(s,N,T):
    result = []
    visited = [0]*(N+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        if t == N:
            result.append(visited[t]-1)
        for w in adj_lst[t]:
            if visited[w] == 0 and w != T:
                queue.append(w)
                visited[w] = visited[t]+1
    return result

N,M = map(int, input().split())
adj_lst = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
T = int(input())

ans = bfs(1,N,T)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))