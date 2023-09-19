# arr = [i for i in range(1,11)]
# path = [0]*10
# def backtracking(cnt):
#     # 재귀 종료 조건
#     if sum(path) == 10:
#         print(path)
#         return
#     # 반복문
#     for num in arr:
#         # 가지 치기
#         if num in path:
#             continue
#         # 들어가기 전 로직 - 경로 저장
#         path[cnt] = num
#         if sum(path) > 10:
#             return
#         # 다음 재귀 함수 호출
#         backtracking(cnt+1)
#         # 돌아와서 할 로직
#         path[cnt] = 0
#
# backtracking(0)




class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = left
        self.right = right

    def insert(self,childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return

        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return

        return

    # 순회
    def preorder(self):
        if self!= None
            print(self.value, end='')
            if self.right:
                self.right.preorder()
            if self.left:
                self.left.preorder()

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# 이진 트리 만들기
nodes = [TreeNode[i] for i in range(1,7)]
for i in range(0,len(arr),2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

test = 1