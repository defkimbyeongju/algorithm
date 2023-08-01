num = 456789
c = [0] * 12 # 메모리를 2자리만큼 더 설정하여, index error를 막기 위한 if문을 사용하지 않게 됨. 이게 더 자연스러운 코드 흐름임.

for i in range(6): # 각 숫자 개수를 조사하기
    c[num % 10] += 1 # 10으로 나누면서 한 자리씩 1을 추가해서 개수 세기
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run +tri == 2:
    print("Baby Gin")
else:
    print("Lose")