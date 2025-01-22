"""
*주제 가려놓고 풀어야 하는 이유.


[배운 것]
1. 절대적인 양 부족

[확인할 것]
1. 어떻게 접근하시는지

"""
n = int(input())
answer = 0

for i in range(1,n+1):
    for j in range(i,(n//i)+1):
        answer += 1
print(answer)