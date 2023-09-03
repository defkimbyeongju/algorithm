A, B = map(int, input().split())
cnt = 0
while B > A:
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        if str(B)[-1] == '1':
            B = (B-1)//10
            cnt += 1
        else:
            break


if B == A:
    print(cnt)
else:
    print(-1)
