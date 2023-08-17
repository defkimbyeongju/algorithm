# short = [int(input()) for _ in range(9)]
#
# for i in range(1<<9):
#     seven = []
#     for j in range(9):
#         if i & (1<<j):
#             seven.append(short[j])
#     if len(seven) == 7 and sum(seven) == 100:
#         break
#
# for i in sorted(seven):
#     print(i)

# n = int(input())
# cnt = 1
# if n == 1:
#     cnt = 0
# while n > 3:
#     if n % 3 == 0:
#         n /= 3
#     elif n % 2 == 0:
#         if (n-1) % 3 == 0:
#             n -= 1
#     else:
#         n -= 1
#     cnt += 1
#
# print(cnt)

# 백준 1932 정수삼각형

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N+1)]
#
# for i in range(1,N+1): # i, i+1


# 백준 2839 설탕 배달

n = int(input())
def sugar(n):
    dp = [0]*(n+1)
    dp[3] = 1
    dp[4] = -1
    dp[5] = 1
    dp[6] = 2
    dp[7] = -1
    dp[8] = 2
    if n > 9:
        for i in range(9, n+1):
            if dp[i-3] == -1 and dp[i-5] == -1:
                dp[i] = -1
            elif dp[i-3] == -1 and dp[i-5] != -1:
                dp[i] = dp[i-5]+1
            elif dp[i-3] != -1 and dp[i-5] == -1:
                dp[i] = dp[i-3]+1
            else:
                dp[i] = min(dp[i-3], dp[i-5])+1

    return dp[n]

print(sugar(n))
