# 2231번 : N의 생성자 구하기
n = int(input())
result = 0 

for i in range(1, n+1) : # 모든 수
    a = list(map(int, str(i))) # 숫자 i의 각 자리 수를 분리
    s = i + sum(a)
    
    if (s == n) :
        result = i
        break
        
print(result)


# 7568번 : 덩치 등수 구하기
N = int(input()) # 전체 사람의 수
people = []

for _ in range(N) :
    weight, height = map(int, input().split()) # 몸무게와 키
    people.append((weight, height)) # people 리스트에 몸무게와 키 넣어주기
    
for i in people :
    rank = 1 # 랭크 초기값
    
    for j in people :
        if i[0] < j[0] and i[1] < j[1] : # i보다 몸무게와 키가 클 경우
            rank += 1 # 랭크 상승
            
    print(rank, end = " ")


# 1018번 : 체스판 경우의 수
N, M = map(int, input().split())
chess = list()

for i in range(N) :
    chess.append(input())
    
fix = list()

for i in range(N-7) :
    for j in range(M-7) :
        first_W = 0 # 첫번째가 흰색
        first_B = 0 # 첫번째가 검은색
        
        for k in range(i, i+8) :
            for l in range(j, j+8) :
                if (k + l) % 2 == 0 :
                    if chess[k][l] != 'W' :
                        first_W = first_W + 1
                    if chess[k][l] != 'B' :
                        first_B = first_B + 1    
                else :
                    if chess[k][l] != 'B' :
                        first_W = first_W + 1
                    if chess[k][l] != 'W' :
                        first_B = first_B + 1 
                        
        fix.append(first_W)
        fix.append(first_B)
print(min(fix))


# 1436번 : N번째 종말의 수가 나올 때까지 차례대로 시도하기
N = int(input())

cnt = 0
title = 666

while True :
    if '666' in str(title) :
        cnt += 1
    
    if cnt == N :
        print(title)
        break
    
    title += 1