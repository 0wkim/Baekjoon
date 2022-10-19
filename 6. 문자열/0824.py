# 5622번 : 문자에 대응하는 수 출력
alphabet = input().lower() # 소문자로 입력받기

DialNumber = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv','wxyz']

time = 0 # 다이얼을 걸기 위해 필요한 시간을 알기 위해 time변수 초기화

for i in range(len(alphabet)) : # 입력한 단어의 길이만큼 반복
    for j in DialNumber : # 다이얼 넘버 하나하나를 반복
        if alphabet[i] in j : # 만약 입력받은 단어가 j의 문자열에 해당된다면
            # 0부터 시작하기 때문에 3초를 더함
            time = time + (DialNumber.index(j) + 3) 
print(time)


# 2941번 : 크로아티아 알파벳 개수 세기
word = input()

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳

for i in alphabet :
    word = word.replace(i, '*') # word가 alphabet에 있는 알파벳을 찾아 *로 변환
print(len(word))


# 1316 : 조건에 맞는 문자열 찾기
cnt = int(input())
result = cnt

for i in range(cnt) :
    word = input()

    for j in range(len(word) - 1) : 
        if word[j] == word[j + 1] : # 현재 알파벳과 다음 알파벳이 동일할 경우
            pass # 계속 진행
        elif word[j] in word[j+1:] : # 현재 알파벳과 다음 알파벳이 다를 경우
            result -= 1 # result 값 감소 
            break

print(result)