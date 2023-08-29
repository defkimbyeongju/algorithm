n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    if i < 8:
        if i % 2 == 0:
            dp[i] = dp[i-2] + arr[i-1]
        if i % 7 == 0:
            dp[i] = dp[i-7] + arr[i-1]
    else:
        if dp[i-7] != 0:
            dp[i] = max(dp[i-2], dp[i-7])+arr[i-1]
        else:
            dp[i] = dp[i-2]+arr[i-1]
print(max(dp[n:n-7:-1]))
