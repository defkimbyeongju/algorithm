N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sum(arr, [])
print(arr.count(0))