'''
[BOJ] 1107. 리모컨
T: 2s
M: 256MB
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m == 0:
    broken_button = list()
else:
    broken_button = list(map(int,input().split()))

available_button = {i for i in range(0,10)} - set(broken_button)

def is_possible_channel(channel, available_button):
    for i in str(channel):
        if int(i) not in available_button:
            return False
    return True ### 숫자만으로 갈 수 있으면 False, +/- 조작해야 하면 False

def solution(goal, available_button):
    current_min = abs(goal-100)

    for channel in range(1000001):
        if is_possible_channel(channel,available_button):
            current_press = abs(goal-channel) + len(str(channel))
            current_min = min(current_min, current_press)
    print(current_min)
    return

solution(n,available_button)