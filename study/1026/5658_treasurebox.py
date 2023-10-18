T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    q = list(input())
    num_list = []
    div = N // 4
    for _ in range(4):
        a = q.pop(0)
        q.append(a)
        for i in range(4):
            temp = q[div*i:div*(i+1)]
            temp = ''.join(temp)
            num_list.append(int(temp,16))

    num_list = list(set(num_list))
    num_list.sort(reverse=True)

    print(f'#{tc} {num_list[K]}')