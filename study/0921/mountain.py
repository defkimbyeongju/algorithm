'''
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(i, j, fuel):
    global min_v
    if i == j == N-1:
        min_v = min(min_v, fuel) # 기존 최솟값이랑 비교해서 더 작은 값으로 최소값 갱신
        return
    if fuel > min_v: # 현재 연료가 이미 최소값을 넘어서면 더 탐색할 필요 없음
        return
    for l in range(M):
        if i == tunnel_start[l][0] and j == tunnel_start[l][1] and visited[tunnel_finish[l][0]][tunnel_finish[l][1]] == 0:
            visited[tunnel_finish[l][0]][tunnel_finish[l][1]] = 1
            dfs(tunnel_finish[l][0],tunnel_finish[l][1], fuel+fuels[l])
            visited[tunnel_finish[l][0]][tunnel_finish[l][1]] = 0
    for y, x in dir:
        ny, nx = i + y, j + x
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            if arr[i][j] > arr[ny][nx]:
                dfs(ny, nx, fuel)
                visited[ny][nx] = 0
            elif arr[i][j] == arr[ny][nx]:
                dfs(ny, nx, fuel+1)
                visited[ny][nx] = 0
            else:
                dfs(ny, nx, fuel + (arr[ny][nx] - arr[i][j])*2)
                visited[ny][nx] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel_start = []
    tunnel_finish = []
    fuels = []
    for _ in range(M):
        x1, y1, x2, y2, power = map(int,input().split())
        tunnel_start.append([x1-1, y1-1])
        tunnel_finish.append([x2-1, y2-1])
        fuels.append(power)
    min_v = float('inf')
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    dfs(0, 0, 0)
    print(f'#{tc} {min_v}')
'''

import heapq
dir = [(0,1),(1,0),(0,-1),(-1,0)]
def dijkstra(si,sj):
    distance[si][sj] = 0
    pq = [(0,si,sj)]
    while pq:
        dist, sy, sx = heapq.heappop(pq)
        if distance[sy][sx] < dist:
            continue
        # sy,sx가 터널 시작점인지 체크
        if_tunnel = tunnel_check(sy,sx)
        if if_tunnel:
            ny, nx, fuel = if_tunnel[0], if_tunnel[1], if_tunnel[2]
            new_cost = dist + fuel
            if distance[ny][nx] > new_cost:
                distance[ny][nx] = new_cost
                heapq.heappush(pq, (new_cost,ny,nx))
        else:
            for y,x in dir:
                ny, nx = sy+y, sx+x
                if 0<=ny<N and 0<=nx<N and (ny,nx) not in in_tunnel:
                    # 다음 칸의 높이(더 큼, 같음, 더 작음)에 따라 distance가 달라짐
                    if arr[ny][nx] > arr[sy][sx]:
                        new_cost = dist + (arr[ny][nx]-arr[sy][sx])*2
                    elif arr[ny][nx] == arr[sy][sx]:
                        new_cost = dist + 1
                    else:
                        new_cost = dist
                    if distance[ny][nx] > new_cost:
                        distance[ny][nx] = new_cost
                        heapq.heappush(pq,(new_cost,ny,nx))
    return distance[N-1][N-1]

def tunnel_check(i,j):
    for idx in range(M):
        if i+1 == tunnel[idx][0] and j+1 == tunnel[idx][1]:
            return [tunnel[idx][2]-1, tunnel[idx][3]-1, tunnel[idx][4]]
    return False


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]
    tunnel.sort(key=lambda x:x[4])
    in_tunnel = set()
    for i in range(M):
        if tunnel[i][0] == tunnel[i][2]:  # y좌표가 같은 수평 터널일 때
            for k in range(1, tunnel[i][3]-tunnel[i][1]):
                in_tunnel.add((tunnel[i][0]-1, tunnel[i][1]-1+k))
        elif tunnel[i][1] == tunnel[i][3]:  # x좌표가 같은 수직 터널일 때
            for k in range(1, tunnel[i][2] - tunnel[i][0]):
                in_tunnel.add((tunnel[i][0]-1+k, tunnel[i][1]-1))
        else:
            for k in range(1, tunnel[i][3] - tunnel[i][1]):
                in_tunnel.add((tunnel[i][0]-1+k, tunnel[i][1]-1+k))
    distance = [[float('inf')]*N for _ in range(N)]
    print(f'#{tc} {dijkstra(0,0)}')