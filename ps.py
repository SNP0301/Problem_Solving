'''
[BOJ] 1107. 리모컨

T: 2s
M: 512MB
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
available_buttons = list()

def get_available_buttons(broken_buttons):
    available_buttons = [i for i in range(10)]
    for i in broken_buttons:
        available_buttons.remove(i)
    return available_buttons

def available_with_numbers(target, buttons):
    for i in str(target):
        if int(i) not in buttons:
            return False
    return True

if m != 0:
    broken_buttons =  list(map(int,input().split()))
    available_buttons = get_available_buttons(broken_buttons)
else:
    available_buttons = [i for i in range(10)]

current_min = abs(n-100)

for i in range(1000001):
    if available_with_numbers(i,available_buttons):
        current_press = abs(n-i) + len(str(i))
        current_min = min(current_min, current_press)


print(current_min)