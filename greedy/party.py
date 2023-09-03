N, M = map(int, input().split())
min_x = 10e10
min_y = 10e10
for _ in range(M):
    a, b = map(int, input().split())
    if min_y > a:
        min_y = a
    if min_x > b:
        min_x = b

if min_y < min_x*6:
    if min_y < min_x*(N%6):
        result = min_y*(N//6)+min_y
    else:
        result = min_y*(N//6)+min_x*(N%6)
else:
    result = N*min_x

print(result)

