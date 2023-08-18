def bfs(s,g):
    visited = [0]*(N+1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        if t == g:
            return 'YES'
        for w in adj_lst[t]:
            if visited[w]==0:
                queue.append(w)
                visited[w] = 1
    return "NO"

N = int(input())
T = int(input())
adj_lst = [[]*(N+1) for _ in range(N+1)]
for i in range(T):
    n1, n2 = map(int, input().split())
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)
a = int(input())
b = int(input())
print(bfs(a,b))