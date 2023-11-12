'''
[BOJ] 15726. 이칙연산
T: 1 s
M: 256 MB
'''

a, b, c = map(int,input().split())

print(int(max(a*b/c,a/b*c)))