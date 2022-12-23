# 10872번 : 팩토리얼
N = int(input())

def factorial(N) : # factorial 함수 정의
    if N == 0 : # 입력받은 수가 0일때
        return 1 # 1로 반환
    return N * factorial(N - 1) # 입력값에 1을 빼고 계속해서 함수 반복

print(factorial(N))

# 만약 N이 5라면,
# 5 * 4 * 3 * 2 * 1
# 즉, 출력되는 N! 값은 120이다.


# 10870번 : 피보나치 수 
n = int(input()) # n번까지 실행

def fibonacci(n) : # fibonacci 함수 정의
    if n <= 1 : # n이 0 혹은 1 이라면
        return n # n값 반환
    return fibonacci(n-1) + fibonacci(n-2) 

    # 만약 n이 2라면,
    # (2-1) + (2-2) = 1 + 0 = 1
    # 2번째는 0과 1을 합한 1이 나온다.
    
print(fibonacci(n))


