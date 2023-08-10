num_list = [3,5,1,9,7]
for _ in range(4):
    dir = input()
    if dir == 'R':
        a = num_list.pop(4)
        num_list.insert(0, a) # insert 메서드는 list의 원하는 위치에 값을 추가할 수 있다. list.insert(원하는 위치 인덱스, 추가할 값)
    elif dir == 'L':
        a = num_list.pop(0)
        num_list.append(a)

print(*num_list)
