# 첫 번째 풀이
''' input
4
7 3
1 8 1 4 2 5 1
1 5 2 6 7 2 3
7 9 5 5 1 9 8
3 7 0 9 8 0 7
5 5 3 9 5 1 4
2 5 9 3 3 6 8
0 1 4 1 8 4 0
7 2
3 3 8 8 5 5 0
4 3 9 6 0 2 5
0 8 6 2 0 3 8
5 1 0 8 2 9 6
1 7 5 3 9 2 0
8 4 2 9 5 5 3
2 3 6 2 9 1 4
5 3
9 3 0 4 0
3 9 4 0 4
0 4 9 4 0
4 0 4 9 3
0 4 0 3 9
5 4
1 2 3 4 9
2 3 4 5 9
3 4 5 6 9
4 5 6 7 9
9 9 9 9 9

결과는
#1 75
#2 47
#3 40
#4 81
'''

# 첫 번째 풀이(5중 반복문)
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T+1):
#     N, P = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#     for i in range(N):
#         for j in range(N):
#             count = arr[i][j]
#             for k in range(4):
#                 for p in range(1, P+1):
#                     ni, nj = i+di[k]*p, j+dj[k]*p
#                     if 0<=ni<N and 0<=nj<N:
#                         count += arr[ni][nj]
#             if max_v < count:
#                 max_v = count
#     print(f'#{tc} {max_v}')


# 함수를 사용한 버전

def virus(y, x):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    total = arr[y][x]
    for i in range(4):
        for k in range(1, P+1):
            ny, nj = y+dy[i]*k, x+dx[i]*k
            if 0<=ny<N and 0<=nj<N:
                total += arr[ny][nj]
    return total

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            result.append(virus(i, j))
    print(f'#{tc} {max(result)}')










