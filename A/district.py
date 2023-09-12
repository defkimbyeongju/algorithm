def combinations(arr, n):
    def backtrack(start, current_combination):
        if len(current_combination) == n:
            result.append(current_combination[:])
            return
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result

def check_adj(): # 각 마을끼리 인접해 있는지 확인하는 함수 

# 예제
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    adj_arr = [list(map(int, input().split())) for _ in range(N)]
    idx_list = [i for i in range(N)]
    ans_list = []
    for i in range(1, N//2+1):
        result = combinations(idx_list, i)
        ans_list.append(result)
    print(ans_list)
