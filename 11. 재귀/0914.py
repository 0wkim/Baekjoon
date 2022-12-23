# 25501번 : 재귀
import sys # 시간 초과가 되지 않기 위해 input() 대신 사용
input = sys.stdin.readline

def recursion(s, l, r):
    global cnt # 함수에서 cnt를 전역변수로 활용하기 위해 선언
    cnt += 1 
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)


