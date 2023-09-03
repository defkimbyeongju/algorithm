coins = [500, 100, 50, 10]
N = int(input())
cnt = 0
for i in coins:
    if N >= i:
        while N >= i:
            N -= i
            cnt += 1
print(cnt)