N, K = map(int, input().split())
dp = [10e3]*1000001
dp[N] = 1
if N < K:
    for i in range(N+1, K+1):
        dp[i] = min(dp[i-1], dp[i+1], dp[i//2])+1
    print(dp[K]-1)
elif K < N:
    for i in range(N-1,K-1, -1):
        dp[i] = dp[i+1]+1
    print(dp[K] - 1)
else:
    print(0)