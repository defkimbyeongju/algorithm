for _ in range(10):
    tc = int(input())
    check = input()
    origin = input()
    result = 0
    for i in range(len(origin)-len(check)+1):
        j = 0
        while j < len(check):
            if origin[i] != check[j]:
                break
            j += 1
            i += 1
        else:
            result += 1
    print(f'#{tc} {result}')
