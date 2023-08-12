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

n = int(input())
cnt = 1
if n == 1:
    cnt = 0
while n > 3:
    if n % 3 == 0:
        n /= 3
    elif n % 2 == 0:
        if (n-1) % 3 == 0:
            n -= 1
    else:
        n -= 1
    cnt += 1

print(cnt)