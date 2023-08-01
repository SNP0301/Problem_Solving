N = int(input())
for_five = 9999
for_three = 9999
for_mix = 9999
current_mix = 10000

if(N % 5 == 0):
    for_five = N//5

if(N % 3 == 0):
    for_three = N//3

for i in range(N//5,(N//3)+1):
    if(N-5*i <=0):
        break
    if((N-5*i)%3 == 0):
        for_mix = i + ((N-5*i)//3)
        break

if(for_five+for_three+for_mix == 29997):
    print(-1)
else:
    print(min(for_five,for_three,for_mix))