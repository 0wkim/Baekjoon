# 2581번 : 소수 판별 2
M = int(input()) # 시작 숫자
N = int(input()) # 마지막 숫자

decimal = [] # 소수 

for i in range(M, N+1) :
  for j in range(2, i+1) :
    if j == i : # 소수이면
      decimal.append(i)
    if i % j == 0 : # 소수가 아니면
      break 

if not decimal :
  print(-1)
else : 
  print(sum(decimal)) # 합
  print(decimal[0]) # 소수의 최솟값


