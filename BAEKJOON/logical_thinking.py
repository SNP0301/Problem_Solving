n = int(input())
new_n = (n%10)*10 + ((n//10)+(n%10))%10
cnt = 0

while True:
    if (n!=new_n):
        cnt += 1
        new_n = (new_n%10)*10 + ((new_n//10)+(new_n%10))%10
    else:
        print(cnt+1)
        break