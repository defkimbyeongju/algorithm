'''
N = int(input())
arr = list(map(int, input().split()))
clean = 21e8
for i in range(N-1):
    for j in range(i+1, N):
        temp = arr[i]+arr[j]
        if clean > abs(temp):
            clean = abs(temp)
            pair = [arr[i], arr[j]]
        if clean == abs(temp):
            if abs(pair[0]) + abs(pair[1]) > abs(arr[i]) + abs(arr[j]):
                continue
            else:
                pair = [arr[i], arr[j]]
pair.sort()
print(*pair)
'''
# 강사님 풀이

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 투 포인터 초기화
left = 0
right = n-1
# 변수 초기화
minimum = 2e9 +1
ansleft, ansright = 0, 0
while left < right:
    sum = arr[left] + arr[right] # 합 구하기
    if sum == 0:
        print(arr[left], arr[right])
        exit() # break와의 차이점: 아예 프로그램을 종료시킴
    # 절대값을 이용해서 최소 차이를 찾기
    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    # 합이 0보다 크면 right를 줄이고, 합이 0보다 작으면 left를 늘린다
    if sum > 0:
        right -= 1
    else:
        left += 1
print(arr[ansleft], arr[ansright])
