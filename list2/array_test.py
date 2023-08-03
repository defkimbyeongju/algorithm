# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total1 = 0
# total2 = 0
# for i in range(N):
#     total1 += arr[i][i]
#     total2 += arr[i][N-1-i]


# arr = [3,6,7,1,5,4]
# n = len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i % (1<<j):
#             print(arr[j], end=', ')
#     print()
# print()


A = [3, 9, 7, 16, 1, 20, 6, 15, 18]
N = len(A)
min_idx = 0
for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print(A)

