'''
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
'''

# 순열 생성 코드
# def perm(i, n, total):
#     global max_v
#     if i==n: # 순열 완성
#         baloons = arr[:]
#         temp = 0
#         for j in range(n):
#             if p[j] == 0: # 제일 처음 풍선일 경우
#                 temp += baloons[p[j]+1]
#                 baloons.pop(0)
#                 for k in range(1,n):
#                     p[k] -= 1
#             elif p[j] == len(baloons)-1:
#                 temp += baloons[p[j]-2]
#                 baloons.pop()
#             else:
#                 temp += (baloons[p[j]-1] * baloons[p[j]+1])
#                 baloons.pop(p[j])
#                 for k in range(j, n):
#                     if p[j] < p[k]:
#                         p[k] -= 1
#         max_v = max(max_v, temp)
#         return
#     else: #p[i]에 들어갈 숫자를 결정
#         for j in range(n):
#             if used[j] == 0: # 아직 사용되기 전이면
#                 used[j] = 1
#                 perm(i+1, n)
#                 used[j] = 0
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     used = [0]*N
#     max_v = 0
#     perm(0,N)
#     print(f'#{tc} {max_v}')


'''
1 2 3 4
1 0 3 4
1 0 0 4
'''

def baloon_shot(total, baloons):
    global max_v
    if sum(used) == N:
        max_v = max(total, max_v)
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            left = 1
            right = 1
            while True:
                if i - left < 0:
                    break
                if baloons[i-left] != 0:
                    break
                left += 1
            while True:
                if i + right == N:
                    break
                if baloons[i+right] != 0:
                    break
                right += 1
            if i - left < 0 and i + right == N: # 주변에 남은 풍선이 없으면 자기 자신의 점수
                temp = baloons[i]
            elif i - left < 0: # 왼쪽 끝에 있는 풍선일 경우
                temp = baloons[i+right]
            elif i + right == N:
                temp = baloons[i-left] # 오른쪽 끝에 풍선일 경우
            else:
                temp = baloons[i+right] * baloons[i-left]
            t = baloons[i]
            baloons[i] = 0
            baloon_shot(total+temp, baloons)
            used[i] = 0
            baloons[i] = t

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    used = [0] * N
    baloon_shot(0, arr)
    print(f'#{tc} {max_v}')