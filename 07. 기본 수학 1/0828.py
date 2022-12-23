# 2839번 : 5와 3을 최소 횟수로 합하여 N 만들기
N = int(input())

bag = 0 # 봉지
while N >= 0 :
    if N % 5 == 0 :  # 5의 배수이면
        bag += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
        
    N -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)


# 10757번 : 큰 수 A+B
A, B = map(int, input().split())

C = A + B
print(C)