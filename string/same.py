T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) * N for _ in range(N)]
    result = ''
    count = 0
    for i in range(N):
        for j in range(N-M+1):
            text_row = arr[i][j:j+M]
            if text_row == text_row[::-1]:
                result = ''.join(text_row)
                break
    for i in range(N-M+1):
        for j in range(N):
            text_col = [arr[k][j] for k in range(i, i+M)]
            if text_col == text_col[::-1]:
                result = ''.join(text_col)

    print(f'#{tc} {result}')