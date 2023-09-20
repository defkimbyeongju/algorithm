# dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#
# def backtracking(i, j, fuel):
#     global min_v
#     if i == j == N - 1:
#         min_v = min(fuel, min_v)
#         return
#     if fuel > min_v:
#         return
#     temp = tunnel_check(i, j)
#     if temp:
#         for idx in range(len(temp)):
#             if visited[temp[idx][0]-1][temp[idx][1]-1] == 0:
#                 visited[temp[idx][0]-1][temp[idx][1]-1] = 1
#                 backtracking(temp[idx][0]-1, temp[idx][1]-1, fuel + temp[idx][4])
#                 visited[temp[0] - 1][temp[1] - 1] = 0
#     for y, x in dir:
#         ny, nx = i + y, j + x
#         if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
#             visited[ny][nx] = 1
#             if arr[i][j] > arr[ny][nx]:
#                 backtracking(ny, nx, fuel)
#                 visited[ny][nx] = 0
#             elif arr[i][j] == arr[ny][nx]:
#                 backtracking(ny, nx, fuel + 1)
#                 visited[ny][nx] = 0
#             else:
#                 backtracking(ny, nx, fuel + (arr[ny][nx] - arr[i][j]) * 2)
#                 visited[ny][nx] = 0
#
#
# def tunnel_check(i, j):
#     result = []
#     for k in range(M):
#         if (i == tunnel[k][0] - 1 and j == tunnel[k][1] - 1):
#             result.append(tunnel[k])
#     if result:
#         return result
#     else:
#         return False
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     tunnel = [list(map(int, input().split())) for _ in range(M)]
#     min_v = float('inf')
#     visited = [[0] * N for _ in range(N)]
#     visited[0][0] = 1
#     backtracking(0, 0, 0)
#     print(f'#{tc} {min_v}')

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