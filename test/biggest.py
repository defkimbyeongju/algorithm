T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_index = 0
    max_index = 0
    for i in range(1, N):
        if arr[i] >= arr[max_index]:
            max_index = i
        if arr[i] < arr[min_index]:
            min_index = i
    print(f'#{tc} {abs(max_index - min_index)}')
