# def dfs(i, j):
#     global cnt
#     cnt += 1
#     dir = [(0,1), (1,0), (-1,0), (0,-1)]
#     for y,x in dir:
#         ny, nx = i+y, j+x
#         if -1<ny<N and -1<nx<N and arr[ny][nx] - arr[i][j] == 1:
#             dfs(ny, nx)
#     return
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#     ans = 10e9
#     for i in range(N):
#         for j in range(N):
#             cnt = 0
#             dfs(i, j)
#             if max_v < cnt:
#                 max_v = cnt
#                 ans = arr[i][j]
#             elif max_v == cnt:
#                 if ans > arr[i][j]:
#                     ans = arr[i][j]
#     print(f'#{tc} {ans} {max_v}')

# 강사님 풀이

dir = [(0,1), (1,0), (-1,0), (0,-1)]
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N*N+1)
    for i in range(N):
        for j in range(N):
            for r, c in dir:
                # 격자 내에 있어야 함
                if 0 <= i+r < N and 0<=j+c<N and arr[i][j] + 1 == arr[i+r][j+c]:
                    v[arr[i][j]] = 1 # 연속된 숫자임을 표시
    start, cnt, temp = 0,1,1
    for i in range(len(v)-1, -1, -1):
        if v[i] == 1: # 연속된 숫자인 경우
            temp += 1 # 연속된 카운트 증가
        else:
            if cnt <= temp: # 최대값 갱신
                cnt = temp
                start = i+1 # 시작점 갱신
            temp = 1 # 연속 카운트 초기화
    print(f'#{tc} {start} {cnt}')