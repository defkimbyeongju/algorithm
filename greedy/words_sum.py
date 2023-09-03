# N = int(input())
# words = [list(input()) for _ in range(N)]
# temp = 9
# result = []
# for i in range(N):
#     cnt = 0
#     for j in range(len(words[i])):
#         if not words[i][j].isdigit():
#             last = words[i][j]
#             words[i][j] = str(temp-cnt)
#             for k in range(len(words[i])):
#                 if words[i][k] == last:
#                     words[i][k] = str(temp-cnt)
#             cnt += N
#     temp -= 1
#
# for i in range(N):
#     new_value = ''
#     for j in range(len(words[i])):
#         new_value += words[i].pop(0)
#     result.append(int(new_value))
#
# print(sum(result))

N = int(input())
words = [input() for _ in range(N)]
temp = 9
result = []
change = {}
max_len = 8

for i in range(max_len):
    for j in range(N):
        try:
            if words[j][i] not in change:
                change[words[j][i]] = str(temp)
                temp -= 1
        except:
            continue
for i in range(N):
    for j in range(len(words[i])):
        if not words[i][j].isdigit():
            imsi = words[i].replace(words[i][j], change.get(words[i][j]))
            words[i] = imsi
words = [int(i) for i in words]
print(sum(words))