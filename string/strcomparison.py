T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    result = str2.find(str1)
    if result < 0:
        result = 0
    else:
        result = 1
    print(f'#{tc} {result}')