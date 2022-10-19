# 3052번 : 나머지
a = [] # 리스트 생성

for i in range(10) : 
    b = int(input())
    a.append(b % 42) # b를 42로 나눴을 때의 나머지를 a에 삽입
a = set(a) # a의 중복값 제거
print(len(a)) # a의 길이 출력


# 1546번 : 평균
num = int(input()) # 과목 개수
now = list(map(int, input().split())) # 현재 과목 점수

m = max(now) # 점수의 최댓값

sum = 0 # 수정한 값을 더할 변수

for i in range(num) : # 과목 개수 만큼 반복
    result = now[i] / m * 100 # 새로운 점수를 과목 개수만큼 반복해서 구한다.
    sum += result # 새로운 점수를 sum 변수에 계속 더해준다.
new = (sum / num) # 새로운 점수의 평균
print(round(new, 2)) # 소수점 2번째자리 까지 구한다.


