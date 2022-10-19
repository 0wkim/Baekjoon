# 25305번 : k번째로 큰 수 구하기
def sol(nums,k):
    nums.sort(reverse=True)
    print(nums[k - 1])
 
n,k=map(int, input().split())
nums=list(map(int, input().split()))
sol(nums,k)


