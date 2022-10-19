# 10926번 : 입출력 응용
A = input()
print(A+'??!')


# 18108번 : 식을 세워 계산하기
A = int(input())
print(A-543)


# 3003번 : 체스판
chess = [1, 1, 2, 2, 2, 8]

piece = list(map(int, input().split()))

for i in range(6) :
    print(chess[i]-piece[i], end=' ')


# 10430번 : 4개의 계산식 계산하기
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


# 2588번 : 곱셈
A = int(input())
B = input()

print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))
print(A * int(B)) 


# 10171번 : 고양이 출력하기
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# 쓰고자 하는 문자에 (역슬래시)가 있는 경우에는 (역슬래시)를 두번 써서 구분한다.


# 10172번 : 개 출력하기
print('''\
|\\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|
''')


# 25083번 : 새싹 출력하기
print("""\
         ,r'"7
r`-_   ,'  ,/
 \\. ". L_r'
   `~\\/
      |
      |
""")