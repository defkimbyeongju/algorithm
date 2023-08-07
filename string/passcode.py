# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     sample = list(map(str, input().split()))
#     passcode = list(map(str, input().split()))
#     res = ''.join(passcode)
#     count = 0
#     text = ''
#     result = 0
#     while count != N:
#         for i in passcode:
#             for j in range(count, N):
#                 if i == sample[j]:
#                     text += sample[j]
#                     count += j
#                     continue
#                 count += 1
#     result = result if result == res else 1
#     print(f'#{tc} {result}')



# 강사님 풀이
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    sample = list(map(str, input().split()))
    passcode = list(map(str, input().split()))
    cnt = 0
    result = 0

    for i in range(N):
        if passcode[cnt] == sample[i]:
            cnt += 1
        if cnt == K:
            result = 1
            break
    print(f'#{tc} {result}')
