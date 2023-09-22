# 처음 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0
    while N % 2 == 0:
        N = N / 2
        count_2 += 1
    while N % 3 == 0:
        N = N / 3
        count_3 += 1
    while N % 5 == 0:
        N = N / 5
        count_5 += 1
    while N % 7 == 0:
        N = N / 7
        count_7 += 1
    while N % 11 == 0:
        N = N / 11
        count_11 += 1
    print(f'#{tc} {count_2} {count_3} {count_5} {count_7} {count_11}')

# 좀 더 효율적으로 코드를 짠다면?
