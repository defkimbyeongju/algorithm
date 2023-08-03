'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    result = 'NO'
    for i in range(N):
        if result == "YES":
            break
        for j in range(N):
            if arr[i][j] == "o":
                # 가로로 오목 체크
                if j+4 < N:
                    if arr[i][j] == "o" and arr[i][j+1] == "o" and arr[i][j+2] == "o" and arr[i][j+3] == "o" and arr[i][j+4] == "o":
                        if j + 5 >= N:
                            result = "YES"
                            break
                        else: # 6목이 아닐 조건
                            if arr[i][j+5] != "o":
                                result = "YES"
                                break
                # 세로로 오목 체크
                if i+4 < N:
                    if arr[i][j] == "o" and arr[i+1][j] == "o" and arr[i+2][j] == "o" and arr[i+3][j] == "o" and arr[i+4][j] == "o":
                        if i+5 >= N:
                            result = "YES"
                            break
                        else: # 6목이 아닐 조건
                            if arr[j][i+5] != "o":
                                result = "YES"
                                break
                # 대각선 오목 체크
                if j+4 < N and i+4 < N:
                    if arr[i+1][j+1] == "o" and arr[i+2][j+2] == "o" and arr[i+3][j+3] == "o" and arr[i+4][j+4] == "o":
                        if i+5 >= N and j+5 >= N:
                            result = 'YES'
                            break
                        else:
                            if arr[i+5][j+5] != "o":
                                result = 'YES'
                                break
                if j-4 >= 0 and i+4 < N:
                    if arr[i + 1][j - 1] == "o" and arr[i + 2][j - 2] == "o" and arr[i + 3][j - 3] == "o" and arr[i + 4][j - 4] == "o":
                        if i+5 >= N and j-5 <= 0:
                            result = 'YES'
                            break
                        else:
                            if arr[i+5][j-5] != "o":
                                result = 'YES'
                                break
    print(result)
'''


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    result = 'NO'
    dy = [-1, 0, 1, -1]
    dx = [0, -1, 1, 1]
    while True:

