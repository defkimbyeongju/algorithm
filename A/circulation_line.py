T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    abcd = []
    for a in range(N):
        for b in range(N):
            if abs(b-a) <= 1 or abs(b-a) == N-1:
                continue
            for c in range(N):
                if abs(c-a) <= 1 or abs(c-b) <= 1 or abs(c-a) == N-1 or abs(c-b) == N-1:
                    continue
                for d in range(N):
                    if abs(d-a) <= 1 or abs(d-b) <= 1 or abs(d-c) <= 1 or abs(d-a) == N-1 or abs(d-b) == N-1 or abs(d-c) == N-1:
                        continue
                    if a > b:
                        ab = [i for i in range(b, a+1)]
                    else:
                        ab = [i for i in range(a, b+1)]
                    if c in ab and d not in ab:
                        continue
                    elif d in ab and c not in ab:
                        continue
                    abcd.append((a,b,c,d))

    max_v = 0
    for a, b, c, d in abcd:
        temp = (arr[a]+arr[b])**2 + (arr[c]+arr[d])**2
        if max_v < temp:
            max_v = temp

    print(f'#{tc} {max_v}')