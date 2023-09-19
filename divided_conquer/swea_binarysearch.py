def binary(target):
    start, end = 0, N-1
    dir = ''
    while start <= end:
        middle = (start+end)//2
        if A[middle] == target:
            return 1
        elif A[middle] > target:
            if dir == 'left':
                return 0
            else:
                dir = 'left'
                end = middle - 1
        else:
            if dir == 'right':
                return 0
            else:
                dir = 'right'
                start = middle + 1

    return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        cnt += binary(B[i])
    print(f'#{tc} {cnt}')
