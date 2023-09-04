N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# temp = B.copy()
# idx_list = []
# for _ in range(N):
#     idx_b = temp.index(max(temp))
#     idx_list.append(idx_b)
#     temp[idx_b] = 0
# new_a = [0]*N
# for i in idx_list:
#     new_a[i] = min(A)
#     A[A.index(min(A))] = 1000
# total = 0
# for i in range(N):
#     total += new_a[i] * B[i]
# print(total)
A.sort()
B.sort(reverse=True)
total = 0
for i in range(N):
    total += A[i] * B[i]
print(total)