# n = int(input())
# dp = [[0]*3 for _ in range(n+1)]
# rgb = [list(map(int, input().split())) for _ in range(n)]
# for i in range(1,n+1):
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i-1][0]
#     dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i-1][1]
#     dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i-1][2]
#
# print(min(dp[n][0], dp[n][1],dp[n][2]))



# 백준 1932 정수삼각형

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N+1)]

for i in range(1,N+1): # i, i+1


# 백준 2839 설탕 배달
def sugar(n):
    dp = [0]*(n+1)
    if n == 3:
        dp[3] = 1
    elif n == 4:
        dp[4] = -1
    elif n == 5:
        dp[5] == 1
    else:
        if n%3 == 0 or n%5 == 0:
            dp[n] = min(n//3)
        else:


    return dp[n]
