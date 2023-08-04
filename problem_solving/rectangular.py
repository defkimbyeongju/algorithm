# 실패한 내 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = {}
#     for i in range(N):
#         for j in range(N):
#             for y,x in [(0,1), (1,0)]:
#                 for k in range(1, N-i): # 세로로 먼저 탐색하고 끝에서 가로로
#                     ni, nj = i+y*k, j+x*k
#                     if arr[i][j] == arr[ni][nj]:
#                         result[str((ni+1)*(nj+1))] = result.get(str((ni+1)*(nj+1)), 0) +1
#                 for p in range(1, N-j): # 가로 탐색
#                     nj += p
#                     if arr[i][j] == arr[ni][nj]:
#                         result[str((ni+1)*(nj+1))] = result.get(str((ni+1)*(nj+1)), 0) +1
#     result = sorted(result.items())
#     print(f'#{tc} {result[0]}')


# 재도전
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0
    for i in range(N):
        for j in range(N):
            cur = arr[i][j]
            for y in range(i, N):
                for x in range(j, N):
                    if cur == arr[y][x]:
                        area = (y-i+1) * (x-j+1)
                        if max_area < area:
                            max_area = area
                            cnt = 1
                        elif max_area == area:
                            cnt += 1
    print(f'#{tc} {cnt}')



''' 강사님 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = arr[y][x] # 왼쪽 위의 좌표 값
            # 현재 위치에서 오른쪽 아래로 탐색
            for ny in range(y, N):
                for nx in range(x, N):
                    if arr[ny][nx] == cur:
                        # 면적 계산
                        area = (ny-y+1) * (nx-x+1)
                        # 최대값이라면 갱신
                        if max_area < area:
                            max_area = area
                            cnt = 1
                        elif area == max_area:
                            cnt += 1
    print(f'#{tc} {cnt}')
'''