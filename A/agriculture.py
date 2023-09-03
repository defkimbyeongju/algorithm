# def dfs(i,j):
#     global harvest
#
#     if days >= M:
#         return
#     dir = [(0,1),(1,0),(0,-1),(-1,0)]
#     for y,x in dir:
#         ny, nx = i+y, j+x
#         if -1<ny<N and -1<nx<N and arr[ny][nx]==0: # 범위 내에 있고 씨앗이 심어져 있지 않으며, 농지일 경우
#             if not visited[ny][nx]:
#                 visited[ny][nx] = 1
#                 days += 1
#                 dfs(ny, nx)
#             elif visited[ny][nx] == 4:
#                 harvest += 1
#                 visited[ny][nx] = 0
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 visited = [0*N for _ in range(N)]
#                 harvest = 0
#                 dfs(i, j)


# 정답 코드
import copy

# ** ydir, xdir, face는 직접 그려보면서 왜 이런 값이 나오는지를 확인해보길 바람.
# 지금 보는 방향에서 오앞왼뒤 이동했을때의 y offset
ydir = [
    # 오앞왼뒤
    (1, 0, -1, 0),  # 오
    (0, -1, 0, 1),  # 앞
    (-1, 0, 1, 0),  # 왼
    (0, 1, 0, -1)  # 뒤
]
# 지금 보는 방향에서 오앞왼뒤 이동했을때의 x offset
xdir = [
    # 오앞왼뒤
    (0, 1, 0, -1),  # 오
    (1, 0, -1, 0),  # 앞
    (0, -1, 0, 1),  # 왼
    (-1, 0, 1, 0)  # 뒤
]
# 지금 보는 방향에서 오앞왼뒤 이동하고 나서 보는 방향
face = [
    # 오앞왼뒤
    (3, 0, 1, 2),  # 오
    (0, 1, 2, 3),  # 앞
    (1, 2, 3, 0),  # 왼
    (2, 3, 0, 1)  # 뒤
]


def sim(y, x, dir):
    days = M # 일수는 M으로 입력 받음
    cnt = 0
    seedcnt = [[0 for _ in range(N)] for _ in range(N)]  # seedcnt : 각 (y,x) 좌표에 몇번째 (K) 씨앗이 심어졌는지 기록. 이중리스트로 구현
    seeds = []  # 씨앗들. (y좌표, x좌표, 날짜)로 담기게 된다

    # M일동안 simulation
    while days > 0:
        harvested = False
        days -= 1  # 하루가 지났다
        size = len(seeds)
        # 모든 씨앗들 업데이트
        for _ in range(size):
            now = seeds.pop(0)  # 맨 앞에거 빼고
            now[2] += 1  # 날짜 하루 추가
            # K + 3일이 지났다면
            if now[2] == (3 + seedcnt[now[0]][now[1]]):
                mapcopy[now[0]][now[1]] = 3  # 수확 가능하도록 설정
            else:
                seeds.append(now)  # 아니면 다시 queue(list)에 삽입
        # 지금 위치가 수확이 가능하다면
        if mapcopy[y][x] == 3:
            cnt += 1  # 수확 + 1
            mapcopy[y][x] = 0  # 빈 땅으로 변경
            harvested = True  # 이번 턴에 수확했다! 기록
        # 다음 위치 / 방향 확인
        nextdir = -1
        for i in range(4):
            ny = y + ydir[dir][i]
            nx = x + xdir[dir][i]
            # 산이거나, 싹이 튼곳이면 못간다. (테두리는 모두 1이니 범위 검사는 필요 없음)
            if mapcopy[ny][nx] == 1 or mapcopy[ny][nx] == 2:
                continue
            # 오앞왼뒤 우선순위로 갈수 있는곳 찾았으면 break
            nextdir = i
            break
        # 현재 이동이 가능하지 않다면 -> 다음날로
        if nextdir == -1:
            continue
            # 이동이 가능하고, 현재 위치가 빈 땅이면서, 여기서 오늘 수확한곳이 아니라면
        if mapcopy[y][x] == 0 and harvested == False:
            mapcopy[y][x] = 2  # 씨앗을 뿌리고
            seedcnt[y][x] += 1  # 여기에 씨앗을 뿌린 횟수 늘려주고 (K)
            seeds.append([y, x, -1])  # 씨앗 추가 (y좌표, x좌표, 날짜)
        y = y + ydir[dir][nextdir]  # 다음 Y
        x = x + xdir[dir][nextdir]  # 다음 X
        dir = face[dir][nextdir]  # 다음 방향
    return cnt


T = int(input())
for tc in range(1, T + 1):
    # input
    N, M = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # solve - 모든 위치에서 모든 방향으로 두기
    for i in range(N):
        for j in range(N):
            # 산이라면 pass
            if MAP[i][j] == 1:
                continue
            for d in range(4):
                # 돌릴때마다 원본 맵으로 복구 -> mapcopy를 simulation용 맵으로 사용
                mapcopy = copy.deepcopy(MAP)
                temp = sim(i, j, d)
                ans = max(temp, ans)
    # output
    print(f"#{tc} {ans}")