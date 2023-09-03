import itertools
def find_max(arr):
    idx_list = list(itertools.permutations(range(N), N))
    idx_list = [list(i) for i in idx_list]
    max_v = 0
    for i in idx_list:
        numbers = arr.copy()
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


# 순열 생성 코드
# def perm(i, n):
#     if i==n: # 순열 완성
#         print(p)
#         return
#     else: #p[i]에 들어갈 숫자를 결정
#         for j in range(n):
#             if used[j] == 0: # 아직 사용되기 전이면
#                 p[i] = card[j]
#                 used[j] = 1
#                 perm(i+1, n)
#                 used[j] = 0
#
#
# card = list(map(int, input()))
# used = [0]*6
# p = [0]*6
# perm(0,6)