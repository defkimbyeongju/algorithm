dp = [0]*1000
N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    dp[i] = rgb[i].index(min(rgb[i]))

if dp[0] != dp[1]:
    total += min(rgb[0])
else:
    if min(rgb[0]) < min(rgb[1]):
        total += min(rgb[0])
    else:
        





if rgb[0].index(min(rgb[0])) == rgb[1].index(min(rgb[1])):
    if min(rgb[0]) < min(rgb[1]):
        total += min(rgb[0])
        dp[0] = rgb[0].index(min(rgb[0]))
    for i in range(1, N-1):

else:
    total = min(rgb[0]) + min(rgb[1])
    dp[0], dp[1] = rgb[0].index(min(rgb[0])), rgb[1].index(min(rgb[1]))
    for i in range(2, N-1)

for i in range(1, N-1):
    if min(rgb[i]) < min(rgb[i+1]):
        total += min(rgb[i])
        dp[i] = rgb[i].index(min(rgb[i]))
