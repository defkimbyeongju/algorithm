'''
def chicken_distance(used, houses): # 치킨 거리를 구하는 함수
    global min_chicken
    total = 0
    for hy, hx in houses:
        min_v = 1e9
        for i in range(len(used)):
            if used[i]:
                for cy, cx in chickens[i]:
                    temp = abs(hy-cy) + abs(hx-cx)
                    min_v = min(temp, min_v)
        total += min_v
        if total >= min_chicken: # 가지치기
            return
    min_chicken = total # 최소 치킨 거리 값 최신화

def remain_chicken(used, M, start):
    if sum(used) == M:
        chicken_distance(used, houses)
        return
    for i in range(start, len(chickens)):
        if not used[i]:
            used[i] = 1
            remain_chicken(used, M, start+1)
            used[i] = 0
'''


def combinations(arr, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result

import sys
N,M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
houses = []
chickens = []
min_chicken = 1e9
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i,j))
        elif arr[i][j] == 2:
            chickens.append((i,j))
res = combinations(chickens, M)
result = 1e9
for i in range(len(res)):
    total = 0
    for hy, hx in houses:
        temp = 1e9
        for j in range(M):
            temp = min(temp, abs(res[i][j][0] - hy) + abs(res[i][j][1] - hx))
        total += temp
    result = min(result, total)
print(result)