# 2447번 : 재귀함수 패턴으로 별 찍기
n = int(input())

# star 함수 생성
def star(n): 
    if n == 3 : # n이 3일 경우의 패턴 제작
        return ['***', '* *', '***']
    
    arr = star(n // 3) 
    stars = []
    
    for i in arr :
        stars.append(i * 3)           
        
    for i in arr :
        stars.append(i+' '*(n//3)+i) 
        
    for i in arr :
        stars.append(i * 3)            
        
    return stars 

print('\n'.join(star(n)))


# 11729번 : 재귀함수로 탑 이동 순서 찾기
n = int(input())

# hanoi 함수 생성
def hanoi(n, a, b, c): 
    if n == 1 : # n이 1일 경우
        print(a, c)
        
    else : 
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)
        
sum = 1
    
for i in range(n-1) :
    sum = sum * 2 + 1

print(sum)
hanoi(n, 1, 2, 3)