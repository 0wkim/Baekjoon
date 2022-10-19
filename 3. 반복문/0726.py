# 11022번 : A+B-8
T = int(input())

for i in range(T) :
    A, B = map(int, input().split())
    C = A + B
    print("Case #{}: {} + {} = {}".format(i+1, A, B, C))


# 2438번 : 별 찍기 1
N = int(input())

for i in range(N) :
    i += 1
    print('*'*i)


# 2439번 : 별 찍기 2
N = int(input())

for i in range(1, N+1) : # 1부터 N번째 까지
    print(' '*(N-i) + '*'*i) # N-i로 공백을 넣고, 이어서 (곱하기)를 증가시키는 것


#10871번 : for문과 if문 같이 사용
n, x = map(int, input().split())
a = list(map(int, input().split())) # list로 감싸주기

for i in range(n) : # i가 n까지 반복
    if a[i] < x : # 만약 a의 리스트(i)값이 x보다 작을 경우
        print(a[i], end=" ") # x보다 작은 리스트 값을 출력한다.


