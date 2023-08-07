T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) * N for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(0, N-M+1):
            if arr[i][j] == arr[i][M-j]:
                count += 1
            else:
                break
        if count == M//2:
            result = arr[i]
            break
    print(f'#{tc} {result}')

