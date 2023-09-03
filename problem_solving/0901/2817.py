# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     cnt = 0 # 합이 K가 되는 경우의 수
#
#     for i in range(1<<N):
#         s = 0
#         for j in range(N):
#             if i&(1<<j):
#                 s += arr[j]
#         if s==K:
#             cnt += 1
#     print(f'#{tc} {cnt}')


def f(i, N, s, K, rs):
    global cnt
    if i==N:
        if s==K:
            cnt += 1
    elif s>K:
        return
    elif s+rs<K:
        return
    else:
        f(i+1, N, s+arr[i], K, rs-arr[i])
        f(i+1, N, s, K, rs-arr[i])

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    s = 0
    f(0,N,s,K, sum(arr))
    print(f'#{tc} {cnt}')