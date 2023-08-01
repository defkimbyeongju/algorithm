T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i
    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')