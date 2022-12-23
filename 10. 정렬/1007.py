# 2108번 : 정렬 활용
# 빠르게 입력값 받는 라이브러리
import sys

# Counter 함수
from collections import Counter

n = int(sys.stdin.readline())
nums = [] # 숫자를 담을 리스트

for _ in range(n) :
    nums.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(nums)/n))

# 중앙값
nums.sort() # 오름차순
print(nums[n//2]) # 중간값

# 최빈값
cnt_nums = Counter(nums).most_common() # Counter 함수 사용
if len(cnt_nums) > 1 and cnt_nums[0][1] == cnt_nums[1][1] :
    print(cnt_nums[1][0])
else :
    print(cnt_nums[0][0])

# 범위
print(max(nums) - min(nums)) # 최댓값 - 최솟값


# 1427번 : 숫자 정렬
n = int(input())

li = [] # 리스트

for i in str(n) : # 문자열
    li.append(int(i)) # 리스트에 삽입

# li = list(map(int,str(n))) 으로 단축 가능

li.sort(reverse=True) # 내림차순

for i in li :
    print(i, end='')


# 11650번 : 좌표 정렬
# 빠르게 입력값을 받는 라이브러리
import sys 

n = int(sys.stdin.readline())
li = []

for _ in range(n) :
    li.append(list(map(int, sys.stdin.readline().split())))

# lamdba 사용
li.sort(key = lambda x: (x[0], x[1]))

for i in li :
    print(i[0], i[1])


# 11651번 : 좌표 정렬 2
# 빠르게 입력값을 받는 라이브러리
import sys 

n = int(sys.stdin.readline())
li = []

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    li.append([y, x])

s_li = sorted(li)

for y, x in s_li :
    print(x, y)


