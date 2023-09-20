def bfs(now, total):
    if 0 < total <= K:
        result.append(now)
    elif total > K:
        return
    for i in range(M):
        if arr[i][0] == now:
            bfs(arr[i][1], total+arr[i][2])

N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
result = []
bfs(0,0)
result.sort()
print(*result)