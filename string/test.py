T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    count = 0
    diff = B - A
    if diff == 1 or diff == 0:     # A와 B의 차이가 1 또는 0이면 불가능
        print(f'#{tc}', -1)
    else:           # count 값이 최대가 되기 위해서는 2또는 3만 사용해야 한다.
        count = C // 2  # A와 B의 차이가 2이상이면 차를 2로 나눈 몫
        print(f'#{tc} {count}')
