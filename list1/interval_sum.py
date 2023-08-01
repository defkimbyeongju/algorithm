T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    new_arr = []
    for i in range(N-M+1):
        result = 0
        for j in range(i, i+M):
            result += arr[j]
        new_arr.append(result)
    max_arr = max(new_arr)
    min_arr = min(new_arr)
    print(f'#{tc} {max_arr - min_arr}')