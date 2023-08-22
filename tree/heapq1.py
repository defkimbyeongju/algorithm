# def ugly_number(n):
#     if n == 1:
#         return 1
#     temp = 2
#     cnt = 2
#     while tree[n] == 0:
#         if temp % 2 == 0 or temp % 3 == 0 or temp % 5 == 0:
#             tree[cnt] = temp
#             cnt += 1
#         temp += 1
#     return tree[n]
#
# Q = int(input())
# num_lst = list(map(int, input().split()))
# ans = []
# for i in num_lst:
#     tree = [0 for _ in range(i+1)]
#     ans.append(ugly_number(i))
#
# print(*ans)


import heapq
N = int(input())
K = list(map(int, input().split()))
ugly =[]
heap = [1] # 최초 힙에 1 넣기
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

while len(ugly) < max(K):
    n = heapq.heappop(heap) # 최소값 가져오기
    if n not in ugly: #중복 피하기
        ugly.append(n)
        heapq.heappush(heap, n*2)
        heapq.heappush(heap, n*3)
        heapq.heappush(heap, n*5)
for i in K:
    print(ugly[i-1], end= ' ')


