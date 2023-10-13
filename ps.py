'''
[BOJ] 18870. 좌표 압축
T: 2초
M: 512MB
'''
import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int,input().split()))
points_set = set(points)

points_list = list(points_set)
points_list.sort()
points_dict = dict()

for i in range(len(points_list)):
    points_dict.update({points_list[i]:i})

for i in points:
    print(points_dict[i],end=" ")
