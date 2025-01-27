fb_arr = list()
for i in range(3):
    fb_arr.append(input())
    if 48<=ord(fb_arr[i][0])<=57:
        answer = int(fb_arr[i])+(3-i)

if answer % 3 == 0:
    if answer % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)