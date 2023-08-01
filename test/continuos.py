T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = 0
    last_cnt = 0

    for i in arr:
        if i == 1:
            cnt += 1
            if cnt > last_cnt:
                last_cnt = cnt
        elif i == 0:
            if cnt > last_cnt:
                last_cnt = cnt
            cnt = 0
    print(f'#{tc} {last_cnt}')
