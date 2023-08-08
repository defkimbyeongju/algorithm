# text = input()
# count = 0
# new_list = []
# for i in range(len(text)):
#     if ord(text[i]) == 43 or ord(text[i]) == 45:
#         new_list.append(text[count:i])
#         new_list.append(text[i])
#         count = i+1
#     if i == len(text)-1:
#         new_list.append(text[count:i+1])
# result = int(new_list[0])
# for j in range(1, len(new_list)-1, 2):
#     if new_list[j] == '+':
#         result += int(new_list[j+1])
#     elif new_list[j] == '-':
#         result -= int(new_list[j+1])
#
# print(result)

# print(eval(input())) # 계산을 자동으로 해주는 eval 메서드
'''
ex = input()
if ex[0] == '-':
    ex = '0' + ex
word = ex.split('+')
ans = 0
for w in word:
    w= w.split('-')
    inner_ans = int(w[0])
    for i in range(1, len(w)):
        inner_ans -= int(w[i])
    ans += inner_ans
print(ans)
'''
