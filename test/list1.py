# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_val = arr[0]
#     min_val = arr[0]
#     for i in range(N):
#         if arr[i] > max_val:
#             max_val = arr[i]
#         if arr[i] < min_val:
#             min_val = arr[i]
#
#     diff = max_val - min_val
#     print(f'#{tc} {diff}')
#

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_v = arr[0]
#     min_v = arr[0]
#     for i in range(N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]
#     print(f'#{tc} {max_v-min_v}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_v = 0
#     min_v = 100000
#     for i in range(0, N-M+1):
#         total = 0
#         for j in range(i, M+i):
#             total += arr[j]
#         if max_v < total:
#             max_v = total
#         if min_v > total:
#             min_v = total
#     print(f'#{tc} {max_v-min_v}')

for i in range()