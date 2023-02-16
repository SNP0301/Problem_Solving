cnt = 0

input_list = []
for i in range(10):
    input_list.append(int(input()))

div_check_list = []
for i in range(42):
    div_check_list.append(0)

for i in range(10):
    div_check_list[input_list[i]%42] = 1

for i in range(42):
    if(div_check_list[i]==1):
        cnt += 1

print(cnt)
