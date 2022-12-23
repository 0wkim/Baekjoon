# 10814번 : 나이순 정렬
# sys 라이브러리
import sys

n = int(sys.stdin.readline()) # 회원 수

member = [] # 회원 리스트

for i in range(n) :
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), i, name]) # 입력받은 순서대로 정렬하기 위해 i 추가

member.sort()

for i in range(len(member)) :
    print("%d %s" % (member[i][0], member[i][2]))


# 18870번 : 좌표
# sys 라이브러리
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []

# set 함수로 중복 제거 후 정렬
arr2 = list(sorted(set(arr)))

# dic 사용으로 시간 단축
dic = {arr2[i]:i for i in range (len(arr2))}

for i in arr:
    print(dic[i],end=' ')