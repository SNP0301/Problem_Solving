'''
[BOJ] 27889. 특별한 학교 이름
T: 1 s
M: 512 MB
'''

import sys
input = sys.stdin.readline

n = input().rstrip()

if n == "NLCS":
    print("North London Collegiate School")
elif n == "BHA":
    print("Branksome Hall Asia")
elif n == "KIS":
    print("Korea International School")
elif n == "SJA":
    print("St. Johnsbury Academy")