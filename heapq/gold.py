import heapq
n = int(input())
gold = list(map(int, input().split()))
heap = []
cnt = 0
for i in gold:
    heapq.heappush(heap, (i, 'G'))
while True:
    a = heapq.heappop(heap)
    if a[1] == 'S':
        break
    else:
        cnt += 1
    b = heapq.heappop(heap)
    if b[1] == 'S':
        break
    else:
        cnt += 1
        heapq.heappush(heap, (b[0]*2, 'S'))
print(cnt)