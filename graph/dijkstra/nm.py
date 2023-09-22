import heapq

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijkstra(si, sj):
    pq = [(arr[0][0], si, sj)]
    distance[si][sj] = arr[0][0]
    while pq:
        dist, sy, sx = heapq.heappop(pq)
        if distance[sy][sx] < dist:
            continue
        for y, x in dir:
            ny, nx = sy + y, sx + x
            if 0 <= ny < N and 0 <= nx < M:
                new_cost = dist + arr[ny][nx]
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
distance = [[float('inf')] * M for _ in range(N)]
dijkstra(0, 0)
print(distance[N - 1][M - 1])