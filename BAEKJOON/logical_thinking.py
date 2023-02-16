check_list = []
for i in range(0,31):
    check_list.append(0)
    
##name_list = []
for i in range(0,28):
    ##name_list.append(int(input()))
    new_number = int(input())
    check_list[new_number]=1


no_submit = []
for i in range(1,31):
    if(check_list[i]==0):
        no_submit.append(i)

print(min(no_submit))
print(max(no_submit))