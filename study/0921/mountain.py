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

from collections import deque

def bfs(r,c):
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    visited[r][c] = 0 # 시작지점 연료소비량 0 초기화
    queue = deque()
    queue.append((r,c))
    while queue: # 큐에 노드가 있으면 계속 탐색
        r, c = queue.popleft()
        if (r,c) in tunnel_start:
            idx = tunnel_start.index((r,c))
            nr, nc = tunnel[idx][2], tunnel[idx][3]
            val = 0
            if arr[r][c] < arr[nr][nc]:
                val = arr[nr][nc] - arr[r][c]
            # 2. 이동하려는 위치의 연료 소비량 갱신
            if visited[r][c] + 1 + val < visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1 + val
                queue.append((nr-1, nc-1))
        else:
            for dr, dc in dir:
                nr, nc = r+dr, c+dc
                # 이동 가능한 범위 내에 있을 때
                if 0<=nr<N and 0<=nc<N:
                    val = 0
                    # 1. 현재 지점보다 높은 지역으로 이동할 때 높이 차이
                    if arr[r][c] < arr[nr][nc]:
                        val = arr[nr][nc] - arr[r][c]
                    # 2. 이동하려는 위치의 연료 소비량 갱신
                    if visited[r][c] + 1 + val < visited[nr][nc]:
                        visited[nr][nc] = visited[r][c] + 1+ val
                        queue.append((nr-1,nc-1))
    return visited[N-1][N-1]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]
    tunnel.sort(key=lambda x:x[4])
    tunnel_start = [(i,j) for i,j,a,b,c in tunnel]
    visited = [[float('inf')]*N for _ in range(N)]
    result = bfs(0,0)
    print(f'#{tc} {result}')
