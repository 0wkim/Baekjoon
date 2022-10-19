# 10809번 : 알파벳 위치 찾기
S = input() # 알파벳 소문자로 이루어진 단어

alphabet = ['a','b','c','d','e','f','g',
            'h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet :
    print(S.find(i))


# 2675번 : 문자열 반복
T = int(input()) # 테스트 케이스 개수

for i in range(T):
    R, S = input().split() # R은 반복 횟수, S는 문자열
    text = ''
    for i in S: # 문자열의 수
        text += int(R) * i # 반복횟수와 문자열 곱하기
    print(text)


