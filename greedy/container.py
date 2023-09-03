T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    total = 0
    for i in range(N):
        if truck:
            if container[i] <= truck[0]:
                total += container[i]
                truck.pop(0)
        else:
            break
    print(f'#{tc} {total}')