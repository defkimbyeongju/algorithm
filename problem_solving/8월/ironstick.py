T = int(input())
for tc in range(1,T+1):
    arr = input()
    cnt = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        elif arr[i] == ')':
            if arr[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')