# n = 5
# r = 3
# a = [1,2,3,4,5]
# tr = [0]*r
# def comb(n,r):
#     if r == 0:
#         print(tr)
#     elif n < r: # 남은 원소보다 많은 원소를 선택해야 하는 경우
#         return # 불가
#     else:
#         tr[r-1] = a[n-1] # a[n-1] 조합에 포함시키는 경우
#         comb(n-1, r-1)
#         comb(n-1, r)  # a[n-1]을 포함시키지 않는 경우
#
# comb(n,r)

# A = [1,2,3,4,5]
# N = len(A)
# R = 3
# comb = [0]*R
#
#
# def ncr(n,r,s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             ncr(n, r-1, i+1)
#
# ncr(N, R, 0)

# numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(numbers)
# target = 0
# cnt = 0
# for i in range(1<<N):
#     temp = 0
#     for j in range(N):
#         if i & (1<<j):
#             temp += numbers[j]
#     if temp == target:
#         cnt += 1
# print(cnt)

N = 6
seed = [[0]*N for _ in range(N)]
print(seed)