T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    min_val = arr[0]
    for i in range(N):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    diff = max_val - min_val
    print(f'#{tc} {diff}')
