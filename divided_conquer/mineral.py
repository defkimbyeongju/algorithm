def binary_start(target):
    start, end = 0, N-1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] >= target:
            end = middle - 1
        else:
            start = middle + 1
    return start

def binary_end(target):
    start, end = 0, N-1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return end+1


N,Q = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(Q):
    si, ei = map(int, input().split())
    print(binary_end(ei) - binary_start(si))