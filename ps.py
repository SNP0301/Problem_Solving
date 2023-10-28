'''
[BOJ] 1076. 저항
T: 1 s
M: 128 MB
'''

import sys
input = sys.stdin.readline

f = input().rstrip()
s = input().rstrip()
t = input().rstrip()

color_name = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
color_value = [i for i in range(0,10)]
color_multiplier = [10**i for i in range(10)]

before_multiple = int(color_name.index(f))*10+int(color_name.index(s))

for i in range(len(color_name)):
    if t == color_name[i]:
        print(before_multiple*color_multiplier[i])
        break