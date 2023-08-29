T, n = map(int, input().split())
value = list(map(int, input().split()))
dp = [0] * (T+1)


for i in range(T+1):
    if i in value:
        dp[i] = 1
    else:
        temp = []
        for j in range(n):
            if i-value[j] > 0 and dp[i-value[j]] != 0:
                temp.append(dp[value[j]]+dp[i-value[j]])
        if temp:
            dp[i] = min(temp)

if dp[T] == 0:
    print('impossible')
else:
    print(dp[T])