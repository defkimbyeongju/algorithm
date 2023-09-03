def isrun(arr):
    if len(arr) < 3:
        return 0
    for i in range(len(arr)-2):
        if arr[i]+1 in arr and arr[i]+2 in arr:
            return 1
    return 0

def triplet(arr):
    if len(arr) < 3:
        return 0
    for i in range(len(arr)-2):
        if arr.count(arr[i]) == 3:
            return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    a = [] # 첫번째 플레이어
    b = [] # 두번째 플레이어
    card = list(map(int, input().split()))
    result = 0
    while card:
        a.append(card.pop(0))
        a.sort()
        if isrun(a) or triplet(a):
            result = 1
            break
        b.append(card.pop(0))
        b.sort()
        if isrun(b) or triplet(b):
            result = 2
            break
    print(f'#{tc} {result}')