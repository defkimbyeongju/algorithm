T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    print(arr)