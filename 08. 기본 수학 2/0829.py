# 1978번 : 소수 판별 1
N = int(input()) # 수의 개수
number = list(map(int, input().split())) # 수
count = 0 # 소수의 개수

for x in number :
    for i in range(2, x+1) :
        if x % i == 0 :
            if x == i :
                count += 1
            break

print(count)


