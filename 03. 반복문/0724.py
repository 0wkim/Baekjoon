# 2738번 : 구구단
N = int(input())

for i in range(1, 10) :
    print(N, "*", i, "=", N*i)


# 10950번 : A+B를 여러 번 출력
T = int(input())

for i in range(T) :
    A, B = map(int, input().split())
    C = A + B
    print(C)


# 8393번 : 1부터 N까지의 합
n = int(input())
start = 0

for i in range(1, n+1) :
    start += i
print(start)


# 25304번 : 영수증
X = int(input()) # 총 금액
N = int(input()) # 물건의 종류의 수

sum = 0

for i in range(N) :
    a, b = map(int, input().split())
    
    sum = sum + (a*b)
    
if sum == X :
    print('Yes')
else :
    print('No')


# 15552번 : 빠르게 입출력 계산
import sys

T = int(input())

for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    C = A + B
    print(C)

# import sys로 선언 후 사용
# 처음 입력값에는 input을 사용해도 되지만, 반복문 사용시 시간단축을 위해서 sys를 사용해야 함
# jupyter notebook에서는 오류 발생


# 11021번 : A+B-7
T = int(input())

for i in range(T) :
    A, B = map(int, input().split())
    C = A + B
    print("Case #{}: {}".format(i+1, C))
