# 10818번 : 최솟값과 최댓값
cnt = int(input()) # 정수의 개수 n개
num = list(map(int, input().split())) # n개의 정수를 공백으로 구분

print(min(num), max(num))


# 2562번 : 최댓값
num_list = []

for i in range(9) :
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1) # list는 0에서 시작

# append로 리스트 값 삽입
# .index()로 인덱스 값 구하기


