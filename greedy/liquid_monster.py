N = int(input())
liquid = list(map(int, input().split()))
total = []
while len(liquid) > 1:
    liquid.sort()
    temp = liquid[0]+liquid[1]
    liquid.append(temp)
    total.append(temp)
    liquid.pop(0)
    liquid.pop(0)
print(sum(total))
