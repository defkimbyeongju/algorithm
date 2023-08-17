for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    while arr[7] != 0:
        minus = 1
        for i in range(5):
            if (arr[0]-minus) > 0:
                arr.append(arr.pop(0)-minus)
                minus += 1
            else:
                arr.pop(0)
                arr.append(0)
                break
    print(f"#{tc}",*arr)