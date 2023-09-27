'''
[BOJ] 2839. 설탕 배달
T: 1s
M: 128MB
'''
import sys
input = sys.stdin.readline

n = int(input())

def sugar(num):
    total = 2
    while total<=num:
        for for_five in range(0,total+1):
            for_three = total-for_five
            #print("%d = %d + %d"%(total,for_five,for_three))
            if for_five*5 + for_three*3 == num:
                return for_five + for_three
        total += 1
    return -1


print(sugar(n))