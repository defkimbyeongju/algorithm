def bfs(i):
    global cnt
    queue = []
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.pop(0)
        for num in adj_arr[t]:
            if not visited[num]:
                cnt += 1
                visited[num] = 1
                queue.append(num)


N = int(input())
M = int(input())
adj_arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    adj_arr[a].append(b)
    adj_arr[b].append(a)
target = int(input())
visited = [0]*(N+1)
cnt = 0
bfs(target)
print(cnt)