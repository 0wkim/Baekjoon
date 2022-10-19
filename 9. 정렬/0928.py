# 2751번 : 수 정렬하기 2
import sys

N = int(input())
N_list = []

for i in range(N) :
    N_list.append(int(sys.stdin.readline()))
    
# 정렬
M_list = sorted(N_list)

for j in range(len(M_list)) :
    print(M_list[j])


# 10989번 : 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
n_list = [0] * 10001

for _ in range(n) :
    n_list[int(sys.stdin.readline())] += 1



for i in range(10001) :
    if n_list[i] != 0 :
        for j in range(n_list[i]) :
            print(i)


