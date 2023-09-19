N = int(input())
path = [0]*N
chess_board = [i for i in range(1,N+1)]
result = 0
def backtracking(cnt):
    global result
    if cnt == N:
        result += 1
        return
    for i in chess_board:
        if i in path: # 캐슬이 서로 같은 라인에 있으면 안됨
            continue
        path[cnt] = i
        backtracking(cnt+1)
        path[cnt] = 0

backtracking(0)
print(result)