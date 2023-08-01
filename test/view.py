# 10번 반복한다고 주어져 있어서 input()함수 사용 안함.
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2, N-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            total += arr[i] - max(arr[i-1],arr[i-2],arr[i+1], arr[i+2])

    print(f'#{tc} {total}')
