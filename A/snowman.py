import heapq
horizontal_dir = [(0,1),(0,-1)] # 좌우로 이동 가능
vertical_dir = [(1,0),(-1,0)] # 상하로 이동 가능
def dijkstra(si, sj):
    distance[si][sj] = 0
    pq = [(0, si, sj)]
    while pq:
        dist, sy, sx = heapq.heappop(pq)
        if distance[sy][sx] < dist: # 현재 좌표의 거리보다 크다면 더 볼 필요가 없음
            continue
        for y,x in horizontal_dir: # 수평으로 이동할 때는 추가 거리가 들지 않아서 이전 값을 그대로 이어 받음
            ny, nx = sy+y, sx+x
            if 0<=nx<M and arr[ny][nx] != 0:
                if distance[ny][nx] > dist:
                    distance[ny][nx] = dist
                    heapq.heappush(pq, (dist,ny,nx))

        for y,x in vertical_dir: # 수직일 때는 위아래로 가장 가까운 만큼만 가면 됨
            ny, nx = sy+y, sx+x
            if 0 > ny or ny >= N: # 범위를 벗어나면 cut
                continue
            if y == 1: # 아래로 내려감
                cnt = 1
                while True:
                    if arr[ny][nx] != 0: # 한 칸 위아래에 위치하면 바로 heappush하면 됨
                        if distance[ny][nx] > dist:
                            next_cost = max(dist, cnt)
                            distance[ny][nx] = next_cost
                            heapq.heappush(pq, (next_cost,ny,nx))
                        break
                    ny += 1
                    if ny >= N:
                        break
                    cnt += 1
            elif y == -1: # 위로 올라감
                cnt = 1
                while True:
                    if arr[ny][nx] != 0:  # 한 칸 위아래에 위치하면 바로 heappush하면 됨
                        if distance[ny][nx] > dist:
                            next_cost = max(dist, cnt)
                            distance[ny][nx] = next_cost
                            heapq.heappush(pq, (next_cost,ny,nx))
                        break
                    ny -= 1
                    if 0 > ny:
                        break
                    cnt += 1



N,M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
start_y, start_x, target_y, target_x = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start_y = i
            start_x = j
        elif arr[i][j] == 3:
            target_y = i
            target_x = j
distance = [[float('inf')]*M for _ in range(N)]
dijkstra(start_y, start_x)
print(distance[target_y][target_x])