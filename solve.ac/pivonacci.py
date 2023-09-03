def fivo(n):
    global cnt_0
    global cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    return fivo(n-1) + fivo(n-2)


T = int(input())
for _ in range(T):
    cnt_0 = 0
    cnt_1 = 0
    target = int(input())
    fivo(target)
    print(cnt_0, cnt_1)
