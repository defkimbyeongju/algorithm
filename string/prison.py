text = input()
count = 0 # 파싱을 위한 인덱스 변수 설정
new_list = [] # 새로운 리스트 생성
num = 0 # 숫자의 개수를 세는 변수
for i in range(len(text)): # 문자열 하나씩 순회하기
    if 65 <= ord(text[i]) <= 90: # 아스키코드로 접근. 대문자에 해당하면 그냥 넘기기
        continue
    elif 48 <= ord(text[i]) <= 57: # 숫자에 해당할 때
        num += 1 # num은 1씩 증가
        if i+1 < len(text): # 문자열의 마지막 문자가 아닐 때,
            if 65 <= ord(text[i+1]) <= 90: # 다음 문자가 알파벳이라면
                new_list.append(text[count:i+1].replace(text[i-num+1:i+1],'#' + str(int(text[i-num+1:i+1])+17)))  # count부터 i+1까지 new_list에 추가할 것인데, #을 붙이고, 숫자는 17을 더한 형태로 replace.
                count = i+1 # count는 다음 문자열이 시작하는 인덱스로 재설정
                num = 0 # 숫자 개수도 초기화
        elif i+1 == len(text): # 마지막 문자열일 경우
            new_list.append(text[count:i + 1].replace(text[i - num + 1:i + 1], '#' + str(int(text[i - num + 1:i + 1]) + 17)))

for j in new_list:
    print(j)

