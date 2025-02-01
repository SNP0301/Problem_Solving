"""
[복잡도] O(n)
    - input 자체가 크지 않다.
"""

T = int(input())
nums = [0,1,1,1,2,2,3]+[0 for _ in range(94)]
for i in range(7,101):
    nums[i] = nums[i-1] + nums[i-5]
for _ in range(T):
    N = int(input())
    print(nums[N])
    

