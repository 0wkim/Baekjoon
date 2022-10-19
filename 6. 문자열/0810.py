# 1157번 : 단어에서 가장 많이 사용 된 알파벳 출력
word = input().upper() # 대문자로 변환
word_list = list(set(word)) # 중복 문자 제거

cnt = [] 

for i in word_list :
    count = word.count # 알파벳이 사용된 횟수 저장
    cnt.append(count(i)) # 리스트에 추가
    
if cnt.count(max(cnt)) > 1 : # 가장 많이 사용된 것이 2이상, 즉 중복된다면
    print("?")
else :
    print(word_list[(cnt.index(max(cnt)))])


