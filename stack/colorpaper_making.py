N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in arr:
    total += sum(i)

print(total)