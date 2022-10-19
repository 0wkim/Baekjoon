# 11653번 : 소인수분해
N = int(input()) # 정수

if N == 1 :
    print('')
else : 
    for i in range(2, N + 1) : # 2부터 하나씩 나누기
        if N % i == 0 : 
            while N % i == 0 :
                print(i)
                N = N / i


