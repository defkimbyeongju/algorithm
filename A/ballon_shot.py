import itertools
import copy
def find_max(arr):
    idx = [i for i in range(N)]
    idx_list = list(itertools.permutations(idx, N))
    idx_list = [list(i) for i in idx_list]
    max_v = 0
    for i in idx_list:
        numbers = copy.deepcopy(arr)
        total = 0
        for j in range(N):
            if len(numbers) >= 3 and 1<=i[j]<len(numbers)-1:
                total += numbers[i[j]-1] * numbers[i[j]+1]
            elif len(numbers) >= 2 and i[j] == 0:
                total += numbers[i[j]+1]
            elif len(numbers) >= 2 and i[j] == len(numbers)-1:
                total += numbers[i[j]-1]
            else:
                total += numbers[i[j]]
            for k in range(N):
                if i[k] > i[j]:
                    i[k] -= 1
            numbers.pop(i[j])
        if max_v < total:
            max_v = total

    return max_v


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = find_max(arr)
    print(f'#{tc} {result}')