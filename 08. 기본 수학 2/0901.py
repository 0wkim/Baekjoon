# 1929번 : M이상 N이하의 소수를 모두 출력하기

M, N = map(int, input().split())

for i in range(M, N+1) :
    if i == 1 : # 1은 소수가 아니므로 제외하기
        continue
    for j in range(2, int(i**0.5)+1) : # 특정 수의 약수를 포함하는 수를 모두 제거
        if i % j == 0 : # 나누어 떨어지면 소수가 아니므로 검사 할 필요가 없어 멈춤
            break 
    else : # i가 1이 아니라면 해당 숫자 출력
        print(i)


# 4948번 : 소수 응용 문제 1
import sys

n_max = 123456
is_prime = [True] * (2 * n_max + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int((2 * n_max) ** 0.5) + 1):
    if is_prime[i]:
        j = 2
        while (i * j) <= (2 * n_max):
            is_prime[i * j] = False
            j += 1

while (n := int(sys.stdin.readline())) != 0:
    print(is_prime[n + 1:(2 * n) + 1].count(True))


# 9020번 : 소수 응용 문제 2
n = [0 for i in range(10001)]
n[1] = 1

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        n[j] = 1
        
t = int(input())

for i in range(t):
    a = int(input())
    b = a // 2
    
    for j in range(b, 1, -1):
        if n[a - j] == 0 and n[j] == 0:
            print(j, a - j)
            break