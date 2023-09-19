N,M = map(int,input().split())
dice = [i for i in range(1,7)]
path = [0] * N
stack = []

def backtracking(cnt):
    if cnt == N:
        if sorted(path) in stack:
            return
        else:
            stack.append(sorted(path))
            print(*path)
            return
    for i in dice:
        path[cnt] = i
        backtracking(cnt+1)
        path[cnt] = 0

backtracking(0)