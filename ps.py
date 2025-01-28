N, M = map(int,input().split())
number_list = list(map(int,input().split()))+[0] ## 5 4 3 2 1
sum_list = [0 for _ in range(N+1)] ## 0 5 9 12 14 15
sum_list[1] = number_list[0]
for i in range(2,N+1):
    sum_list[i] = sum_list[i-1] + number_list[i-1]
#print(sum_list)
for _ in range(M):
    start, end = map(int,input().split())
    print(sum_list[end]-sum_list[start-1])
