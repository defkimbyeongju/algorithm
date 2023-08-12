T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        col = []
        row = []
        for j in range(9):
            row.append(arr[i][j])
            col.append(arr[j][i])
        if len(set(row)) != 9 or len(set(col)) != 9:
            result = 0
            break
    for k in range(0, 9, 3):
        cross = []
        for p in range(0, 9, 3):
            cross.extend([arr[k][p], arr[k][p+1], arr[k][p+2],
            arr[k+1][p], arr[k+1][p+1], arr[k+1][p+2],
            arr[k+2][p], arr[k+2][p+1], arr[k+2][p+2]])
            if len(set(cross)) != 9:
                result = 0
    print(f'#{tc} {result}')

# 라이브 강사 풀이
'''
def sudoku(arr):
    for i in range(9):
        cnt = [0]*10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                return 0
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    sudoku(arr)
'''