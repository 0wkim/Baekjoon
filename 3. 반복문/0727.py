# 10952번 : 0 0이 들어올 때까지 A+B 출력
while True :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    else :
        print(A+B)


# 10951번 : 입력이 끝날 때까지 A+B 출력
while True : # 테스트케이스 개수가 주어지지 않음
        try : # try문 사용
            A, B = map(int, input().split())
            print(A+B)
        except : # try에 대한 에러 발생 시
            break


# 1110번 : 원래 수로 돌아올 때까지 연산 반복
n = int(input())
num = n
cnt = 0 # 사이클 수

while True :
    a = num // 10 # 10의 자리
    b = num % 10 # 1의 자리
    c = (a + b) % 10 # n의 자릿수 대로 합한 값의 1의 자리
    num = (b *10) + c # b가 10의자리가 되고, c와 이어짐

    cnt += 1 # 사이클 수 증가

    if (num == n) :
        break

print(cnt)