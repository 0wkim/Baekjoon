# 15596번 : 정수 N개의 합

# solve(a) = 정수 n개가 주어졌을 때 주어진 정수의 합을 구하는 함수
def solve(a) : # 함수 생성 시 def 이용
    return sum(a) # 반환값


# 4673번 : 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력

# n은 d(n)의 생성자 ('33 + 3 + 3 = 39'에서 33은 39의 생성자)
# 생성자가 없는 숫자가 셀프 넘버 (42, 53, 64, ...)

# 함수 d(n) : n과 n의 각 자리수를 더하는 함수
def d(n) : 
    n = n + sum(map(int, str(n)))
    return n

# 생성자가 있는 수(셀프넘버가 아닌 수)들이 들어 갈 집합
nonSelfNum = set()

# 생성자가 있는 수(셀프넘버가 아닌 수)들 찾아서 넣기
for i in range(1, 10001) :
    nonSelfNum.add(d(i)) # add로 삽입
    
# 셀프넘버 출력하기
for b in range(1, 10001) :
    if b not in nonSelfNum :
        print(b)

