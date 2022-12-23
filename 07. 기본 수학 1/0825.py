# 1712번 : 이익 발생 지점 찾기
A, B, C = map(int, input().split())

if B < C :
    result = A/(C-B)+1
    print(int(result))
else : 
    print('-1')


# 2292번 : 벌집의 위치
N = int(input())

room = 1 # 벌집의 개수, 1개부터 시작
cnt = 1 

while N > room :
    room = room + (6 * cnt) # 벌집이 6의 배수로 증가
    cnt += 1 # 반복 횟수
print(cnt)


# 1193번 : 분수 찾기
X = int(input()) # 분수의 자리

line = 1 # 1부터 줄 시작

# 반복문 
while X > line :
    X = X - line # 각 line에서 n이 몇번째에 위치했는지 확인
    line += 1
    
# 조건문
if line % 2 == 0 : # line이 짝수일 경우
    up = X
    down = line - X + 1
else : # line이 홀수일 경우
    up = line - X + 1
    down = X

print(up,'/',down,sep="") # sep : 구분자를 변경


