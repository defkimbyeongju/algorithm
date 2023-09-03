# def bfs(i,j):
#     queue = deque()
#     queue.append((i,j))
#     visited = [[0]*M for _ in range(N)]
#     visited[i][j] = 1
#     dir =  [(0,1),(1,0),(0,-1),(-1,0)]
#     while queue:
#         di, dj = queue.popleft()
#         for y,x in dir:
#             min_v = 10e10
#             ny, nx = di+y, dj+x
#             if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
#                 if arr[ny][nx] == 'W':
#                     visited_1[i][j] = visited[di][dj]
#                     return visited[di][dj]
#                 else:
#                     queue.append((ny, nx))
#                     visited[ny][nx] = visited[di][dj] + 1
#
#
#

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     total = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'L':
#                 visited_1 = [[0]*M for _ in range(N)]
#                 total += bfs(i,j)
#     print(f'#{tc} {total}')
from collections import deque
T = int(input())
dir =  [(0,1),(1,0),(0,-1),(-1,0)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [[-1]*M for _ in range(N)]
    queue = deque()

    for i in range(N):
        t = input()
        for j in range(M):
            if t[j] == 'W':
                queue.append((i,j))
                visited[i][j] = 0
    result = 0
    while queue:
        di, dj = queue.popleft()
        for y, x in dir:
            ny, nx = di+y, dj+x
            if -1 < ny < N and -1 < nx < M and visited[ny][nx] == -1:
                queue.append((ny,nx))
                visited[ny][nx] = visited[di][dj]+1
    result = sum(sum(visited,[]))
    print(f'#{tc} {result}')