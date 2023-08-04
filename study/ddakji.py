# 딱지문제
N = int(input())

for _ in range(N):
    arr = []
    for i in range(2):
        arr.append(list(map(int,input().split())))
        arr[i].remove(arr[i][0])
        arr[i].sort(reverse=True)
    if len(arr[0]) == len(arr[1]):
        


