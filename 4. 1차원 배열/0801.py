# 8958번 : OX퀴즈의 점수 계산
cnt = int(input())

for i in range(cnt) :
    quiz = list(input())

    score = 0 #점수를 넣을 변수
    sum = 1 # 점수의 증가값

    for i in quiz :
        if i == 'O' :
            score = score + sum # 변수에 점수값이 들어감
            sum += 1 # 계속해서 점수가 증가
        else : # X를 만난 경우
            sum = 1 # sum은 증가하지 않음
    print(score)


# 4344번 : 평균값
C = int(input())

for i in range(C) :
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0]
    
    cnt = 0 # 평균이 넘는 학생 수
    for i in N[1:] :
        if i > avg :
            cnt += 1
    
    per = (cnt/N[0])*100 # 퍼센트 구하기
    
    print('{0:0.3f}%'.format(per))