# 2798번 : 세장의 카드를 고르는 모든 경우
N, M = map(int, input().split()) # N = 카드 개수, M = 숫자
number = list(map(int, input().split())) # 카드에 쓰인 수

result = 0 # 결과값 저장 변수

for i in range(N) : # 모든 경우의 수 살피기
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if number[i] + number[j] + number[k] > M : # 세 카드 값이 M 보다 큰 경우
                continue
            else : # result에 저장
                result = max(result, number[i] + number[j] + number[k])
print(result)


