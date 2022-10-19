# 1330번 : 두 수 비교
A, B = map(int, input().split())

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')


# 9498번 : 시험점수 계산하기
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")


# 2753번 : 윤년 판별
year = int(input())

if year % 4 == 0 and year % 100 != 0 :
    print(1)
elif year % 400 == 0 :
    print(1)
else :
    print(0)


# 14681번 : 사분면에서 점의 위치 찾기
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 :
    print(3)
elif x > 0 and y < 0 :
    print(4)


# 2884번 : 시간 계산하기
H, M = map(int, input().split())

if M > 45 :
    print(H, M-45)

elif M == 45 :
    print(H, 0)

elif M < 45 :
    if H <= 0 :
        H = 24 - 1 # 반례 : 1 0 을 통해서 최종 수정
        print(H, M+15)
        # 만약 M이 20일 경우, 20 - 45 = - 25, -25 + 60 = 35
        # M - 45 + 60 = M + 15
    else :
        print(H-1, M+15)


# 2525번 : 범위가 더 넓은 시간 계산하기
A, B = map(int, input().split())
C = int(input())

# 분에 필요한 시간을 더하기
B = B + C

# 시와 분 다시 계산
A = A + (B//60) # 나눴을때의 몫이 시에 더해지는 것
B = B % 60 # 나머지가 분이 되는 것

# 시가 24시를 넘어갈 경우, 0부터 다시 세기
if A >= 24 :
    A = A - 24
print(A, B)


# 2480번 : 조건에 따라 상금 계산하기
A, B, C = input().split()

if A == B == C :
    print(10000 + (int(A)*1000))
elif A == B or A == C :
    print(1000 + (int(A)*100))
elif B == C :
    print(1000 + (int(B)*100))
elif A > B and A > C :
    print(int(A)*100)
elif B > A and B > C :
    print(int(B)*100)
elif C > A and C > B :
    print(int(C)*100)