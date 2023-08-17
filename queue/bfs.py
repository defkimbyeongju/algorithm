# 트리 인접행렬
'''
def bfs(arr, v):
    visited = [0] * 6
    q = []
    q.append(v)
    while q:
        t = q.pop(0)
        print(t, end=' ')
        if not visited[t]:
            visited[t] = True
            for i in range(6):
                if not visited[i] and arr[t][i] == 1:
                    q.append(i)

n = int(input())
arr = [[0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

bfs(arr, n)
'''

# 그래프 BFS
'''
arr = [[0,0,0,0,1,0],[1,0,1,0,0,1],[1,0,0,1,0,0],[1,1,0,0,0,0],[0,1,0,1,0,1],[0,0,1,1,0,0]]
def bfs(arr, v):
    visited = [0] * 6
    q = []
    q.append(v)
    while q:
        t = q.pop(0)
        print(t)
        if not visited[t]:
            visited[t] = 1
            for i in range(6):
                if arr[t][i] == 1 and not visited[i] and i not in q:
                    q.append(i)
n = int(input())
bfs(arr, n)
'''

# 미로의 거리
'''
def bfs(i,j):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    q = []
    q.append([i, j])
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    while q:
        t, v = q.pop(0)
        for k in range(4):
            ny, nx = t+dy[k], v+dx[k]
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[t][v]+1
                    q.append([ny,nx])
                elif arr[ny][nx] == 3:
                    return visited[t][v]-1
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                ans = bfs(i,j)
                break
    print(f'#{tc} {ans}')
'''

# 미로 거리 강사님 풀이

direction = [(1,0), (-1,0), (0,1), (0,-1)]

def start(): # 출발 위치 찾는 함수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return i,j

def bfs(y, x):
    queue = []
    queue.append((y,x))
    visited[y][x] = 1 # 시작 위치 방문 표시
    while queue:
        cy, cx = queue.pop(0)
        if arr[cy][cx] == '3': # 도착 위치면 거리 반환
            return visited[cy][cx] - 2 # 시작과 끝 제외
        for dy,dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0<=ny<N and 0<=nx<N: # 미로 범위 내에 있는
                if arr[ny][nx] != '1' and visited[ny][nx] == 0: # 벽이 아니고, 방문 안했을 때
                    visited[ny][nx] = visited[cy][cx]+1   # 거리 갱신
                    queue.append((ny,nx)) # 큐에 추가
    return 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    si, sj = start()
    print(f'#{tc} {bfs(si, sj)}')


