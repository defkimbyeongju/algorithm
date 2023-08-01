T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input()))
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    count_list = sorted(d.items(), key=lambda x:(x[1], x[0]), reverse=True)
    print(count_list)