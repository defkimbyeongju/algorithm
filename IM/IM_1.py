# 단어 어디에 들어갈까

# def word_count_1(i,j): # 가로 판별
#     global result
#     power = 1
#     while True:
#         ny, nx = i, j+(1 * power)
#         if 0<=nx<N and arr[ny][nx] == 1:
#             power += 1
#         else:
#             break
#     if power == K:
#         result += 1
#     return
#
# def word_count_2(i,j): # 세로 판별
#     global result
#     power = 1
#     while True:
#         ny, nx = i+(1 * power), j
#         if 0<=ny<N and arr[ny][nx] == 1:
#             power += 1
#         else:
#             break
#     if power == K:
#         result += 1
#     return
#
#
# T = int(input())
# for tc in range(1,T+1):
#     result = 0
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 if i == 0 or arr[i-1][j] == 0:
#                     word_count_2(i,j)
#                 if j == 0 or arr[i][j-1] == 0:
#                     word_count_1(i,j)
#     print(f'#{tc} {result}')

# 원재의 메모리

# T = int(input())
# for tc in range(1,T+1):
#     bit = list(input())
#     length = len(bit)
#     temp = ['0']*length
#     cnt = 0
#     for i in range(length):
#         if bit[i] == '1' and temp[i] == '0':
#             for j in range(i, length):
#                 temp[j] = '1'
#             cnt += 1
#             if bit == temp:
#                 break
#         elif bit[i] == '0' and temp[i] == '1':
#             for k in range(i, length):
#                 temp[k] = '0'
#             cnt += 1
#             if bit == temp:
#                 break
#     print(f'#{tc} {cnt}')


# 삼성시의 버스노선

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     bus = [0]*5001
#     for _ in range(N):
#         a, b = map(int, input().split())
#         for i in range(a, b+1):
#             bus[i] += 1
#     P = int(input())
#     result = []
#     for _ in range(P):
#         c = int(input())
#         result.append(bus[c])
#
#     print(f'#{tc}', *result)


# 오목판정

def omok(arr):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1,1), (1,-1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for y, x in dir:
                    cnt = 1
                    for power in range(1,5):
                        ny, nx = i + (y*power), j + (x*power)
                        if 0<=ny<N and 0<=nx<N:
                            if arr[ny][nx] == 'o':
                                cnt += 1
                            else:
                                break
                        if cnt == 5:
                            return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {omok(arr)}')


