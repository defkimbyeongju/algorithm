def binary_search(arr, target, start, end):
    while start < end:
        middle = start + (end - start) // 2
        if arr[middle] == target or arr[start] == target or arr[end] == target:
            return 'O'
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return 'X'

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
K = int(input())
targets = list(map(int, input().split()))
result = ''
for i in range(K):
    res = binary_search(arr, targets[i], 0, N-1)
    print(res, end='')
