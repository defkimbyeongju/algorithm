# N = int(input())
# def make1(N):
#     if N == 1:
#         return 0
#     if N == 2:
#         return 1
#     dp = [0] * (N+1)
#     dp[1] = 0
#     dp[2] = 1
#     dp[3] = 1
#     for i in range(2, N+1):
#         dp[i] = dp[i-1]+1
#         if i % 2 == 0:
#             dp[i] = min(dp[i//2]+1, dp[i])
#         if i % 3 == 0:
#             dp[i] = min(dp[i//3]+1, dp[i])
#     return dp[N]



def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))