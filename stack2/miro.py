# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     dir = [(0,1),(0,-1), (1,0), (-1,0)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 stack = []
#                 for k,p in range(4):
#                     ni, nj = i+k, j+p
#                     if 0<=ni<N and 0<=nj<N:
#                         if arr[ni][nj] == 0:
#                             stack.append((ni, nj))


# 강사님 풀이
def maze():
    while stack:
        y,x = stack.pop() # 현재 위치를 스택에서 꺼냄
        arr[y][x] = -1 # 지나간 길 표시
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny <N and 0<=nx<N:
                if arr[ny][nx] == 3:  # 도착점을 찾았을 때
                    return 1
                elif arr[ny][nx] == 0:  # 갈 수 있는 곳을 모두 stack에 추가
                    stack.append((ny,nx)) # 튜플 형태로
    return 0 # 도착점을 못 찾으면 0 반환

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 미로 정보
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2: # 시작점 찾기
                stack = [(y,x)]  # 시작점을 스택에 추가
                break

    print(f'#{tc} {maze()}')