# 2750번 : 수 정렬하기
N = int(input())
N_list = []

for i in range(N) :
    N_list.append(int(input()))
    
# 정렬
N_list = sorted(N_list)

for j in range(len(N_list)) :
    print(N_list[j])


