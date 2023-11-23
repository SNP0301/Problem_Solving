'''
[BOJ] 14581. 팬들에게 둘러싸인 홍준
T: 1 s
M: 1024 MB
'''

import sys
input = sys.stdin.readline

id = input().rstrip()

print(":fan::fan::fan:")
print(":fan::%s::fan:"%(id))
print(":fan::fan::fan:")