# 10807번 : 배열을 입력받고 v찾기
n = int(input())

# 숫자 리스트 생성
num_list = list(map(int, input().split()))

v = int(input())

# count 사용
print(num_list.count(v))


# 5597번 : 특정 출석 번호 찾기
students = [i for i in range(1, 31)] # 전체 학생 번호

for _ in range(28) :
    s_num = int(input())
    students.remove(s_num) # 제출한 번호 제거

print(min(students))
print(max(students))

