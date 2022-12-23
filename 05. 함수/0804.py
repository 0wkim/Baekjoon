# 1065번 : 함수 판별
N = int(input())
hansu = 0 # 한수를 넣을 변수

for i in range(1, N+1) : # 1부터 N까지의 수 중
    if i <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1 # 한수 증가
    else :
        nums = list(map(int, str(i))) # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2] : # 등차수열 확인
            hansu += 1 # 등차수열일 경우 한수 증가
print(hansu)