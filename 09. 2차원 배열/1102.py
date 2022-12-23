# 2738번 : 행렬 더하기
A, B = [], [] # A와 B의 리스트

n, m = map(int, input().split()) # 행렬의 크기

# 행렬 원소 입력
for row in range(n) :
    row = list(map(int, input().split()))
    A.append(row) # 추가

for row in range(n) :
    row = list(map(int, input().split()))
    B.append(row) # 추가

for row in range(n) :
    for col in range(m) :
        print(A[row][col] + B[row][col], end=' ')
    print() # 줄바꿈