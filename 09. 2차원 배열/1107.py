# 2566번 : 최댓값 구하기
import sys
input = sys.stdin.readline

num_list = []

for _ in range(9) :
    num_list.append(list(map(int, input().split())))

x = 0
y = 0
max = -1

for i in range(9) : 
    for j in range(9) :
        if num_list[i][j] > max :
            max = num_list[i][j]
            x = i+1 
            y = j+1 

print(max)
print(x, y)


# 2563번 : 검은 영역의 넓이 찾기
n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n) :
    x, y = map(int, input().split())
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            paper[i][j] = 1

answer = 0
for row in paper :
    answer += row.count(1)
print(answer)