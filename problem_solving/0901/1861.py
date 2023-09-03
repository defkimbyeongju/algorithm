def combinations(arr, k, start=0, current=[]):
    if len(current) == k:
        print(current)
        return

    for i in range(start, len(arr)):
        current.append(arr[i])
        combinations(arr, k, i + 1, current)
        current.pop()

# 이중 리스트
double_list = [[1, 2], [3, 4], [5, 6]]

# 2개씩의 조합을 구한다고 가정
k = 2
combinations(double_list, k)