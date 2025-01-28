N = int(input())
given_lst = list(map(int,input().split()))
my_lst = [0 for _ in range(63)]
my_lst[0] = given_lst.count(1)

for i in range(1,63):
    my_lst[i] += given_lst.count(2**i) + my_lst[i-1]//2

for i in range(62,-1,-1):
    if my_lst[i] != 0:
        print(2**i)
        break