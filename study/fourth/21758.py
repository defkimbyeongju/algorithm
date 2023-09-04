N = int(input())
honey = list(map(int, input().split()))
idx = [i for i in range(N)]
idx_lst =
start_1 =
start_2 =
goal =

if start_1 > goal:
    for i in range(start_1-1, goal-1, -1):
        if i == start_2:
            continue
        total += honey[i]
else:
    for i in range(start_1+1, goal+1):
        if i == start_2:
            continue
        total += honey[i]

if start_2 > goal:
    for i in range(start_2-1, goal-1, -1):
        if i == start_1:
            continue
        total += honey[i]
else:
    for i in range(start_2+1, goal+1):
        if i == start_1:
            continue
        total += honey[i]
