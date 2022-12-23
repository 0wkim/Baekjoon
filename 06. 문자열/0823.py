# 2908번 : 숫자를 뒤집어서 비교하기
a, b = input().split()

# 역수로 변환
a = int(a[::-1]) 
b = int(b[::-1]) 

if a > b :
    print(a)
else :
    print(b)


