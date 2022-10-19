# 2869번 : 달팽이의 움직임 계산하기
import math # math 모듈 사용 (수학 공식을 계산해주는 함수 이용 가능)

A, B, V  = map(int, input().split())

day = (V - B) / (A - B) # 정상에 한 번 도달하면 밤에 미끄러지지 않게 하는 식

print(math.ceil(day)) # day가 나누어 떨어지지 않을 경우를 대비해 올림 처리


# 10250번 : 호텔 방 번호의 규칙 찾기
T = int(input()) # 입력받을 데이터의 개수

for i in range(T) :
    H, W, N = map(int, input().split()) # 호텔 층수, 각층의 방 수, 몇번째 손님인지
    
    num = N // H + 1 # 각층의 방 번호
    floor = N % H # 객실의 층
    
    # N이 H의 배수인 경우
    if N % H == 0 : # H의 배수이면
        num = N // H 
        floor = H
        
    print(f'{floor * 100 + num}')


# 2775번 : 층과 거주자 수의 규칙 찾기
T = int(input()) # 입력받을 데이터의 개수

for i in range(T) :
    k = int(input()) # 층
    n = int(input()) # 호
    
    people = [i for i in range(1, n+1)] # 0층
    
    for j in range(k) : # 층
        new = [] 
        
        for m in range(n) : # 호
            new.append(sum(people[:m+1])) # 아래층의 1 ~ n호 까지의 합
            
        people = new.copy()
    
    print(people[-1])


