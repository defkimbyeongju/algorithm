# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     cnt = [0] * 201
#     for a,b in arr:
#         a = (a+a%2)//2
#         b = (b+b%2)//2
#         for i in range(min(a,b), max(a,b)+1):
#             cnt[i] += 1
#
#     print(f'#{tc} {max(cnt)}')





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    pre = []
    cnt = 1
    for _ in range(N):
        a, b = map(int,input().split())
        temp = [i for i in range(min(a,b), max(a,b)+1)]
        for i in temp:
            if i in pre:
                cnt += 1
                break
        pre = temp

    print(f'#{tc} {cnt}')