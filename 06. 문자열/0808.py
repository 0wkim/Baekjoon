# 11654번 : 아스키 코드
a = input()

print(ord(a))

# ord() : 문자의 아스키 코드값을 리턴
# chr() : 아스키 코드에 해당하는 문자 출력


# 11720번 : 정수를 문자열로 입력받기
N = int(input()) # 숫자의 개수
num = input() # 숫자 N개

sum = 0

for i in num : # num의 인덱스 값으로 계산
    sum = sum + int(i)
print(sum)


